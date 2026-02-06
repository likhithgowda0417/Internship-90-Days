class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def show_balance(self):
        print("account holder:", self.name)
        print("balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest):
        self.interest = interest
        super().__init__(name, balance)

    def display_details(self):
        self.show_balance()
        print("interest rate:", self.interest)


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft):
        self.overdraft = overdraft
        super().__init__(name, balance)

    def display_details(self):
        self.show_balance()
        print("overdraft limit:", self.overdraft)


sa = SavingsAccount("rahul", 5000, 4.5)
ca = CurrentAccount("arjun", 3000, 10000)

sa.display_details()
ca.display_details()

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        self.roll_no = roll_no
        super().__init__(name)


class SportsPlayer(Person):
    def __init__(self, name, sport):
        self.sport = sport
        super().__init__(name)


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, roll_no, sport):
        Student.__init__(self, name, roll_no)
        SportsPlayer.__init__(self, name, sport)

    def display_details(self):
        print("name:", self.name)
        print("roll no:", self.roll_no)
        print("sport:", self.sport)


cs = CollegeStudent("kiran", 101, "cricket")
cs.display_details()

class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel):
        self._private_reels.append(reel)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("private reels:", self._private_reels)
        else:
            print("access denied! only followers can view private reels")

    def add_archived_reel(self, reel):
        self.__archived_reels.append(reel)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("archived reels:", self.__archived_reels)
        else:
            print("access denied! wrong password")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "access denied"

    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("password updated")
        else:
            print("wrong password")


acc = InstagramAccount("my_account", "1234")

acc.add_private_reel("friends trip")
acc.add_private_reel("gym reel")

acc.add_archived_reel("old reel 1")
acc.add_archived_reel("old reel 2")

acc.display_private_reels(True)
acc.display_private_reels(False)

acc.display_archived_reels("1234")
acc.update_password("1234", "5678")
acc.display_archived_reels("5678")
