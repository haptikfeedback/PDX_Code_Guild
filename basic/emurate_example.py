phrase = ['the', 'cat', 'in', 'the', 'hat']

word = 'the'

phrase_index_list = enumerate(phrase)

# another_things = list(phrase_index_list)
# print(another_things)

for i in phrase_index_list:
    if i[1] == word:
        print(i[0])
        print(i[1])

print()
for i in range(len(phrase)):
    if word == phrase[i]:
        print(phrase[i])
        print(i)

print()
i = 0
while i < len(phrase):
    if word == phrase[i]:
        print(phrase[i])
        print(i)
        i += 1
        
# for i in range(len(phrase)):
#     if word == phrase[i]:
#         print(phrase[i])
#         print(i)
#
# i = 0
# while i < len(phrase):
#     if word == phrase[i]:
#         print(phrase[i])
#         print(i)
#         i += 1