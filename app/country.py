#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

def getCountries():
    results = services.allCountries()
    return jsonify(results)