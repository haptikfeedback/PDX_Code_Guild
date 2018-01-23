def check_this_letter(in_letter):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    sometimes_vowel_list = ['y']
    if in_letter in vowel_list:
        return "That is a vowel."
    elif in_letter in sometimes_vowel_list:
        return "That is sometimes a vowel."
    else:
        return "Go back to grammar school."