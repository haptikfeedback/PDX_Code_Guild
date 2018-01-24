print("******************************************")
print("* Hello, I am your personal assistantant *")
print("******************************************")
current_time = input("\nWhat is the current time?: ")
current_time_split = current_time.split(' ')
timeofday = current_time_split.pop()
hour = int(current_time_split.pop(0))

if timeofday.lower() == 'am':
    if hour >= 7 and hour <= 9:
        print("It is currently time for you to eat BREAKFAST.")
    elif hour == 12:
        print("It's HAMMER time!")
    elif hour <= 4:
        print("It's HAMMER time!")
    else:
        print("You are free at this time")

if timeofday.lower() == 'pm':
    if hour == 12:
        print("It's LUNCH time")
    elif hour <= 2:
        print("It's LUNCH time!")
    elif hour >= 7 and hour <= 9:
        print("It's DINNER time.")
    else:
        print("You should be sleeping.")
