from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = name
	

class Phone(Field):
    def __init__(self, number):
         self.value = check_number(number)

    def check_number(self, number):
         if number == 10:
              return number
         else:
              raise ValueError("The phone number must contain 10 digits")
         

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass
