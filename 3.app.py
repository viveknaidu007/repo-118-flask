from flask import *


app = Flask(__name__)



@app.route('/admin')
def admin():
    return 'this is admin'

@app.route('/student')
def vivek():
    return "pls subscribe"

@app.route('/staff')
def staff():
    return 'this is staff'


@app.route('/user<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='admin':
        return redirect(url_for('student'))
    if name=='admin':
        return redirect(url_for('staff'))
    

if __name__=='__main__':
    app.run()