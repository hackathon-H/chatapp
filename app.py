from flask import Flask, render_template,session,redirect
from datetime import timedelta
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex 
app.permanent_session_lifetime = timedelta(days=1)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')        

@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)