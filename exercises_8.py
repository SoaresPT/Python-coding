import mariadb
import sys
from geopy.distance import geodesic as GD

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
cur.execute("SELECT name, municipality FROM airport WHERE ident= ?", (icao,))
row = cur.fetchall()
if len(row) == 0:
    print("There are no results for this query\n")
else:
    for name, municipality in row:
        print(f"Airport: {name}\nLocation: {municipality}\n")
# 8.2

area_code = input("Type a area code: ")
if area_code != "":
    area_query = f"SELECT * FROM airport WHERE iso_region LIKE '{area_code}%' ORDER BY type"
    cur.execute(area_query)
    row = cur.fetchall()
    if len(row) == 0:
        print("There are no results for this query\n")
    else:
        for data in row:
            print(data)
        print("\n")  # Just an empty line to make it look prettier in the output when running the whole script :)
else:
    print("No area code was typed.\n")

# 8.3
while True:
    icao1 = input("Type the ICAO code of the 1st airport: ")
    icao1_query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}'"
    cur.execute(icao1_query)
    icao1_rows = cur.fetchall()
    if len(icao1_rows) == 0:
        print("Couldn't find that airport. Try again.")
        continue
    else:
        coordinate1 = icao1_rows[0]
        break

while True:
    icao2 = input("Type the ICAO code of the 2nd airport: ")
    icao2_query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}'"
    cur.execute(icao2_query)
    icao2_rows = cur.fetchall()
    if len(icao2_rows) == 0:
        print("Couldn't find that airport. Try again.")
        continue
    else:
        coordinate2 = icao2_rows[0]
        break
print(f"The distance between both airports {icao1.upper()} and {icao2.upper()} is: {GD(coordinate1, coordinate2).km} Km.")

# Close the db connection
conn.close()
