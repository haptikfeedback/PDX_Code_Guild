# Change Return
# Build an program that will return change in sequential order, largest to smallest denomination
import math

def changereturn(x):
    quarter = 25
    dime = 10
    nickle = 5
    penny = 1
    converter = (dollars_input * 100)

    while True:
        quarter_change = math.ceil(converter // quarter)
        if int(quarter_change % quarter) >= 10:
            dime_change = math.ceil((converter % quarter) // 10)
            if int(dime_change % dime) < 5:
                nickle_change = math.ceil((converter % dime) // 5)
                if int(nickle_change % nickle) < 5:
                    penny_change = math.ceil((converter % nickle) // 1)
                    return "The returned change for ${} is \n\t{} Quarter(s) \n\t{} Dime(s) \n\t{} Nickle(s)" \
                           " \n\t{} Penny(ies)".format(dollars_input, quarter_change, dime_change, nickle_change, penny_change)


dollars_input = float(input("Please enter the amount that you would like to exchange >>: "))
print(changereturn(dollars_input))

