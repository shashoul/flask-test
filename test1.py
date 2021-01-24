from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Python Flask..."


@app.route('/hello/<string:name>')
def getHello(name):
    return f"Hello {name}!!"


@app.route('/author')
def author():
    return "The Boss"


@app.route('/copyright')
def copyright():
    return "Copyright 2018"


@app.route('/post/<string:name>')
def getPost(name):
    return name

@app.route('/user/<name>/<age>')
def getUser(name, age):
    return f"{name} {age}"


@app.route('/product/<name>')
def getProduct(name):
    return f"{name}"

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)