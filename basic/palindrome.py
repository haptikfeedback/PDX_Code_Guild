#Palindrome Option BEST

def palindrome():
    convert = phrase.replace(" ", "")
    joined_convert = ''.join(reversed(convert))
    return convert == joined_convert

phrase = input("I can tell if what you typed is a Palindrome.\nPlease make an entry: ")
print(palindrome())

#Palindrome Option 2
# def find_palindrome(w):
#     return w.replace(' ', '').lower() == ''.join(reversed(w.replace(' ','').lower()))

# work = input("What word would you like to check?: ")
# print(find_palindrome(word))