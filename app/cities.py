from flask import Flask, request, jsonify
import services

def getcities():
    results = services.allcities()

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


def createcity(data):
    services.createcity(data)
    return jsonify({"message": "Data inserted successfully"})

def deletecity(city_id):
    services.deletecity(city_id)
    return jsonify({"message": "City successfully deleted"})
