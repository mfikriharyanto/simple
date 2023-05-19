import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask

app = Flask(__name__)

cred = credentials.Certificate('service_account.json')
firebase = firebase_admin.initialize_app(cred)

@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.route("/user/<string:id>")
def user_info(id):
    try:
        user = auth.get_user(id)
        return {"data": {"email": user.email}}, 200
    except:
        return {"message": "User not found!"}
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)