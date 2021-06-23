from flask import Flask, escape, request, jsonify
from flask_cors import CORS, cross_origin
from Db import *
import json

app = Flask(__name__)
DbSF = DB(None, None)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    name = request.args.get("name", "Cast\'ur\'Vote")
    return f'Bienvenue chez {escape(name)} !'

@app.route('/signup', methods=['POST'])
@cross_origin()
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
            print(email)
            print("Vote = ",vote)

            #For the vote permission
            if(vote.lower() == "true"):
                vote = True
            else:
                vote = False

            if(DbSF.userExist(email)):
                value = {
                    "message" : "Email already exist",
                }
                response = jsonify(value)
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response, 401
            else:
                DbSF.insertUser(firstName, lastName, birthDate, email, password, vote)
                value = {
                    "message" : "User created",
                }
                return json.dumps(value), 200

        elif type == "candidate":
            return f'Candidate route ...'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'

@app.route('/signin', methods=['POST'])
def signIn():
    if request.method == 'POST':
        type = request.args.get('type')
        if type == "user" :
            data = json.loads(request.data)
            email = data['email']
            pwd = data['password']
            return DbSF.testConnection(email, pwd)
        elif type == "candidate":
            return f'Candidate route ...'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'