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
            #"""
            self.__connection = mysql.connector.connect(host='freedb.tech',
                                         database='freedbtech_sf',
                                         user='freedbtech_jn',
                                         password='123')
            #"""                           
            
            """
            self.__connection = mysql.connector.connect(host='localhost',
                                         database='sf',
                                         user='root',
                                         password='123')
            """
            
            if self.__connection.is_connected():
                db_Info = self.__connection.get_server_info() # Connection info
                self.__cursor = self.__connection.cursor()
                self.__cursor.execute("select database();")
                record = self.__cursor.fetchone() # Database

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
    # @param [string] Contains user's information
    # @return [boolean] If the user is sucessfully added return true otherwise false
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
    # @param [string] User's email
    # @return [array] return an array with the user's informations
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
    # @param [string] User's id_candidat
    # @return [array] return an array with the user's informations
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
    # @param [string] User's email
    # @return [boolean] return true if the user exists otherwise false
    def userExist(self, email):
        self.connection()
        query = "SELECT * FROM Utilisateur WHERE email=%s;"
        info = (email,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        if len(myresult) > 0: # User exist
            return True
        else :
            return False

    # Get the user's password by his email
    # @param [string] User's email
    # @return [string] return a string if we found the password linked by the email, return None if the password doesn't exist
    def selectUserPassword(self, email):
        self.connection()
        query = "SELECT password FROM Utilisateur WHERE email=%s;"
        info = (email,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        self.disconnect()
        if len(myresult) == 1:
            return myresult[0][0]
        else :
            return None
    
    # Check if the password provided by the user is the same during registration
    # @param [string] User's email & password
    # @return [object, int] return an object depending on the combinaison provided by the user
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
    # @return [array] return an array with the potential candidates' informations from ACandidat table
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
    # @param [string] User's email
    # @return [array] return an array with the user's informations
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
    # @param [string] User's information
    # @return [boolean] return true if the potential candidate is added otherwise false.
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
    # @param [string] User's email
    # @return [array] return true if the user id deleted otherwise false
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
    # @return [array] return all the rows which contain all candidates 
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
        
    # Get a candidate by his id_candidat
    # @param [string] Candidate's id_candidat
    # @return [array] return an array with the candidat's informations
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
    # @param [int, string] Candidate id_candidat and program
    # @return [boolean] return true if the candidat program is sucessfully updated otherwise false
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
    # @return [boolean] return true if the candidat is sucessfully created otherwise false
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
    # @return [int or boolean] return the id_candidat of the latest created candidate, if there an error return false
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
    # @param [string] Potential candidate's email
    # @return [boolean] return true if the potential candidat turn into a candidat successfully otherwise false
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

    #----------------------------------------------
    # Voter
    #----------------------------------------------

    """    
    # AVote represent all users who already voted
    """

    # Check if an user already vote or not
    # @param [int] user's id
    # @return [boolean] return true if the user already voted otherwise false
    def selectAVote(self, id_user):
        self.connection()
        query = "SELECT * FROM AVote WHERE id_user=%s;"
        info = (id_user,)
        self.__cursor.execute(query, info)
        myresult = self.__cursor.fetchall()
        """
        0 : iduser
        """
        self.disconnect()
        if (len(myresult) == 0):
            return False
        else:
            return True

    # Add the user in the "user who voted"
    # @param [string] User's id
    # @return [boolean] return true if the user is sucessfully added otherwise false
    def insertAVote(self, id_user):
        try:
            self.connection()
            query = "INSERT INTO AVote(id_user) VALUES (%s);"
            tuple = (id_user,)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as e:
            print(e)
            return False

    # Delete a vote
    # @param [string] User's email
    # @return [boolean] return true if the user's vote is successfully deleted otherwise false
    def deleteAVote(self, id_user):
        try:
            self.connection()
            query = "DELETE FROM AVote WHERE id_user = %s;"
            tuple = (id_user,)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as e:
            print(e)
            return False

    # Check how many user voted
    # @return [int] return the number of user who already voted
    def countAVote(self):
        self.connection()
        query = "SELECT COUNT(*) FROM AVote;"
        self.__cursor.execute(query,)
        myresult = self.__cursor.fetchall()
        self.disconnect()
        return myresult[0][0]

    """    
    # Resultat represent the result of the election
    """

    # Insert row which determine each candidate's number of vote
    # @return [boolean] return true if the rows are successfully added otherwise false
    def initResult(self):
        try:
            number_candidat = self.selectAllCandidat()
            if(len(number_candidat) > 0):
                self.connection()
                self.__cursor.execute("DELETE FROM Resultat;")
                self.__cursor.execute("DELETE FROM Avote;")
                query = "INSERT INTO Resultat(id_candidat, nombre) VALUES (%s, %s);"
                tuple = (0, 0,)
                self.__cursor.execute(query, tuple)
                for i in range(len(number_candidat)):
                    query = "INSERT INTO Resultat(id_candidat, nombre) VALUES (%s, %s);"
                    tuple = ((i+1), 0,)
                    self.__cursor.execute(query, tuple)
                self.__connection.commit()
                self.disconnect()
            return True
        except Exception as e:
            print(e)
            return False
    
    # See the results
    # @return [array] return an array with the results
    def selectAllResult(self):
        self.connection()
        query = "SELECT * FROM Resultat;"
        self.__cursor.execute(query)
        myresult = self.__cursor.fetchall()
        """
        0 : id_candidat
        1 : nombre
        """
        self.disconnect()
        return myresult

    # Select the candidat's result
    # @param [int] candidate's id_candidat
    # @return [array] return an array with the candidat's result informations
    def selectResult(self, id_candidat):
        self.connection()
        query = "SELECT * FROM Resultat WHERE id_candidat = %s;"
        tuple = (id_candidat,)
        self.__cursor.execute(query, tuple)
        myresult = self.__cursor.fetchall()
        """
        0 : id_candidat
        1 : nombre
        """
        self.disconnect()
        return myresult

    # If an user vote for a candidat, the candidat voice number will increase by 1
    # @param [int] candidat's id
    # @return [boolean] return true if the candidate's vote increment, otherwise false
    def incrementResult(self, id_candidat):
        try:
            nombre = self.selectResult(id_candidat)[0][1] + 1
            self.connection()
            query = "UPDATE Resultat SET nombre = %s WHERE id_candidat = %s"
            tuple = (nombre, id_candidat)
            self.__cursor.execute(query, tuple)
            self.__connection.commit()
            self.disconnect()
            return True
        except Exception as e:
            print(e)
            return False
