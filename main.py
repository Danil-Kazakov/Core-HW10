from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError("Phone number should be a string of 10 digits")

    def __str__(self):
        return f"Phone number: {self.value}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    def add_phone(self, phone_number: str):
        try:
            phone = Phone(phone_number)
            if phone not in self.phones:
                self.phones.append(phone)
        except ValueError as e:
            raise ValueError("Phone number should be a string of 10 digits") from e

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
        else:
            raise ValueError("Phone number does not exist")

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number does not exist")

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        return self.data.get(name)