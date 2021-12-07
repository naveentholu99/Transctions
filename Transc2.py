import psycopg2
from tabulate import tabulate
conn = psycopg2.connect(database="postgres", user="postgres", password="Unitedstates@123", host="127.0.0.1", port="5432")

#For isolation: SERIALIZABLE
conn.set_isolation_level(3)
#For atomicity
conn.autocommit = False
#The depot d1 is deleted from Depot and Stock
try:

    cur = conn.cursor()

    cur.execute("DELETE from DEPOT where DEP='D1';")
    conn.commit()
    print("Total number of rows deleted :", cur.rowcount)

    cur.execute("SELECT DEP, ADDR, VOLUME  from DEPOT")
    rows = cur.fetchall()
    for row in rows:
        print("DEP = ", row[0])
        print("ADDR = ", row[1])
        print("VOLUME = ", row[2], "\n")

    cur.execute("SELECT PROD, DEP, QUANTITY  from STOCK")
    rows = cur.fetchall()
    for row in rows:
        print("PROD = ", row[0])
        print("DEP = ", row[1])
        print("QUANTITY = ", row[2], "\n")

    print("Operation done successfully")


except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    conn.rollback()
finally:
    if conn:
        conn.commit()
        cur.close
        conn.close
        print("PostgreSQL connection is now closed")
