from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "cas'ur'vote")
    return f'Bienvenue chez {escape(name)} !'