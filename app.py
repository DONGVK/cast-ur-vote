"""
*   app.py
*   @Author : DONG
"""
__author__      = "DONG"

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

@app.route('/signup', methods=['POST'])
@cross_origin(supports_credentials=True)
def signUp():
    if request.method == 'POST':
        type = request.args.get('type')

        if type == "user" :
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
                response.headers.add('Access-Control-Allow-Origin', '*')
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