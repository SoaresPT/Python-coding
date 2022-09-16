import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="soares",
        host="127.0.0.1",
        port=3306,
        database="flight_game"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# 8.1
icao = input("Type a ICAO code: ")
cur.execute("SELECT name, municipality FROM airport WHERE ident= ?",(icao,))

for name, municipality in cur:
    print(f"Airport: {name}\nLocation: {municipality}\n")

# 8.2

area_code = input("Type a area code: ")
area_query = f"SELECT * FROM airport WHERE iso_region LIKE '{area_code}%' ORDER BY type"
print(area_query)
cur.execute(area_query)
for row in cur:
    print(row)

# Close the db connection
conn.close()