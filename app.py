from flask import Flask, request, jsonify
import json

""" Database structure
{
  "users":[
    {
      "email": "tejas@abc",
      "password": "123",
      "firstname": "tejas",
      "lastname": "gujjar"
    }
  ]
}
"""

app = Flask(__name__)
DATABASE_PATH = "database.json"

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/users', methods=['GET'])
def getUsers():
    users = _getUsers()
    return users

@app.route('/users', methods=['POST'])
def createUser():
    if not request.data:
        return "Invalid payload", 404

    body = json.loads(request.data)
    if 'email' not in body:
        return "Missing email", 404
    if 'password' not in body:
        return "Missing password", 404
    if 'firstname' not in body:
        return "Missing firsname", 404
    if 'lastname' not in body:
        return "Missing lastname", 404

    if _doesEmailExist(body['email']):
        return "Email exists", 404

    f = open(DATABASE_PATH)
    data = json.load(f)
    f.close()
    data['users'].append({
        "email": body['email'],
        "password": body['password'],
        "firstname": body['firstname'],
        "lastname": body['lastname']
    })
    json_object = json.dumps(data, indent=2)
    with open(DATABASE_PATH, "w") as outfile:
        outfile.write(json_object)

    return "Success", 201

@app.route('/users/<email>', methods=['PUT'])
def updateUser(email):
    if not request.data:
        return "Invalid payload", 404

    if not email:
        return "Invalid email", 404

    body = json.loads(request.data)
    if 'email' in body:
        return "Unexpected email parameter in payload", 404

    if not _doesEmailExist(email):
        return "User does not exist", 404

    f = open(DATABASE_PATH)
    data = json.load(f)
    f.close()
    for user in data['users']:
        if user['email'] == email:
            user['password'] = body['password']
            user['firstname'] = body['firstname']
            user['lastname'] = body['lastname']

    json_object = json.dumps(data, indent=2)
    with open(DATABASE_PATH, "w") as outfile:
        outfile.write(json_object)

    return "Success", 201

@app.route('/users/<email>', methods=['DELETE'])
def deleteUser(email):
    if request.data:
        return "Invalid payload", 404

    if not _doesEmailExist(email):
        return "User does not exist", 404
    f = open(DATABASE_PATH)
    data = json.load(f)
    f.close()
    for user in data['users']:
        if user['email'] == email:
            data['users'].remove(user)
            break

    json_object = json.dumps(data, indent=2)
    with open(DATABASE_PATH, "w") as outfile:
        outfile.write(json_object)
    return "Success", 201

@app.route('/reset', methods=['POST'])
def resetApp():
    data = {
        "users":[
            {
            "email": "tejas@abc",
            "password": "123",
            "firstname": "tejas",
            "lastname": "gujjar"
            }
        ]
    }
    json_object = json.dumps(data, indent=2)
    with open(DATABASE_PATH, "w") as outfile:
        outfile.write(json_object)
    return "Success", 200

def _getUsers():
    f = open(DATABASE_PATH)

    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()
    return data['users']

def _doesEmailExist(email):
    users = _getUsers()
    for user in users:
        if user['email'] == email:
            return True
    return False
