from flask import Flask, render_template
from datetime import timedelta
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex 
app.permanent_session_lifetime = timedelta(days=1)


@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)