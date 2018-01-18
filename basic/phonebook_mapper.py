import csv


def load_phonebook():
    pb = {}
    with open('phonebook.csv', newline='') as csvfile:
        phonebook = csv.reader(csvfile, delimiter=',')

        for row in list(phonebook)[1:]:
            pb[int(row[0])] = {'f_name': row[1], 'l_name': row[2], 'number': row[3]}
    return pb


def save_phonebook(dct):
    with open('phonebook.csv', 'w', newline='') as csvfile:
        phone_writter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        phone_writter.writerow(['id', 'f_name', 'l_name', 'number'])
        for id, entry in dct.items():
            phone_writter.writerow([id, entry['f_name'], entry['l_name'], entry['number']])


if __name__ == '__main__':
    print(load_phonebook())

    # save_phonebook({1: {'f_name': 'Chris', 'l_name': 'Jones', 'number': '5032779710'},
    #                 2: {'f_name': 'Sheri', 'l_name': 'Dover', 'number': '5035551212'}})