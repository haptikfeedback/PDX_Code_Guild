import random
count = 0
eye = ["0 0", "0 -", "- 0", "^ ^", "- ^", "- -"]
nose = [" 4", " d", " D", " @", " v", " c", " C"]
mouth = ["\_/", "u-u", "___", "q_p", "___", "*_*"]
while (count < 6):
    print("\n")
    print(random.choice(eye))
    print(random.choice(nose))
    print(random.choice(mouth))
    print("\n")
    count = count + 1

print("Are you not entertained!?")
