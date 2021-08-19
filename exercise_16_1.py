foods = {'ian': 'pizza', 'michelle': 'pasta', 'janet': 'salad'}

for name, food in foods.items():
    # use this method with older versions of python3
    print("{}'s favorite food is {}".format(name, food))

    # use this with python 3.6 or later
    print(f"{name}'s favorite food is {food}")
