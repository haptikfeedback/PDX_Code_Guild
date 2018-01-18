email = input("Please enter your email address: ")
at_index = email.index("@")
end_index = email.index('.com')
print(email[at_index + 1: end_index])
 