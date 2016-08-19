#import datetime import date
#print (date.today())
#import beautiful soup



""" Create a Phone book that stores phonebook entries
Include
1. Search ability
2. Add entries
3. Delete entries
4. Change entries"""
#search
phonebook = {
'Chris' : {'name': 'Chris', 'phone': "5043034302"}
}
try:
    search = input ('Who are you looking for?')
    print (phonebook [search.lower()])
    print (phonebook [search.lower()]['name'])
    print (phonebook [search.lower()]['age'])

except KeyError:
    print ('There is no entry of {}'.format(search))
# add entry
def add():
    name = input ('What is the name?')
    phone = input ('What is the phone?')
    phonebook ['dsr'] = {'name':'dsr', 'phone': '594-4546-456'}
    phonebook[name.lower()] = { 'name': name.capitalize (), 'phone': phone}
    print (phonebook)

    #delete entry
def delete():
    name = input ('What is the name you would like to delete?')
    phone = input ('What is the phone number for this person you would like to delete?\
    ')
    del phonebook[name.lower()]
    print (phonebook)

#change
def change():
    change_name = input ('What is the name you would like to change?')
    change_phone = input ('What is the phone number you would like to change?')
    new_name = input ('What would you name would you like to put instead?')
    new_phone = input ('What would the new number be?')
    del phonebook[name.lower()]
    print (phonebook)



#exit
#User input loop function
def phone_book():
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
            elif choice == 2:
               add()
            elif choice == 3:
                change()
            elif choice == 4:
               remove()
            elif choice == 5:
                exit()
        except ValueError:
                print(" Not valid, try again please!")
phone_book()
