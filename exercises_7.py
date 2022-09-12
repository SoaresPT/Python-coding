# 7.1
seasons = ("spring", "summer", "autumn", "winter")
#month = int(input("Type the number of a month: "))
month = 6
if month in (1,2,12):
    print(seasons[3])
elif month in (3,4,5):
    print(seasons[0])
elif month in (6,7,8):
    print(seasons[1])    
elif month in (9,10,11):
    print(seasons[2])
### or ####
seasons_dct = {
  "spring": [3,4,5],
  "summer": [6,7,8],
  "autumn": [9,10,11],
  "winter": [12,1,2]
}
print("-----------------------")
month = 1
for key, value in seasons_dct.items():
    print(key, value)

# 7.2

name_set = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    else:
        if name in name_set:
            print("Existing name")
        else:
            print("New name")
            name_set.add(name)
print("Empty Line Detected. Exiting...")
print("List of names:")
for name in name_set:
    print(name)

icao_dt = {
    "00AK":  "Lowell Field",
    "00AL":  "Epps Airpark",
    "00AZ":  "Cordes Airport",
    "00CA":  "Goldstone \/Gts\/ Airport",
    "00CO":  "Cass Field",
    "00FA":  "Grass Patch Airport",
    "00FL":  "River Oak Airport",
    "00GA":  "Lt World Airport",
    "00ID":  "Delta Shores Airport",
    "00IL":  "Hammer Airport",
    "00IS":  "Hayenga's Cant Find Farms Airport",
    "00KS":  "Hayden Farm Airport",
    "00KY":  "Robbins Roost Airport",
    "00LS":  "Lejeune Airport",
    "00MD":  "Slater Field",
    "00MN":  "Battle Lake Municipal Airport",
    "00MO":  "Cooper Flying Service Airport",
    "00MT":  "Sands Ranch Airport",
    "00NC":  "North Raleigh Airport",
    "00NY":  "Weiss Airfield",
    "00OH":  "Exit 3 Airport",
    "00PN":  "Ferrell Field",
    "00PS":  "Thomas Field",
    "00SC":  "Flying O Airport",
    "00TN":  "Ragsdale Road Airport",
    "00TS":  "Alpine Range Airport",
    "00VA":  "Vaughan Airport",
    "00VI":  "Groundhog Mountain Airport",
    "00WA":  "Howell Airport",
    "00WI":  "Northern Lite Airport",
    "00WN":  "Hawks Run Airport",
    "00WV":  "Lazy J. Aerodrome",
    "00XS":  "L P Askew Farms Airport",
    "01AL":  "Ware Island Airport",
    "01CL":  "Swansboro Country Airport",
    "01FA":  "Rybolt Ranch Airport",
    "01FL":  "Cedar Knoll Flying Ranch Airport",
    "01GE":  "The Farm Airport",
    "01IA":  "Stender Airport"
}

def options():
    print("Pick an option:")
    print("\t[1] Create new airport")
    print("\t[2] Find information of an existing airport")
    print("\t[3] Exit\n")

while True:
    options()
    choice = int(input("Type an option: "))
    if choice == 3:
        print("Quitting...")
        break
    elif choice == 1:
        new_icao = input("Type the new icao code: ").upper()
        new_airport = input("Type the new airport name: ")
        # Should check for existing ICAO? -- Ask teacher on class
        icao_dt[new_icao] = new_airport
    elif choice == 2:
        icao = input("Type the ICAO code: ")
        print(f"{icao_dt.get(icao.upper(), 'Airport not found on the database.')}{chr(10)}")
    else:
        print("That's not a valid option. Try again...")   
