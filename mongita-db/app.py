from flask import Flask,render_template,send_from_directory, request,jsonify
import os
import json
from mongita import MongitaClientDisk

client=MongitaClientDisk()

moviesDb = client.moviesdb

path = os.path.join(os.path.dirname(__file__), 'templates')
    
print(path)
app =Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route("/movies")
def movies():
    return render_template("index.html")

@app.route("/test-movies")
def moviesData():
    return json.loads(open('movies.json').read())

@app.route("/<path:path>")
def staticFile(path):
    print(path)
    return send_from_directory('templates', path)


# @app.route("/findMovies")
# def findMovies():

#     new_collection = moviedb.mongoose_collection

#     data= list(new_collection.find({"title":"Blade Runner"}))
#     print(data)
#     return jsonify({"data":data})
