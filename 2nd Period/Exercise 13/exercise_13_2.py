from flask import Flask
import mysql.connector


connection = mysql.connector.connect(
    #change these to match your info
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    password="ChangeToYourRootPassword!!"
)
cursor = connection.cursor()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/')
def index():
    return f'This is a placeholder text for the Exercise 13.2. The correct path to check for airport info as per exercise instructions is at the <a href="/airport/">airport</a> page'

@app.route('/airport/')
def prime():
    return f'Pass a number to the url after airport/ to do the tests.'

@app.route('/airport/<ICAO>', methods=['GET'])
def airport_info(ICAO):
    sql = f'SELECT ident, NAME, municipality from airport WHERE ident = "{ICAO}"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if(len(results) == 0):
        return {"ICAO": ICAO, "Name": "Not found", "Municipality": "Not found"}
    return {"ICAO": results[0][0], "Name": results[0][1], "Municipality": results[0][2]}

app.run(host='0.0.0.0', port=5000)