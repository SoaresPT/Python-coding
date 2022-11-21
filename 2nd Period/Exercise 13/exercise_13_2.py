from flask import Flask
from csv import reader, DictReader

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/')
def index():
    return f'This is a placeholder text for the Exercise 13.2. The correct path to check for airport info as per exercise instructions is at the <a href="/airport/">airport</a> page'

@app.route('/airport/')
def prime():
    return f'Pass a number to the url after prime_number/ to do the tests.'

@app.route('/airport/<ICAO>', methods=['GET'])
def airport_info(ICAO):
    with open("airports.csv", "r") as airports_file:
        csv_reader = DictReader(airports_file)
        for row in csv_reader:
            if ICAO.upper() == row['ident'].upper():
                return {"ICAO": row['ident'], "Name": row['name'], "Location": row['iso_country']}

"""
@app.route('/airport/<ICAO>', methods=['GET'])
def airport_info(ICAO):
    with open("airports.csv", "r") as airports_file:
        csv_reader = reader(airports_file)
        for row in csv_reader:
            if ICAO.upper() == row[1].upper():
                return {"ICAO": row[1], "Name": row[3], "Location": row[8]}
"""
"""
@app.route('/airport/<ICAO>', methods=['GET'])
def airport_info(ICAO):
    with open("airports.csv", "r") as airports_file:
        csv_reader = csv.reader(airports_file, delimiter=',')
        for row in csv_reader:
            i = 1
            if ICAO.upper() == row[i].upper():
                return {"ICAO": row[1], "Name": row[3], "Location": row[8], "I": i}
                #return str(row)
            else:
                i+= 1
        return "Not found"
"""    
app.debug = True        
app.run(host='0.0.0.0', port=5000)