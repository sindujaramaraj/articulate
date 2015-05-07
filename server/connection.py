from pymongo import MongoClient

client = MongoClient()
db = client.articulate

def get_db():
    return db

def make_response(is_success, message):
    return {
            "status": "success" if is_success else "failure",
            "message": message
            }