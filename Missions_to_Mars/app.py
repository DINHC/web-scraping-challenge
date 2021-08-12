
import scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import pymongo
# from app import app 

app = Flask(__name__)

# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# db = client.marsDB
# collection = db.martian
mongo = PyMongo(app, uri="mongodb://localhost:27017/MARSSTUFF")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/MARSSTUFF"
# mongo = PyMongo(app)


@app.route('/')
def index():
    marsdata = (mongo.db.martian.find_one())
    return render_template('index.html', marsdata=marsdata)

@app.route('/scrape')
def scrape():
    marsdata = mongo.db.martian
    mars = scrape_mars.scrape2()
    mongo.db.martian.update({}, mars, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)