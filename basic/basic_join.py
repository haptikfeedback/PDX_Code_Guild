#convert words into kebab-case

# def kebabcase():
#     convert = phrase.split(" ")
#     kebab_case = "-".join(convert)
#     print(kebab_case)
#     return

# phrase = input("Please enter your title: ").lower()
# kebabcase()

def join_phrase(phrase_list):
    return '-'.join(phrase_list)

phrase = input("Enter the word to Kebab!: ")
p_l = phrase.split()
print(join_phrase(p_l))