# Find the index of a given letter in a word/phrase

word = list(input("Enter a word:\n>>>"))
letter = input("What letter are you looking for:\n>>>")

word_index_list = enumerate(word)

for i in range(len(word)):
    if letter == word[i]:
        print(word[i] + " " + str(i))
        # print(i)
    elif letter != word[i]:
        print("-1")

# print()
