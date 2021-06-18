from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "cas-ur-vote")
    return f'Bienvenue chez {escape(name)} !'

@app.route('/singup', methods=['POST'])
def signUp():
    if request.method == 'POST':
        type = request.args.get('type')
        if type == "utilisateur":
            return f'User route'
        elif type == "week":
            return f'Candidate route'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'