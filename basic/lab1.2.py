import random
print("When multiple responses are requested, separate with a 'comma'\n")
gender = input("Enter in a gender: ")
adjective = input("Enter an adjective: ")
mood = input("Now enter a mood: ")
#name = input("what's your name?: ")
animal = input("What is your favorite type of animal?: ")
mood_list = []
adjective_list = []
adjective_list.append(adjective_list)
mood_list.append(mood)
random_adjective_list = random.choice(adjective_list)
random_mood_list = random.choice(mood_list)

print(("{}, looking for a companion. Must be {} and {}. It's important to know that I'm afraid of a{}.").format(gender, mood, adjective, animal))
