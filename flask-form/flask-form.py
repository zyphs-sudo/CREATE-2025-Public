from flask import (
    Flask, 
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for,
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
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] in login_info.keys() and login_info[request.form["username"]] == request.form["password"]:
            app.config["USERNAME"] = request.form["username"]
            app.config["PASSWORD"] = request.form["password"]
            return f"""<h1>Welcome to the Flask Form, {app.config["USERNAME"]}!</h1>
            <button onclick="location.href='/'">Go to Home</button>
            """
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form["username"] in login_info.keys():
            error = "Username already exists"
        elif request.form["password"] == "":
            error = "Password cannot be empty"
        elif request.form["username"] == "" or request.form["password"] == "":
            error = "Username and password cannot be empty"
        else: 
            login_info[request.form["username"]] = request.form["password"]
            app.config["USERNAME"] = request.form["username"]
            app.config["PASSWORD"] = request.form["password"]
            return f"""
            <h1>Registration successful! Welcome, {app.config["USERNAME"]}!</h1>
            <button onclick="location.href='/'">Go to Home</button>
            """
    return render_template('register.html', register_error=error)

if __name__ == "__main__":
    app.run()