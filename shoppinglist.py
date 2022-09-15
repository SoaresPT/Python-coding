def grocery(items):
    print("Here's your shopping list: ")
    for item in items:
        print(f"- {item}")


shopping_list = ["Fish", "Ice Cream", "Orange"]
grocery(shopping_list)
shopping_list.append("Cinnamon buns")
grocery(shopping_list)
