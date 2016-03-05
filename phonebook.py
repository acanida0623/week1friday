import json


with open("phonebook.json") as json_file:
    phone_book = json.load(json_file)


def save_phonebook():
    with open('phonebook.json', 'w') as fp:
        json.dump(phone_book, fp)


def main():


    print("Welcome to the Phone Book!")
    while True:
        print("-" * 40)
        print("Press 1 to search.")
        print("Press 2 to add.")
        print("Press 3 to change an entry.")
        print("Press 4 to remove.")
        print("Press 5 to exit.")
        print("-" * 40)
        try:
            choice = int(input('> '))
            if choice == 1:
                search()
            if choice == 2:
                add()
            if choice == 3:
                change()
            if choice == 4:
                remove()
            if choice == 5:
                save_phonebook()
                exit()

        except ValueError:
            print("That is not a valid entry. Please try again.")

def search():
    while True:
        search_name = str(input("Who's number would you like to search for? "))

        if search_name == '5':

            exit()
        for key, value in phone_book.items():
            if key.lower() == search_name.lower():
                print("{name}'s number is {phone}".format(name=value['name'].title(),phone=value['phone']))
                break
        else:
            print("There is nobody by that name in your phone book. ")


def add():
    key_name = str(input("Who would you like to add to your phonebook? ")).lower()

    val_name = key_name.title()

    string = "What is the number for {name} ".format(name=val_name.title())

    phone = str(input(string))

    phone_book[key_name] = {'name':val_name,'phone':phone}

    print("{name} has been added to your phonebook! ".format(name=val_name.title()))

    save_phonebook()




def change():
    name_to_change = str(input("Who's number would you like to change? ")).lower()

    for key, value in phone_book.items():

        if key.lower() == name_to_change.lower():

            new_num = str(input("What would you like to change {name}'s number to? ".format(name=value['name'].title())))

            value['phone'] = new_num

            print("{name}'s  new number is {phone}".format(name=value['name'].title(),phone=value['phone']))

            save_phonebook()

            break

        else:

            print("There is nobody by that name in your phone book. ")



def remove():
    name_to_remove = str(input("Who would you like to remove from your phone book? ")).lower()
    try:
        phone_book.pop(name_to_remove, None)

        print("{name} has been removed from your phone book." )

        save_phonebook()

    except KeyError:
        
        print("There is nobody by that name in your phone book.")

main()
