from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "Ektor")
    return f'Bienvenue chez {escape(name)} !'

@app.route('/signup', methods=['POST'])
def turnover():
    if request.method == 'POST':
        type = request.args.get('type')
        if type == "user":
            return f'User route ...'
        elif type == "candidate":
            return f'Candidate route ...'
        else :
            return f'Please change the method or the parameters'
    else:
        return f'Please change the method or the parameters'