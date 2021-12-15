#Project
Implementing ACID properties using CRUD Operations

import psycopg2

from tabulate import tabulate

con = psycopg2.connect( host="localhost", database="postgres", user="postgres", password="Unitedstates@123")

#For isolation: SERIALIZABLE
con.set_isolation_level(3)

