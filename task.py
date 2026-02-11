# ================================
# Task 1: Book system where book details can be displayed, updated, and deleted
# ================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("title:", self.title)
        print("author:", self.author)

    def update(self, title, author):
        self.title = title
        self.author = author

    def delete(self):
        self.title = None
        self.author = None


book = Book("python basics", "john")
book.display()
book.update("advanced python", "david")
book.display()
book.delete()


# ================================
# Task 2: Mobile comparison feature
# ================================

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


m1 = Mobile("samsung", 30000)
m2 = Mobile("oneplus", 35000)
print(m1 > m2)


# ================================
# Task 3: User object creation flow
# ================================

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print("username:", self.username)
        print("email:", self.email)


user = User("rahul", "rahul@gmail.com")
user.display()


# ================================
# Task 4: Database connection handler
# ================================

class Database:
    def connect(self):
        print("database connected")

    def close(self):
        print("database closed")


db = Database()
db.connect()
db.close()


# ================================
# Task 5: Calculator callable feature
# ================================

class Calculator:
    def __call__(self, a, b):
        return a + b


calc = Calculator()
print("result:", calc(10, 20))


# ================================
# Task 6: Shopping cart system
# ================================

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display(self):
        print("cart items:", self.items)


cart = Cart()
cart.add_item("laptop")
cart.add_item("mouse")
cart.display()
cart.remove_item("mouse")
cart.display()


# ================================
# Task 7: Session closing feature
# ================================

class Session:
    def close(self):
        print("session closed successfully")


session = Session()
session.close()


# ================================
# Task 8: Library search feature
# ================================

class Library:
    def __init__(self, books):
        self.books = books

    def search(self, book):
        return book in self.books


library = Library(["python", "java", "c++"])
print("book found:", library.search("python"))


# ================================
# Task 9: Employee salary comparison feature
# ================================

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


e1 = Employee(40000)
e2 = Employee(35000)
print(e1 > e2)


# ================================
# Task 10: Counter iterator system
# ================================

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration


for number in Counter(5):
    print(number)
