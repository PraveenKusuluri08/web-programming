from flask import Flask,render_template,request,jsonify
from flask_bcrypt import Bcrypt

from mongita import MongitaClientDisk

client=MongitaClientDisk()


quotesDB = client.quotesdb

app = Flask(__name__)
bcrypt = Bcrypt(app)

def encrypt_password(password):
    return bcrypt.generate_password_hash(password, None)


@app.route("/")
def hello():
    print(request.args)
    return render_template("index.html")

@app.route("/form",methods=["POST"])
def form():
    username= request.form.get("username")
    password= request.form.get("password")

    userscollection = quotesDB.users
    
    #password hash
    encrypted_password=encrypt_password(password)
    users =[{
         "username":username,
        "password":encrypted_password
    }]
    userscollection.insert_many(users)
    
    
    
    return "user created"
    
    