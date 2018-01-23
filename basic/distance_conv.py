distance = input("Enter your distance\n:")
input_unit = input("Enter your measurement\n:")
output_unit = input("You'd like to conver to?\n:")

meter_conversion_dict = {"inch": 39.3701, "foot": 3.28084, "yard": 1.09361, "mile": 0.000621371}

def convert_units(distance, input_unit, output_unit):
    meters = int(distance) / meter_conversion_dict[input_unit]
    return meters * meter_conversion_dict[output_unit]

print(str(distance) + " " + input_unit + " is " + str(convert_units(distance, input_unit, output_unit)) + " " + output_unit)