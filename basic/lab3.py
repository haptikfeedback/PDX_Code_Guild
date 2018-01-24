miles = input("Enter the number of miles to convert: ")
#meter_dict = {"inch": 39.3701, "foot": 3.28084, "yard": 1.09361, "mile": 0.000621371}
#inch_in_mile = 63360
feet_in_mile = 5280
inch_convert = (str((miles) * (feet_in_mile)))

print("There are {} inches in {} mile(s)".format(inch_convert, miles))