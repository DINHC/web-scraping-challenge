
from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import pymongo
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.marsDB
collection = db.martian
# app.config["MONGO_URI"] = "mongodb://localhost:27017/"
# mongo = PyMongo(app)

print("Connection Successful")
client.close()