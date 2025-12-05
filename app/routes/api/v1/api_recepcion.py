from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from app.db.db_querys import DB_Queries
import json
# Inicia variables de entorno
load_dotenv()
# Inicializa a aplicacion Flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
db_queries = DB_Queries()


# Endpoint de debug
@app.route('/', methods=['GET'])
def debug_main():
    return jsonify({"message": "Hello world!"}), 200

## BORRAR DESPUES DE PRUEBAS
@app.route('/insert-valores', methods=['GET'])
def insert_valores():
    db_queries.insert_prueba()
    return jsonify({"message": "Insert valores!"}), 200

@app.route('/insert-ocs-dev', methods=['GET'])
def insert_ocs_dev():
    data = request.get_json()
    num_oc = data.get('num_oc', 67860)
    db_queries.insert_OCS_prueba(num_oc)
    return jsonify({"message": "Insert OCS valores!"}), 200

@app.route('/get-valores-tables', methods=['POST'])
def querys_debug():
    data = request.get_json()
    table_name = data.get('table_name', 'prueba')
    result = db_queries.get_all(table_name)
    if result:
        return jsonify({"status": "success", "data": result}), 200
    else:
        return jsonify({"status": "error", "message": "No data found"}), 404

@app.route('/clean-tables', methods=['POST'])
def querys_clean_debug():
    data = request.get_json()
    table_name = data.get('table_name', 'prueba')
    result = db_queries.clean_table(table_name)
    if result:
        return jsonify({"status": "success", "data": result}), 200
    else:
        return jsonify({"status": "error", "message": "No data found"}), 404
## BORRAR DESPUES DE PRUEBAS

# Endpoint para obtener recepcion
@app.route('/recepcion', methods=['POST'])
def recepcionar_producto():
    # Obtener datos de request
    data = request.get_json()
    sku_producto = data['sku']
    numero_oc = data['numero_oc']

    # Crear cursor
    producto = db_queries.get_producto(sku_producto, numero_oc)
    if producto:
        return jsonify({"status": "success", "data": producto}), 200
    else:
        return jsonify({"status": "error", "message": "Producto no encontrado"}), 404

# Endpoint para obtener listado OC por tienda
@app.route('/listar_oc', methods=['POST'])
def listar_oc_tienda():
    data = request.get_json()
    store_id = data['store_id']

    # Obtener listado de OC
    oc_list = db_queries.get_all_oc(store_id)

    if oc_list:
        return jsonify({"status": "success", "data": oc_list}), 200
    else:
        return jsonify({"status": "error", "message": "No se encontraron OC"}), 404


# Endpoint para obtener detalle OC
@app.route('/detalle_oc', methods=['POST'])
def detalle_oc():
    data = request.get_json()
    oc_number = data['numero_oc']

    # Obtener detalle de OC
    oc_detail = db_queries.get_detail_oc(oc_number)
    if not oc_detail:
        return jsonify({"status": "error", "message": "OC no encontrada"}), 404
    # else:
    # Valida estado de recepcion por SKU
    line_sku_list = [item['id_oc'] for item in oc_detail]
    # print(f"SKUs in OC: {line_sku_list}")
    # print(f"DETALLE in OC: {oc_detail}")
    oc_recep_detail = db_queries.validate_sku_recepcionado( line_sku_list )
    if oc_recep_detail is None:
        oc_recep_list = []
    else:
        oc_recep_list = [id_oc['id_oc'] for id_oc in oc_recep_detail]
    # Ids encontrados se cruzan con el detalle OC y se deja el estado como true o false
    for oc_select in oc_detail:
        if len(oc_recep_list) > 0 and oc_select['id_oc'] in oc_recep_list:
            oc_select['estado'] = True
        else:
            oc_select['estado'] = False
    # print(f"Reception details for OC: {oc_recep_detail}")
    return jsonify({"status": "success", "data": oc_detail}), 200
    

# Endpoint para actualizar recepcion de liena OC
@app.route('/actualizar_recepcion', methods=['POST'])
def actualizar_recepcion():
    data = request.get_json()
    if type(data) is str:
        data = json.loads(data)
    print(f"Received request data: {type(data)}")
    print(f"Received request data content: {data}")
    print('-'*100)
    numero_oc = data['doc']
    comentario = data['comment']
    id_usuario = data['id_user']
    sku_producto_list = data['data']
    # cantidad_recepcionar = data['cantidad_recepcionar']

    print(f"Received data: products={sku_producto_list}, OC={numero_oc}, Comment={comentario}")

    # Valida que no haya sido recepcionado
    product_list_corregido = []
    for producto in sku_producto_list:
        sku_producto = producto['sku']
        cantidad_recepcionar = producto['cantidad']
        id_oc_recepcionar = db_queries.get_id_oc_sku(sku_producto, numero_oc)
        if id_oc_recepcionar is None:
            return jsonify({"status": "error", "message": f"SKU {sku_producto} o Numero OC {numero_oc} no validos"}), 404
        product_list_corregido.append({"id_oc_recepcionar": id_oc_recepcionar[0]['id_oc'], "sku_producto": sku_producto, "cantidad_recepcionar": cantidad_recepcionar})

    if len(product_list_corregido) == 0:
        return jsonify({"status": "error", "message": "No se encontro uno de los productos."}), 404

    print(f"Corrected product list: {product_list_corregido}")
    list_ids_oc = [prod['id_oc_recepcionar'] for prod in product_list_corregido]
    print(f"List of OC IDs to validate: {list_ids_oc}")
    lista_error_recepcion = []
    ## Fecha de recepcion
    fecha_recepcion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for producto in product_list_corregido:
        id_oc_recepcionar = producto['id_oc_recepcionar']
        sku_producto = producto['sku_producto']
        cantidad_recepcionar = producto['cantidad_recepcionar']
        # Prepara variable para insert
        # Inicia recepcion
        print(f"Updating reception for SKU: {sku_producto}, OC ID: {id_oc_recepcionar}, Quantity: {cantidad_recepcionar}")

        # Valida que no este en tabla recepcion
        validacion_recepcion = db_queries.get_recepcionado_line(id_oc_recepcionar)
        print(f"Reception validation for OC ID {id_oc_recepcionar}: {validacion_recepcion}")
        if validacion_recepcion:
            return jsonify({"status": "error", "message": f"El SKU {sku_producto} ya ha sido recepcionado."}), 400

        # Valida cantidades
        # Ingresa recepcion en la tabla
        insert_values = db_queries.insert_recepcion_producto(
            id_oc=id_oc_recepcionar,
            id_usuario=id_usuario,
            fecha=fecha_recepcion,
            cantidad_recepcionada=cantidad_recepcionar,
            comentario=comentario,
        )
        print(f"Insert values result: {insert_values}")
        if not insert_values:
            lista_error_recepcion.append(sku_producto)
            print(f"Error inserting reception for SKU {sku_producto}")
            continue

    # Actualizar recepcion
    if len(lista_error_recepcion) > 0:
        return jsonify({"status": "error", "message": f"Error al insertar recepcion para los siguientes SKUs: {', '.join(lista_error_recepcion)}"}), 500

    return jsonify({"status": "success", "message": "Recepcion actualizada"}), 200
