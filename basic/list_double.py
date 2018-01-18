# multiplication tool

def mult(my_list, n):
    my_new_list = [i * n for i in my_list]
    return my_new_list

# mylist = input("Enter your numbers: ")

# for i in mylist:
#     my_list = list(mylist)

# print(mylist)
# print(my_list)

my_list = [1, 2, 3, 4, 5, 6]

n = int(input("enter a multiplier: "))

print(mult(my_list, n))
