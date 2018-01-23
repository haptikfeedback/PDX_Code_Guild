score = input("Enter your last 5 test scores\n ")

count = 1
num = 5

while (count < 5):
    myscore = int(score)
    scorelist = [myscore]
    if myscore >= 90 and myscore <= 100:
        print("A")
        count = count + 1
        num = num - 1
    elif myscore <= 89 and myscore >=80:
        print("B")
        count = count + 1
        num = num - 1
    elif myscore <= 79 and myscore >=70:
        print("C")
        count = count + 1
        num = num - 1
    elif myscore <= 69 and myscore >=60:
        print("D")
        count = count + 1
        num = num - 1
    elif myscore <= 59 and myscore >0:
        print("F")
        count = count + 1
        num = num - 1
    else:
        myscore <0 or myscore > 100
        print("That is not a valid entry.")
        count = count + 1
        num = num - 1

    scorelist.append(myscore)
    score = input("Enter your last " + str(num) + " test scores\n ")
scoreavg = float(sum(scorelist))/len((str(scorelist)))
print("Thank you... your average grade is " + str(scoreavg))



######
#Working average
print("This program 'is' designed to find the average of n numbers you input\n")
counter = 0
sum_of_numbers = 0
q = '''Would you like to enter %s? Type "yes" if you do, and "no" if you don't. \n'''
qn = 'a number'
while input(q % qn) == "yes" :
    sum_of_numbers += input("Enter your number here:")
    counter += 1
    qn = 'another number after this'

print("Your average is " + str(1.*sum_of_numbers/counter))
