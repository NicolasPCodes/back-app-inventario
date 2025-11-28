import mysql.connector
from dotenv import load_dotenv
import os

class DatabaseConn:
    def __init__(self):
        load_dotenv()
        try:
            self.db =  mysql.connector.connect(
                host=os.getenv("DB_HOST") ,
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE"),
                port=int(os.getenv("DB_PORT"))
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db = None

    def read(self, sql, values = None):
        if self.db is None:
            print("No database connection.")
            return None
        cursor = self.db.cursor(dictionary=True)
        try:
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        # finally:
        #     cursor.close()

    def write(self, sql, values):
        if self.db is None:
            print("No database connection.")
            return False
        cursor = self.db.cursor()
        try:
            cursor.execute(sql, values)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db.rollback()
            return False
        # finally:
        #     cursor.close()

    def close_conection(self):
        if self.db:
            self.db.close()
            self.db = None