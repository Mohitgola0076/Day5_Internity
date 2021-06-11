'''
A Database connection is a facility in computer science that allows client software to talk to database server software,
whether on the same machine or not. A connection is required to send commands and receive answers, 
usually in the form of a result set. Connections are a key concept in data-centric programming.
'''
 
# Creating a Database

create a database named "mydatabase":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# Creating the connection

import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google")  
  
#printing the connection object   
print(myconn)  


# Creating a cursor object

import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google", database = "mydb")  
  
#printing the connection object   
print(myconn)   
  
#creating the cursor object  
cur = myconn.cursor()  
  
print(cur)  


# Check if Database Exists

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
