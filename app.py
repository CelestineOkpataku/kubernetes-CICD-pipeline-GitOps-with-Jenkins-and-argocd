from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'i love this cake, it is yummy!'