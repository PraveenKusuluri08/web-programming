from flask import Flask,render_template,request,session,render_template_string
from flask_bcrypt import Bcrypt

from pymongo import MongoClient

client=MongoClient("127.0.0.1",27017)

quotesDB = client.quotesdb

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key="QUOTES_APPLICATION"

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
    
    count=userscollection.count_documents({"username":username})
    if count>0:
        return render_template("quote.html",error=f"{username} already in use")
    #password hash
    encrypted_password=encrypt_password(password)
    users =[{
         "username":username,
        "password":encrypted_password
    }]
    if request.method=="POST":
        session["logged_in"]=True
        
    userscollection.insert_many(users)
    
    return render_template("quote.html",error=None,loginSession = session["logged_in"],userData={"username":username}) 

@app.route("/logout")
def logout():
    return render_template("index.html")

@app.route("/createQuote",methods=["POST"])
def createQuote():
    quoteAuthor = request.form["author"]
    quote = request.form["quote"]
    
    print(quoteAuthor)
    print(quote)
    
    # quotesCollection = quotesDB.quotesCollection
    
    # quotesCollection.insert_many([{"quote":quote,"author":quoteAuthor}])
    
    return "Quote Added successfully"
    
    

    
    