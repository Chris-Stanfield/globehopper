#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
import cities


#Using Flask framework
app = Flask(__name__)


#Read - GET API 
@app.get("/countries")
def getallcountries():
    return country.getcountries()

@app.get("/cities")
def getallcities():
    return cities.getcities()

#Create - POST API 
@app.post("/countries")
def createcountry():
    data = request.json
    return country.createcountry(data)

@app.post("/cities")
def createcity():
    data = request.json
    return cities.createcity(data)

#Delete - DELETE API 
@app.delete("/countries/<int:country_id>")
def deletecountry(country_id):
    return country.deletecountry(country_id)

@app.delete("/cities/<int:city_id>")
def deletecity(city_id):
    return cities.deletecity(city_id)




#Execute on the terminal 
if __name__ == "__main__":
    app.run(debug=True)