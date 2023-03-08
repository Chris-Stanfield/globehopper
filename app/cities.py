from flask import Flask, request, jsonify
import services

def getcitiesci():
    results = services.allcitiesservice()

    data = []
    for row in results:
        data.append({
            "CityId" : row[0],
            "Name": row[1], 
            "CountryId" : row[2], 
            "Capital" : row[3],
            "FirstLandmark" : row[4],
            "SecondLandmark" : row[5],
            "ThirdLandmark" : row[6]
        })

    return jsonify(data)


def createcityci(data):
    services.createcityservice(data)
    return jsonify({"message": "Data inserted successfully"})

def deletecityci(city_id):
    services.deletecityservice(city_id)
    return jsonify({"message": "City successfully deleted"})

def updatecityci(data):
    services.updatecityservice(data)
    return jsonify({"message": "City successfully updated"})
