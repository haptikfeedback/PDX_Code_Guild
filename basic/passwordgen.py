#Password Generator

import random
import string

character_list = string.digits + string.ascii_letters + string.punctuation
password = ""

password_length = int(input("\n\nSecurity is 'Safety'.\nHow long should your password be?\n:"))
for i in range(0, password_length):
    password = password + random.choice(character_list)
print("\n\n" + password)
