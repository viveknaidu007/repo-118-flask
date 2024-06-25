from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def kiran(name):
    return 'please subscribe' + name


if __name__=='__main__':
    app.run(debug=True)