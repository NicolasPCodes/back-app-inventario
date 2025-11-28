from flask import Flask, jsonify, request
import mysql.connector
from dotenv import load_dotenv
import os
from app.db.db_querys import DB_Queries
# Inicia variables de entorno
load_dotenv()
# Inicializa a aplicacion Flask
app = Flask(__name__)
db_queries = DB_Queries()


# Endpoint de debug
@app.route('/', methods=['GET'])
def debug_main():
    return jsonify({"message": "Hello world!"}), 200

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
    if oc_detail:
        return jsonify({"status": "success", "data": oc_detail}), 200
    else:
        return jsonify({"status": "error", "message": "OC no encontrada"}), 404

# Endpoint para actualizar recepcion de liena OC
@app.route('/actualizar_recepcion', methods=['POST'])
def actualizar_recepcion():
    data = request.get_json()
    sku_producto = data['sku']
    numero_oc = data['numero_oc']
    cantidad_recepcionada = data['cantidad_recepcionada']

    # Actualizar recepcion
    update_status = db_queries.update_recepcion(sku_producto, numero_oc, cantidad_recepcionada)
    if update_status:
        return jsonify({"status": "success", "message": "Recepcion actualizada"}), 200
    else:
        return jsonify({"status": "error", "message": "Error al actualizar recepcion"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
# # Inicia variables de entorno
# load_dotenv()
# # Inicializa a aplicacion Flask
# app = Flask(__name__)

# # Conexion db
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="niebla2018",
#     database="recepcion_dbs"
# )

# # Endpoint para obtener recepcion
# @app.route('/recepcion', methods=['POST'])
# def recepcionar_producto():
#     # Obtener datos de request
#     data = request.get_json()
#     sku_producto = data['sku']
#     numero_oc = data['numero_oc']

#     # Crear cursor
#     cursor = db.cursor(dictionary=True)
#     sql = f"SELECT * FROM orden_compra WHERE sku = {sku_producto} AND numero_oc = {numero_oc}"
#     cursor.execute(sql)
#     producto = cursor.fetchone()
#     cursor.close()
#     if producto:
#         return jsonify({"status": "success", "data": producto}), 200
#     else:
#         return jsonify({"status": "error", "message": "Producto no encontrado"}), 404



# if __name__ == '__main__':
#     app.run(debug=True)




    # if producto:
    #     return jsonify({"status": "success", "data": producto}), 200
    # else:
    #     return jsonify({"status": "error", "message": "Producto no encontrado"}), 404
# from flask import Flask, jsonify, request
# import mysql.connector
# from dotenv import load_dotenv
# import os

# # Inicia variables de entorno
# load_dotenv()
# # Inicializa a aplicacion Flask
# app = Flask(__name__)

# # Conexion db
# db = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_DATABASE")
# )

# # Endpoint para obtener recepcion
# @app.route('/recepcion', methods=['POST'])
# def recepcionar_producto():
#     # Obtener datos de request
#     data = request.get_json()
#     sku_producto = data['sku']
#     numero_oc = data['numero_oc']

#     # Crear cursor
#     cursor = db.cursor(dictionary=True)
#     sql = "SELECT * FROM orden_compra WHERE sku = %s AND numero_oc = %s"
#     cursor.execute(sql, (sku_producto, numero_oc))
#     producto = cursor.fetchone()
#     cursor.close()

#     if producto:
#         return jsonify({"status": "success", "data": producto}), 200
#     else:
#         return jsonify({"status": "error", "message": "Producto no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)