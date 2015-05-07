import connection
from datetime import datetime

def signup(email, password):
    db = connection.get_db()
    users_collection = db.users
    existing_user = users_collection.find_one({"email": email})
    if existing_user.count() > 0:
        return connection.make_response(False, "Email is already taken")
    else:
        user_id = users_collection.insert_one({
                                     "email": email,
                                     "password": password,
                                     "joined": datetime.datetime.utcnow()
                                     })
        return connection.make_response(True, "Welcome to the club!")

def login(email, password):
    db = connection.get_db()
    users_collection = db.users.find_one({
                                          "email": email,
                                          "password": password})
    if users_collection.count() == 1:
        return connection.make_response(True, "Nice to see you again!")
    else:
        return connection.make_response(False, "Sorry buddy. You are not in our system :(")