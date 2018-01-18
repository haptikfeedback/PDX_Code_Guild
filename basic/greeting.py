
print("Hi, It's nice to meet you. My name is Sere.")
name = input("What's your name?: ")
print("*" * len(name))
born = input("Nice to meet you {}, when were you born?: ".format(name))
age = (2017 - int(born))
print("If I'm correct, you're {} years old.".format(age))