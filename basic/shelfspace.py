#How much wine fits on a shelf

wine_size = 3

shelf_length = input("\n\nHow wide is your shelf?\n:")
shelf_long = input("\nHow long is your shelf?\n:")
bottles_in_shelf = ((int(shelf_length) * int(shelf_long)) // wine_size)

print("\n\nYou can fit " + str(bottles_in_shelf) + " bottles in your shelf.")