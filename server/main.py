from flask import Flask
import authenticate

app = Flask(__name__)

@app.route("/login")
def login():
    authenticate.login()

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
    