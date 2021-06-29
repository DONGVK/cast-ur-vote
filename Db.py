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
            """
            self.__connection = mysql.connector.connect(host='localhost',
                                         database='sf',
                                         user='root',
                                         password='123')
            """
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
        query = "INSERT INTO Utilisateur(first_name, last_name, birth_date, email, password, vote) VALUES(%s, %s, %s, %s, %s, %s);"
        tuple = (firstName, lastName, birthDate, email, hashed, vote)
        self.__cursor.execute(query, tuple)
        self.__connection.commit()
        self.disconnect()
     
    def selectUser(self, email):
        self.connection()
        query = "SELECT * FROM Utilisateur WHERE email=%s;"
        info = (email,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        """
        0 : iduser
        1 : lastname
        2 : firstname
        3 : birthdate
        4 : email
        5 : password
        6 : vote
        7 : idcandidate
        """
        self.disconnect()
        return myresult
    
    def userExist(self, email):
        self.connection()
        query = "SELECT * FROM Utilisateur WHERE email=%s;"
        info = (email,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        if len(myresult) > 0:
            print("User exist")
            return True
        else :
            return False

    def selectUserPassword(self, email):
        self.connection()
        query = "SELECT password FROM Utilisateur WHERE email=%s;"
        info = (email,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        self.disconnect()
        print(myresult)
        if len(myresult) == 1:
            return myresult[0][0]
        else :
            return None
    
    def testConnection(self, email, pwd):
        password = self.selectUserPassword(email)
        if password == None or password == "" or pwd == None or pwd == "" :
            value = {
                "message" : "User is not connected",
                "connected" : False
            }
            return value, 400

        if bcrypt.checkpw(pwd.encode() , password.encode()):
            value = {
                "message" : "User is connected",
                "connected" : True
            }
            return value, 200
        else:
            value = {
                "message" : "User is not connected",
                "connected" : False
            }
            return value, 401