import pymongo
import scrape_mars
from flask import Flask, render_template, redirect

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.marsDB
collection = db.mars_data


@app.route('/')
def index():
    marsdata = (db.mars_data.find_one())
    return render_template('index.html', marsdata=marsdata)

@app.route('/scrape')
def scrape():
    marsdata = db.mars_data
    mars = scrape_mars.scrape()
    db.mars_data.update({}, mars, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)