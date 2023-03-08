#Define all services for Country and City
from flask import Flask, request, jsonify
import conn




#Gets all records from Country table using SQL
def allcountriesservice():

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


def getcountrybyconservice(country_name):

    #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = "SELECT * FROM Country WHERE Continent = '%s'"
    value = country_name
    mycursor.execute(mysql % value)
    results = mycursor.fetchall()

    #Close Connection
    mycursor.close()
    conn.myconn.close()
    return results


def allcitiesservice():

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


def createcountryservice(data):
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


def updatecountryservice(data):
    #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid = data["CountryId"]
    name = data["Name"]
    population = data["Population"]
    continent = data["Continent"]

    #Execute the SQL
    mysql = "UPDATE Country SET Name = %s, Population = %s, Continent = %s WHERE CountryId = %s"
    values = (name, population, continent, countryid)
    mycursor.execute(mysql, values)


    #Close Connection
    mycursor.close()
    conn.myconn.close()


def updatecityservice(data):
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
    mysql = "UPDATE City SET Name = %s, CountryId = %s, Capital = %s, FirstLandmark = %s, SecondLandmark = %s, ThirdLandmark = %s  WHERE CityId = %s"
    values = (name, countryid, captial, firstlandmark, secondlandmark, thirdlandmark, cityid)
    mycursor.execute(mysql, values)


    #Close Connection
    mycursor.close()
    conn.myconn.close()





def createcityservice(data):
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


def deletecountryservice(country_id):
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


def deletecityservice(city_id):
     #Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()


    #Execute the SQL
    mysql = "DELETE FROM City WHERE CityId = %s"
    value = (city_id)
    mycursor.execute(mysql % value)


    #Close Connection
    mycursor.close()
    conn.myconn.close()