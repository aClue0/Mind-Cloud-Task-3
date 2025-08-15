class Phone:
    def __init__(self):
        self.__contacts = []
    def addContact(self,contact):
        if contact in self.__contacts:
            return 'Contact is already added!\n'
        else:
            self.__contacts.append(contact)
            return f'{contact} was added successfully!\n'
        
    def getContacts(self):
        return self.__contacts
    
    def removeContact(self,contact):
        if contact in self.__contacts:
            self.__contacts.remove(contact)
            return f'{contact} removed successfully!\n'
        else:
            return 'No Contact with the specified name!\n'
    def call(self,contact):
        if contact in self.__contacts:
            return f'Calling {contact}...'
        else:
            return f'Can\'t call {contact}, not a contact!\n'

class Camera:
    def takePic(self):
        return ('The picture was taken successfully!\n')

class SmartPhone(Phone, Camera):
    def __init__(self):
        super().__init__()  

def testing():
    myphone = SmartPhone()
    print("\n-------------------- Hello, welcome to your phone! --------------------\n")
    while (True):
        choice = input("1. Add a contact\n2. Remove a contact\n3. Call a contact\n4. Take a picture\n5. Exit\nChoice: ")
        match choice:
            case '1':
                contact = input('\nAdd a contact: ')
                print(f'{myphone.addContact(contact)}')     
            case '2':
                contact = input('\nRemove a contact: ')
                print(f'{myphone.removeContact(contact)}')
            case '3':
                contact = input('\n Who do you want to call? ')
                print(f'{myphone.call(contact)}')
            case '4':
                print(f'{myphone.takePic()}')
            case '5':
                break
            case _:
                print('\nPlease enter a valid choice!\n')
    print("-------------------- Bye, have a great day! --------------------\n")

if __name__ == "__main__":
    testing()