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


def allcities():

    #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM city")
    results = mycursor.fetchall()

    #Close Connection
    mycursor.close()
    conn.myconn.close()
    return results


def createcountry(data):
     #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid = data["CountryId"]
    name = data["Name"]
    population = data["Population"]
    continent = data["Continent"]

    #Execute the SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values = (countryid, name, population, continent)
    mycursor.execute(mysql, values)


    #Close Connection
    mycursor.close()
    conn.myconn.close()

def createcity(data):
     #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    captial = data["Capital"]
    cityid = data["CityId"]
    countryid = data["CountryId"]
    firstlandmark = data["FirstLandmark"]
    name = data["Name"]
    secondlandmark = data["SecondLandmark"]
    thirdlandmark = data["ThirdLandmark"]


    #Execute the SQL
    mysql = "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (cityid, name, countryid, captial, firstlandmark, secondlandmark, thirdlandmark)
    mycursor.execute(mysql, values)


    #Close Connection
    mycursor.close()
    conn.myconn.close()


def deletecountry(country_id):
     #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()


    #Execute the SQL
    mysql = "DELETE FROM Country WHERE CountryId = %s"
    value = (country_id)
    mycursor.execute(mysql % value)


    #Close Connection
    mycursor.close()
    conn.myconn.close()