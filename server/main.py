from flask import Flask,request
import authenticate

app = Flask(__name__)

@app.route("signup", methods=['POST'])
def signup():
    email = request.args["email"]
    password = request.args["password"]
    return authenticate.signup(username, password)
    
@app.route("/login", methods=['POST'])
def login():
    email = request.args["email"]
    password = request.args["password"]
    return authenticate.login(username, password)

@app.route("/fetch")
def fetch():
    """Fetch all folders and their content"""
    return True

@app.route("/createFolder")
def create_folder():
    """Create a folder"""
    return True

@app.route("/deleteFolder")
def delete_folder():
    """Delete the folder"""
    return True

@app.route("/addLink")
def add_link():
    """Add a link to a folder"""
    return True

@app.route("/removeLink")
def remove_link():
    """Remove the link from folder"""

@app.route("/share")
def share():
    """Provide a sharable content based on device"""
    return True

if __name__ == "__main__":
    app.run()    
    