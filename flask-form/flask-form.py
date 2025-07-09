from flask import (
    Flask, 
    render_template, 
    request,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["USERNAME"] = "admin"
app.config["PASSWORD"] = "password"

login_info = {
    "admin": "password",
    "user": "1234",
    "guest": "guest", 
    "test": "test123"
}

@app.route('/')
def index():
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    

if __name__ == "__main__":
    app.run()