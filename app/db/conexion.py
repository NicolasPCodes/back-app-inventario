import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv
import os

class DatabaseConn:
    def __init__(self):
        load_dotenv()
        try:
            # self.db =  mysql.connector.connect(
            #     host=os.getenv("DB_HOST") ,
            #     user=os.getenv("DB_USER"),
            #     password=os.getenv("DB_PASSWORD"),
            #     database=os.getenv("DB_DATABASE"),
            #     port=int(os.getenv("DB_PORT")),
            #     # allow_multi_statements=True
            # )
            self.pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=10,
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE"),
                port=int(os.getenv("DB_PORT"))
            )
            print("Database connection established.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db = None

    def read(self, sql, values = None):
        if self.pool is None:
            print("No database connection.")
            return None
        # cursor = self.db.cursor(dictionary=True)
        conn = self.pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            # print(f"Query executed: {sql} with values {values}, Result: {result}")
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    def write(self, sql, values):
        if self.pool is None:
            print("No database connection.")
            return False
        # cursor = self.db.cursor()
        conn = self.pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, values)
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def write_many(self, sql, values_list):
        if self.pool is None:
            print("No database connection.")
            return False
        conn = self.pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.executemany(sql, values_list)
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
    
    def close_conection(self):
        if self.db:
            self.db.close()
            self.db = None