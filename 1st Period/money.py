#name = input("What is your name?")
#print(f"Hello {name}")
group = int(input("How many persons are in your group? "))
print(f"So there are {group} persons in your group")
amount = float(input("How much money do you have? "))
currency = input("What's your currency? (£ / € / $) ")
print(f"So you're splitting {amount}{currency} with {group} persons")
print(f"This will mean each person will get {amount/group}{currency} each")

