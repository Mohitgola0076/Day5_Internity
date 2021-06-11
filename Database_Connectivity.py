'''
Data handling is the process of ensuring that research data is stored, 
archived or disposed off in a safe and secure manner during and after the conclusion of a research project.
Proper planning for data handling can also result in efficient and economical storage, retrieval, and disposal of data.
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
