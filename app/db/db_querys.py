from app.db.conexion import DatabaseConn

class DB_Queries:
    def __init__(self):
        self.db = DatabaseConn()

    def get_producto(self, sku_producto, numero_oc):
        sql = "SELECT id_oc FROM orden_compra WHERE sku = %s AND numero_oc = %s"
        values = (sku_producto, numero_oc)
        result = self.db.read(sql, values)
        if result:
            return result
        return None

    def get_all_oc(self, store_id):
        sql = "SELECT DISTINCT numero_oc FROM orden_compra WHERE tienda = %s"
        values = (store_id,)
        result = self.db.read(sql, values)
        print(f"DB Query Result: {result}")
        if result:
            return result
        return None

    def get_detail_oc(self, oc_number):
        sql = "SELECT * FROM orden_compra WHERE numero_oc = %s"
        values = (oc_number,)
        result = self.db.read(sql, values)
        if result:
            return result
        return None
    
    def get_id_oc_sku(self, sku_producto, numero_oc):
        sql = "SELECT id_oc, cantidad FROM orden_compra WHERE sku = %s AND numero_oc = %s"
        values = (sku_producto, numero_oc)
        result = self.db.read(sql, values)
        if result:
            return result
        return None

    def get_id_user(self, username):
        sql = "SELECT id_usuario FROM usuarios WHERE nombre = %s"
        values = (username,)
        result = self.db.read(sql, values)
        if result:
            return result[0]['id_usuario']
        return None
    
    def valida_sku_oc(self, sku_producto, numero_oc):
        sql = "SELECT cantidad_recepcionada FROM orden_compra WHERE sku = %s AND numero_oc = %s"
        values = (sku_producto, numero_oc)
        result = self.db.read(sql, values)
        if result:
            return result
        return None
    
    def get_recepcionado_line(self, id_oc):
        sql = "SELECT cantidad_recibida FROM recepcion WHERE id_oc = %s"
        values = (id_oc,)
        result = self.db.read(sql, values)
        if result:
            return result
        return None
    
    def insert_recepcion_producto(self, id_oc, id_usuario, fecha, cantidad_recepcionada, comentario, ):
        # id_oc, usuario, fecja, cantidad_recibida, estado_recepcion, comentario
        sql = "INSERT INTO recepcion (id_oc, usuario, fecha, cantidad_recibida, estado_recepcion, comentario) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_oc, id_usuario, fecha, cantidad_recepcionada, 1, comentario)
        result = self.db.write(sql, values)
        return result
    
    def insert_prueba(self):
        sql = """
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12345',1,'Labial blush','Tinte rojo para labios.','Labios');
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12346',2,'Labial brillo','Brillo para labios.','Labios');
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12347',3,'Sombras','Sombras para ojos.','Ojos');
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12385',4,'Encrespador','Especial para pestañas.','Ojos');
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12349',5,'Skincare facial','Cuidado facial.','Cara');
        INSERT INTO `productos` (`sku`,`id_producto`,`nombre`,`descripcion`,`categoria`) VALUES ('SKU12310',6,'Bloqueador en barra','Cuidado facial.','Cara');
        INSERT INTO `usuarios` (`nombre`, `apellido`, `fecha_creacion`, `estado_usuario`, `rol`, `password_hash`)VALUES("Nicolas", "Paredes", "2025-11-02 12:00:00", 'activo', 'encargado', "abc12354");
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (1,'OC-67890','SKU12345','COS',100);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (3,'OC-67890','SKU12310','COS',10);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (4,'OC-67892','SKU12346','COS',100);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (5,'OC-67892','SKU12347','COS',120);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (6,'OC-67892','SKU12385','COS',200);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (7,'OC-67893','SKU12346','MAI',200);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (8,'OC-67893','SKU12347','MAI',20);
        INSERT INTO `orden_compra` (`id_oc`,`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES (9,'OC-67894','SKU12385','MAI',200);"""
        result = self.db.write(sql, ())
        return result

    def insert_OCS_prueba(self, num_oc):
        # sql = f"""
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc)}','SKU12345','COS',100);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc)}','SKU12310','COS',10);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 1}','SKU12346','COS',100);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 1}','SKU12347','COS',120);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 1}','SKU12385','COS',200);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 2}','SKU12346','MAI',200);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 2}','SKU12347','MAI',20);
        # INSERT INTO `orden_compra` (`numero_oc`,`sku`,`tienda`,`cantidad`) VALUES ('OC-{int(num_oc) + 3}','SKU12385','MAI',200);"""
        sql = """INSERT INTO orden_compra (numero_oc, sku, tienda, cantidad)
             VALUES (%s, %s, %s, %s)"""

        data = [
            ("OC-{}".format(num_oc), "SKU12345", "COS", 100),
            ("OC-{}".format(num_oc), "SKU12310", "COS", 10),
            ("OC-{}".format(num_oc + 1), "SKU12346", "COS", 100),
            ("OC-{}".format(num_oc + 1), "SKU12347", "COS", 120),
            ("OC-{}".format(num_oc + 1), "SKU12385", "COS", 200),
            ("OC-{}".format(num_oc + 2), "SKU12346", "MAI", 200),
            ("OC-{}".format(num_oc + 2), "SKU12347", "MAI", 20),
            ("OC-{}".format(num_oc + 3), "SKU12385", "MAI", 200),
        ]
        result = self.db.write_many(sql, data)
        return result

    def get_all(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        result = self.db.read(sql)
        if result:
            return result
        return None

    def clean_table(self, table_name):
        sql = f"DELETE FROM {table_name}"
        result = self.db.write(sql, ())
        return result