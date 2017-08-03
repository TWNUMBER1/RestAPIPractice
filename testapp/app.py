from flask import Flask
from yelpUtil import yelp
app = Flask(__name__)

@app.route("/")
def hello():
    return yelp.getNearbyList()
    #return "Hello from app!\n"

@app.route("/nearbylist", methods=['GET'])
def getNearbyList():
    # GET yelp restaurant list
    return "Not implemented yet\n"

@app.route("/mylist", methods=['GET'])
def getMyList():
    # Get user favorite list
    return "Not implemented yet\n"

@app.route("/store/<string:restaurant>", methods=['POST'])
def storeRestaurant(restaurant):
    # Store user favorite restaurant
    return "Not implemented yet\n"

if __name__ == "__main__":
    app.run()
