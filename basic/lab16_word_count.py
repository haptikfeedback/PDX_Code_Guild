# count-list-items-1.py
import string

frequency = {}

with open('dracula.txt', 'r') as wordstring:
# wordstring = 'I like, to "pet" puppies I also like to pet kittens!'.lower()
    punct = set(string.punctuation)
    sans_punct = ''.join(x for x in wordstring if x not in punct).split(' ')
    wordfreq = [sans_punct.count(w) for w in sans_punct]

for word in sans_punct:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()


# print("String\n" + wordstring + "\n")
print("List\n" + str(sans_punct) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(sans_punct, wordfreq))) + "\n")
print(sans_punct)

