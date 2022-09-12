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
