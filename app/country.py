#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

def getcountriesco():
    results = services.allcountriesservice()

    data = []
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name": row[1], 
            "Population" : row[2], 
            "Continent" : row[3]
        })

    return jsonify(data)


def createcountryco(data):
    services.createcountryservice(data)
    return jsonify({"message": "Data inserted successfully"})


def deletecountryco(country_id):
    services.deletecountryservice(country_id)
    return jsonify({"message": "Country successfully deleted"})


def updatecountryco(data):
    services.updatecountryservice(data)
    return jsonify({"message": "Country successfully updated"})