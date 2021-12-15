#Project
This project illustrates how to execute database transctions using python and postgres by implementing ACID properties on already existed tables in the database 


 
 import psycopg2

from tabulate import tabulate

con = psycopg2.connect( host="localhost", database="postgres", user="postgres", password="Unitedstates@123")

#For isolation: SERIALIZABLE
con.set_isolation_level(3)

