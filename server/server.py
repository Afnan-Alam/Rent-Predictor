from flask import Flask, request, jsonify
import utils
app = Flask(__name__)

# When we have the host link and add /hello it runs the funciton below
@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        "locations" : utils.get_location_names()
    })
    # Allows front-end to access this back-end function
    response.headers.add("access-Control-Allow-Origin", "*")
    return response

@app.route("/api/get_estimated_price", methods=['POST'])
def get_estimated_price():
    location =  request.form["location"]
    typeInput =  request.form["type"]
    beds =  int(request.form["beds"])
    baths =  int(request.form["baths"])
    sq_feet = float( request.form["sq_feet"])
    furnishingb =  int(request.form["furnishingb"])
    smokingb =  int(request.form["smokingb"])
    catsb =  int(request.form["catsb"])
    dogsb =  int(request.form["dogsb"])
    response = jsonify({
        "estimated_price"   :   utils.predict_price(location, typeInput, beds, baths, sq_feet, furnishingb, smokingb, catsb, dogsb)
    })
    response.headers.add("access-Control-Allow-Origin", "*")

    return response

# Equivalent to running the main function basically
if __name__ == "__main__":
    print("Starting Python Flash server for House Rent Predictor")
    utils.load_saved_artifacts()
    print(utils.predict_price("Toronto", "Apartment", 1, 1, 1000, 0, 0, 1, 1))
    print(utils.predict_price("Toronto", "Apartment", 2, 2, 2000, 0, 0, 1, 1))
    print(utils.predict_price("Toronto", "Apartment", 3, 3, 3000, 0, 0, 1, 1))
    app.run(host="127.0.0.1", port=5000)
