"""
*   Db.py
*   @Author : DONG
"""
__author__      = "DONG"

import mysql.connector
from mysql.connector import Error
import bcrypt

class DB :

    def __init__(self, con, cur):
        self.__connection = con
        self.__cursor = cur

    #Connect to the DB
    def connection(self):
        try:
            """
            self.__connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                         database='sql11422138',
                                         user='sql11422138',
                                         password='VR9XRhUtuu')
            """
            
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


    #Disconnect from DB
    def disconnect(self):
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()
            print("MySQL connection is closed")
        else:
            print("Not connected")
    
    #----------------------------------------------
    # Utilisateur
    #----------------------------------------------
    
    # Add new user
    def insertUser(self, firstName, lastName, birthDate, email, password, vote, id_candidat):
        try:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode(), salt)
            self.connection()
            query = "INSERT INTO Utilisateur(first_name, last_name, birth_date, email, password, vote, id_candidat) VALUES(%s, %s, %s, %s, %s, %s, %s);"
            tuple = (firstName, lastName, birthDate, email, hashed, vote, id_candidat)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as e:
            print(e)
            return False

    # Get user's informations by is email
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
    
    # Get user information by his id_candidat
    def selectUserByIDC(self, id_candidat):
        self.connection()
        query = "SELECT * FROM Utilisateur WHERE id_candidat=%s;"
        info = (id_candidat,)
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
    
    # Check if an email is already taken or not
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

    # Get the user's password by his email
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
    
    # Check if the password provided by the user is the same during registration
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
    
    #----------------------------------------------
    # ACandidat
    #----------------------------------------------

    # Get all potentials candidates from the DB
    def selectAllACandidat(self):
        self.connection()
        query = "SELECT * FROM ACandidat;"
        self.__cursor.execute(query)
        myresult = self.__cursor.fetchall()
        """
        0 : idACandidat
        1 : lastname
        2 : firstname
        3 : birthdate
        4 : email
        5 : password
        6 : vote
        """
        self.disconnect()
        return myresult
    
    # Get the potentials candidates by his email
    def selectACandidat(self, email):
        self.connection()
        query = "SELECT * FROM ACandidat WHERE email = %s;"
        tuple = (email,)
        self.__cursor.execute(query, tuple)
        myresult = self.__cursor.fetchall()
        """
        0 : idACandidat
        1 : lastname
        2 : firstname
        3 : birthdate
        4 : email
        5 : password
        6 : vote
        """
        self.disconnect()
        return myresult

    # add a new potential canditate when the admin validate this candidate
    def insertACandidat(self, firstName, lastName, birthDate, email, password, vote):
        try :
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode(), salt)
            self.connection()
            query = "INSERT INTO ACandidat(first_name, last_name, birth_date, email, password, vote) VALUES(%s, %s, %s, %s, %s, %s);"
            tuple = (firstName, lastName, birthDate, email, hashed, vote)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Error:
            return False
    
    # Delete a potential candidate if the admin doesn't validate this candidate
    def deleteACandidat(self, email):
        try :
            self.connection()
            query = "DELETE FROM ACandidat WHERE email = %s;"
            tuple = (email,)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Error:
            return False

    #----------------------------------------------
    # Candidat
    #----------------------------------------------

    # Get all candidayes from the DB
    def selectAllCandidat(self):
        self.connection()
        query = "SELECT * FROM Candidat;"
        self.__cursor.execute(query)
        myresult = self.__cursor.fetchall()
        """
        0 : id_candidat
        1 : prog
        """
        self.disconnect()
        return myresult
        
    # Get a candidate by his id_candiate
    def selectCandidat(self, id):
        try :
            self.connection()
            query = "SELECT * FROM Candidat WHERE id_candidat = %s;"
            tuple = (id,)
            self.__cursor.execute(query, tuple)
            myresult = self.__cursor.fetchall()
            """
            0 : id_candidat
            1 : vote
            """
            self.disconnect()
            return myresult
        except Exception as error :
            print(error)
            return False
    
    # Update a candidate's program
    def updateCandidat(self, id, prog):
        try :
            self.connection()
            query = "UPDATE Candidat set prog = %s WHERE id_candidat = %s"
            tuple = (prog, id)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as error :
            print(error)
            return False

    # Add a new candidate
    def insertCandidat(self):
        try :
            self.connection()
            query = "INSERT INTO Candidat(prog) VALUES('');"
            self.__cursor.execute(query)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as error :
            print(error)
            return False

    # Get the id_candidate from the newest candidate added
    def selectNewCandidat(self):
        try :
            self.connection()
            query = "SELECT MAX(id_candidat) FROM Candidat;"
            self.__cursor.execute(query)
            myresult = self.__cursor.fetchall()
            """
            0 : id_candidat
            1 : vote
            """
            self.disconnect()
            return myresult[0][0]
        except Exception as error :
            print(error)
            return False

    # While the admin confirm a potential candidate, this PA change into a confirmed candidate 
    def confirmCandidat(self, email):
        try:
            self.connection()
            ac = self.selectACandidat(email)
            """ IN ac
            0 : id_acandidat
            1 : last_name
            2 : first_name
            3 : birth_date
            4 : email
            5 : password
            6 : vote
            """
            if(len(ac) == 1):
                if(self.insertCandidat()):
                    id_candidat = self.selectNewCandidat()
                    if(self.insertUser(ac[0][2], ac[0][1], ac[0][3], ac[0][4], ac[0][5], ac[0][6], id_candidat)):
                        self.deleteACandidat(email)
                        return True
            return False
        except Exception as e:
            print(e)
            return False
    