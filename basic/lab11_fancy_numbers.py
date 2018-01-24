#Generates a formatted number based on user input

user_num = input("\nLet me convert your phone numbers for you!\nPlease enter a phone number (only numerical values: ")
print(user_num)
print("({}) {}-{}".format(user_num[0:3],(user_num[3:6]),(user_num[6:10]))) #prints a range of numbers
