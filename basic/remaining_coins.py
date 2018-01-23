import math

quarter = 25
dime = 10
nickle = 5
penny = 1

continue_change = True

dollars_input = input("\n\nHow many dollars do you want change for?\n:")

while continue_change == True:
    dollar_change = float(dollars_input) * 100
    quarter_change = int(dollar_change) // quarter

    if int(quarter_change % quarter) <= 10:
        dime_change = math.ceil((dollar_change % quarter) // 10)
        

        if int(dime_change % dime) < 5:
            nickle_change = math.ceil((quarter_change % dime) // 5)


    print(quarter_change)
    print(dime_change)
    print(nickle_change)
    continue_change = False

