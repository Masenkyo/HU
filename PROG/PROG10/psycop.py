import psycopg2

connectionString = "host='localhost' dbname='fabriek' user='postgres' password=''"

conn = psycopg2.connect(connectionString)
cursor = conn.cursor()

query = """SELECT klantnr, plaats, adres
           FROM   klant
           WHERE  plaats = 'Amersfoort';"""

cursor.execute(query)
records = cursor.fetchall()

conn.commit()
conn.close()

for record in records:
    print(record[0])