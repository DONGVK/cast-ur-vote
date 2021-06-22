import mysql.connector
from mysql.connector import Error
import bcrypt

class DB :

    def __init__(self, con, cur):
        self.__connection = con
        self.__cursor = cur

    def connection(self):
        try:
            self.__connection = mysql.connector.connect(host='freedb.tech',
                                         database='freedbtech_sf',
                                         user='freedbtech_jn',
                                         password='123')
            if self.__connection.is_connected():
                db_Info = self.__connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.__cursor = self.__connection.cursor()
                self.__cursor.execute("select database();")
                record = self.__cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)

    def disconnect(self):
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()
            print("MySQL connection is closed")
        else:
            print("Not connected")
    
    def insertUser(self, firstName, lastName, birthDate, email, password, vote):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        self.connection()
        query = "INSERT INTO Utilisateur(firstName, lastName, birth_date, email, password, vote) VALUES(%s, %s, %s, %s, %s, %s)"
        tuple = (firstName, lastName, birthDate, email, hashed, vote)
        self.__cursor.execute(query, tuple)
        self.__connection.commit()
        self.disconnect()
     
    def selectUser(self):
        self.connection()
        self.__cursor.execute("SELECT * FROM Utilisateur")
        myresult = self.__cursor.fetchall()
        for x in myresult:
            print("Hi",x)
        self.disconnect()