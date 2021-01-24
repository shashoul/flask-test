from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def exampleIndex(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)