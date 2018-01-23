penny = 1
nickel = 5
dime = 10
quarter = 25

i = input("Please enter an amount no more than 1 dollar(in cents): ")
i = int(i)

if i > 100:
    print ("Please enter an amount equal or less than 100. ")
elif i >= quarter:
    quarter_n = i % quarter
    i = i - quarter * quarter_n
    if i >= dime:
        dime_n = i % dime
        i = i - dime * dime_n
        if i >= nickel:
            nickel_n = i % nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i % penny
                print (quarter_n,"quarters,",dime_n,"dimes",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i % penny
                print (quarter_n,"quarters,",dime_n,"dimes",penny_n,"pennies")
    else:
        if i >= nickel:
            nickel_n = i % nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i % penny
                print (quarter_n,"quarters,",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i % penny
                print (quarter_n,"quarters,",penny_n,"pennies")
else:
    if i >= dime:
        dime_n = i % dime
        i = i - dime * dime_n
        if i >= nickel:
            nickel_n = i % nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i % penny
                print (dime_n,"dimes",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i % penny
                print (dime_n,"dimes",penny_n,"pennies")
    else:
        if i >= nickel:
            nickel_n = i % nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i % penny
                print (nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i % penny
                print (penny_n,"pennies")