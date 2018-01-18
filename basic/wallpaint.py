paint_gallon = 400 #square feet
price_gallon = 5
wall_width = int(input("What is the WIDTH of your wall?: "))
wall_height = int(input("What is the HEIGHT of your wall?: "))
wall_coats = int(input("How many coats of paint do you intend to apply?: "))
wall_total = int(input("How many walls are you painting?: "))
wall_dimensions = (wall_coats*(wall_width*wall_height))
wall_total_dimensions = (wall_dimensions * wall_total)
gallons = (wall_total_dimensions / paint_gallon)
totalprice_gallon = (gallons * price_gallon)

print(wall_dimensions)
print(wall_total_dimensions)
print(gallons)
print("You will need {} gallons of paint at an estimated cost of ${}.".format(gallons, totalprice_gallon))
