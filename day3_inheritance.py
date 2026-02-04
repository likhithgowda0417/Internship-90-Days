#Example 1: Father → Son (Single Inheritance)
class Father:
    def __init__(self, surname, father_name):
        self.surname = surname
        self.father_name = father_name

    def display_family_details(self):
        print("surname:", self.surname)
        print("father name:", self.father_name)


class Son(Father):
    def __init__(self, name, surname, father_name):
        self.name = name
        super().__init__(surname, father_name)

    def display_name(self):
        print("son name:", self.name)


son1 = Son("arjun", "kumar", "rajesh")
son1.display_name()
son1.display_family_details()

#Example 2: Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("title:", self.title)
        print("author:", self.author)


class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        self.issued_to = issued_to
        self.issued_date = issued_date
        super().__init__(title, author)

    def display_issued_book(self):
        self.display_book()
        print("issued to:", self.issued_to)
        print("issued date:", self.issued_date)


book1 = IssuedBook("python basics", "john", "student", "04-02-2026")
book1.display_issued_book()

#Example 3: Banking System
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("account holder:", self.name)
        print("balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(name, balance)

    def display_details(self):
        self.show_balance()
        print("interest rate:", self.interest_rate)


acc1 = SavingsAccount("vikram", 5000, 4.5)
acc1.display_details()
