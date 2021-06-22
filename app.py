from flask import Flask, escape, request
from Blockchain import *
from Db import *

app = Flask(__name__)
DbSF = DB(None, None)

@app.route('/')
def hello():
    name = request.args.get("name", "Cast\'ur\'Vote")
    return f'Bienvenue chez {escape(name)} !'

@app.route('/signup', methods=['POST'])
def signUp():
    if request.method == 'POST':
        type = request.args.get('type')
        if type == "user" :
            firstName = request.form.get('firstName')
            lastName = request.form.get('lastName')
            birthDate = request.form.get('birthDate')
            email = request.form.get('email')
            password = request.form.get('password')
            print(firstName)
            vote = request.form.get('vote')
            if(vote.lower() == "true"):
                vote = True
            else:
                vote = False
            DbSF.insertUser(firstName, lastName, birthDate, email, password, vote)
            return f'User route ...'
        elif type == "candidate":
            return f'Candidate route ...'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'
