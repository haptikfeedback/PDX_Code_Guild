phonebook = {
    'jones': {
        'f_name': 'Chris',
        'l_name': 'Jones',
        'number': 5032779710
    },
    'dover': {
        'f_name': 'Sheri',
        'l_name': 'Dover',
        'number': 5032779710
    }
}


# Create New Contact
def create(f_name, l_name, number):
    if l_name not in phonebook:
        phonebook[l_name.lower()] = {'f_name': f_name, 'l_name': l_name, 'number': number}
    else:
        print('{} {} is already in the phonebook!'.format(f_name, l_name))


# Retrieve Contact
def search():
    name = input("Enter the last name of the person you are looking for.\n>: ").lower()

    if name in phonebook:
        print(phonebook[name]['f_name'])
        print(phonebook[name]['l_name'])
        print(phonebook[name]['number'])
    else:
        query = input('I can\'t find anyone by that name. Would you like to create a contact? (y/n)').lower()
        if query in 'yes':
            f = input("Enter the first name of the person you are adding.\n>: ")
            last = input("Enter the last name of the person you are adding.\n>: ")
            n = input("Enter the phone number of the person you are adding.\n>: ")
            create(f, last, n)
        elif query in 'no':
            return None
        else:
            print('I don\'t understand you...')


# Update Existing Contact
def update(old_l_name, f_name, l_name, number):
    delete(old_l_name)
    create(f_name, l_name, number)


# Delete Contact
def delete(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print('I can not find anyone by that name.')


if __name__ == "__main__":
    while True:
        query = input('1: Search\n'
                      '2: Add\n'
                      '3: Edit\n'
                      '4: Remove\n'
                      'Type exit to quit.\n>: ')
        if query == '1':
            search()
        elif query == '2':
            f = input("Enter the first name of the person you are adding.\n>: ")
            last = input("Enter the last name of the person you are adding.\n>: ")
            n = input("Enter the phone number of the person you are adding.\n>: ")
            create(f, last, n)
        elif query == '3':
            old_l_name = input('Please enter the old last name of the person you are changing\n>: ').lower()
            f_name = input('Please enter the new first name of the person you are changing\n>: ')
            l_name = input('Please enter the new last name of the person you are changing\n>: ')
            number = input('Please enter the new number of the person you are changing\n>: ')
            update(old_l_name, f_name, l_name, number)
        elif query == '4':
            na = input("Enter the last name of the person you would like to remove.\n>: ")
            delete(na)
        elif query == 'exit':
            exit()
        else:
            print("I'm sorry, I can not do that right now.")