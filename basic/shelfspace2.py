bottle_type = input("What type of bottle is this?\n:")
bottle_dict = {'wine': 3, 'coke': 1, 'water': 2}

bottle_size = bottle_dict[bottle_type]
shelf_width = int(input("How wide is the shelf?\n:"))
shelf_length = int(input("How long is the shelf?\n:"))
wine_group_length = shelf_length // bottle_size
wine_group_width = shelf_width // bottle_size

print("You can fit " + str(wine_group_length * wine_group_width) + " bottles of " + bottle_type + ".")