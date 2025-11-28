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