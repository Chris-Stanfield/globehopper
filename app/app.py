#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
import cities


#Using Flask framework
app = Flask(__name__)


#Read - GET API 
@app.get("/countries")
def getallcountriesapp():
    return country.getcountriesco()

#Read - GET API 
@app.get("/countries/<string:country_name>")
def getcountriesbyconapp(country_name):
    return country.getcountrybyconco(country_name)

#Read - GET API 
@app.get("/cities")
def getallcitiesapp():
    return cities.getcitiesci()

#Create - POST API 
@app.post("/countries")
def createcountryapp():
    data = request.json
    return country.createcountryco(data)

#Create - POST API
@app.post("/cities")
def createcityapp():
    data = request.json
    return cities.createcityci(data)

#Delete - DELETE API 
@app.delete("/countries/<int:country_id>")
def deletecountryapp(country_id):
    return country.deletecountryco(country_id)

#Delete - DELETE API 
@app.delete("/cities/<int:city_id>")
def deletecityapp(city_id):
    return cities.deletecityci(city_id)


#Update - PUT API 
@app.put("/countries")
def updatecountryapp():
    data = request.json
    return country.updatecountryco(data)

#Update - PUT API 
@app.put("/cities")
def updatecityapp():
    data = request.json
    return cities.updatecityci(data)




#Execute on the terminal 
if __name__ == "__main__":
    app.run(debug=True)