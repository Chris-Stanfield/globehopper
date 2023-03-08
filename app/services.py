#Define all services for Country and City
from flask import Flask, request, jsonify
import conn




#Gets all records from Country table using SQL
def allcountries():

    #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #Close Connection
    mycursor.close()
    conn.myconn.close()
    return results


def createcountry(data):
     #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryId = data["CountryId"]
    name = data["Name"]
    population = data["Population"]
    continent = data["Continent"]

    #Execute the SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values = (countryId, name, population, continent)
    mycursor.execute(mysql, values)


    #Close Connection
    mycursor.close()
    conn.myconn.close()