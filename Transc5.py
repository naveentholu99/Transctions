import psycopg2
from tabulate import tabulate
conn = psycopg2.connect(database="postgres", user="postgres", password="Unitedstates@123", host="127.0.0.1", port="5432")

#For isolation: SERIALIZABLE
conn.set_isolation_level(3)
#For atomicity
conn.autocommit = False

try:
    cur = conn.cursor()
    cur = conn.cursor()

    cur.execute("INSERT INTO PRODUCT (PROD,PNAME,PRICE) \
          VALUES ('P100', 'CD', 5 )");

    cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
          VALUES('P100', 'D2', 50 )");

    conn.commit()
    print("Records created successfully")

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