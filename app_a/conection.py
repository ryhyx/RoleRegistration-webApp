import mysql.connector
from mysql.connector import Error


# class for connecting to database
class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='192.168.108.123',
            database='rihtest',
            user='root',
            port=3306,
            password='1qaz!QAZ',
        )

        self.cursor = self.conn.cursor()

        if self.conn.is_connected():
            print('Successful connection')
        else:
            print("failed to connect")


class Register(DB):
    def read_by_user(self, user_id):
        try:
            query = f"SELECT * FROM users WHERE id = '{user_id}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()  # Fetch a single row
            self.conn.commit()
            print("Data rcv by user_id successfully")
            return result
        except Exception as e:
            print(e)
            pass
    def insert(self, FirstName, LastName, password_, acc):
        try:
            query = f"INSERT INTO users (FirstName, LastName, password_,acc) VALUES ('{FirstName}', '{LastName}',{password_},{acc})"
            # send the insert query to database,th execute
            self.cursor.execute(query)
            # make sure that insert done
            self.conn.commit()
            print("inserted successfully")
        except mysql.connector.Error as e:
            print(f"Error inserting data: {e}")

    def update(self, ID, FirstName, LastName, password_, acc):
        try:
            query = "UPDATE users SET FirstName = %s, LastName = %s, password_ = %s, acc = %s WHERE id = %s"
            values = (FirstName, LastName, password_, acc, ID)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("update was successfull")
        except mysql.connector.Error as e:
            print(f"Error while updating row: {e}")

    def read(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            results = self.cursor.fetchall()  #fetchall return each rows as a tuple

            if results:
                for result in results:
                    # Assuming the table has columns:
                    FirstName = result[0]
                    LastName = result[1]
                    password_ = result[2]
                    acc = result[3]

                    print(f"Firstname: {FirstName}")
                    print(f"Lastname: {LastName}")
                    print(f"password: {password_}")
                    print(f"acc: {acc}")

                return results
            else:
                print("seems you insert nothing")

        except mysql.connector.Error as e:
            print(f"Error reading data: {e}")

    def delete(self, id):
        try:
            query = f"DELETE FROM users WHERE id = '{id}'"
            self.cursor.execute(query)
            self.conn.commit()
            print("Data deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error deleting data: {e}")


