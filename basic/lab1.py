food = input("Enter a food\n ")
name1 = input("What's your name?\n ")
clothing = input("Look at your outfit, what piece is your favorite?\n ")
print("\nLittle " + name1 + " horner, sat in a corner with no " + clothing + ". Eating his " + food + " and whey.\n")
doyoulike = input("Was this funny?\n \n")
if doyoulike == ("yes" or "Yes"):
    print("\nThank you, " + name1 + "\n")
elif doyoulike == ("no" or "No"):
    print("\nI hate you, " + name1 + "\n")
else:
    print("\nThat's not an appropriate answer!")
