"""
*   app.py
*   @Author : DONG
"""
__author__      = "DONG"

import datetime
from flask import Flask, escape, request, session, jsonify
from flask_cors import CORS, cross_origin
from Db import *
import json

app = Flask(__name__)
app.secret_key = "abc"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.update(SESSION_COOKIE_SECURE=True)
CORS(app)
DbSF = DB(None, None)



@app.route('/')
def hello():
    name = request.args.get("name", "Cast\'ur\'Vote")
    return f'Bienvenue chez {escape(name)} !'


"""

Sign up for 2 roles : User & Candidate

"""  

@app.route('/signup', methods=['POST'])
@cross_origin(supports_credentials=True)
def signUp():
    if request.method == 'POST':
        type = request.args.get('type') # Get wich role is it

        if type == "user" :
            data = json.loads(request.data)
            firstName = data['firstname']
            lastName = data['lastname']
            birthDate = data['date']
            email = data['email']
            password = data['password']
            vote = data['vote']

            if(DbSF.userExist(email)): # Control if the email is alreade taken or not
                value = {
                    "message" : "Email already exist",
                }
                response = jsonify(value)
                return response, 401
            else:
                DbSF.insertUser(firstName, lastName, birthDate, email, password, vote, None)
                value = {
                    "message" : "User created",
                }
                return json.dumps(value), 200

        elif type == "candidat":
            data = json.loads(request.data)
            firstName = data['firstname']
            lastName = data['lastname']
            birthDate = data['date']
            email = data['email']
            password = data['password']
            vote = data['vote']

            if(DbSF.userExist(email)):
                value = {
                    "message" : "Email already exist",
                }
                response = jsonify(value)
                return response, 401
            else:
                DbSF.insertACandidat(firstName, lastName, birthDate, email, password, vote)
                value = {
                    "message" : "ACandidat created",
                }
                return json.dumps(value), 200
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'

"""

Log in for user

"""  

@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def signIn():
    if request.method == 'POST':
        type = request.args.get('type')
        if type == "user" :
            data = json.loads(request.data)
            email = data['email']
            pwd = data['password']
            response, status = DbSF.testConnection(email, pwd)
            if status == 200 :
                resUser = DbSF.selectUser(email)
                userV = {
                    "idUser": resUser[0][0],
                    "email" : resUser[0][4],
                    "idCandidate" : resUser[0][7],
                }
                response.update(userV)
            print("La réponse est : ",response)
            return json.dumps(response), status
        elif type == "candidate":
            return f'Candidate route ...'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'

"""

Get all candidates

"""  
@app.route('/getcandidat', methods=['GET'])
@cross_origin(supports_credentials=True)
def getCandidat():
    if request.method == 'GET':
        candidates = []
        res = DbSF.selectAllCandidat()
        for i in range(len(res)):
            candidat = list(DbSF.selectUserByIDC(res[i][0])[0])
            candidat[3] = myconverter(candidat[3])
            candidates.append(tuple(candidat + [res[i][1]]))
            print(candidates)
        if(len(res) > 0) :
            return json.dumps({ "data" : candidates}), 200
        return json.dumps({"message" : "Aucun candidat"}), 500
    else:
        return f'Please change the method or the parameters'

def myconverter(d):
    if isinstance(d, datetime.datetime):
        return d.__str__()