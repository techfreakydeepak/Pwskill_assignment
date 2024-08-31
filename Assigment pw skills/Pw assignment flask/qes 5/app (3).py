from flask import Flask, session, redirect, url_for,request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(days = 1)

@app.route("/")
def index():
    if 'username' in session:
        return f'Logged in as{session["username"]}'
    return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session.permanent=True
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return""" 
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """
@app.route('/logout')
def logout():
    session.app('username',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)