# LAB: ROT CIPHER
import string

supersecret = input("Do you need to encrypt or decrypt your message?: ".lower())
word = input("ENTER YOUR MESSAGE BELOW?\n::")

print(string.ascii_lowercase)
print(string.ascii_uppercase[13:] + string.ascii_lowercase[:13])
translator = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[13:] + string.ascii_lowercase[:13])

if supersecret == 'encrypt':
    new_word = word.translate(translator)
    print(new_word)

elif supersecret == 'decrypt':
    new_word = word.translate(translator)
    print(new_word)