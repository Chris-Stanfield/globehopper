#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Read - GET API 
@app.get("/countries")
def getAllCountries():
    return country.getCountries()

#Create - POST API 
@app.post("/countries")
def createCountry():
    data = request.json
    return country.createCountry(data)



#Execute on the terminal 
if __name__ == "__main__":
    app.run(debug=True)