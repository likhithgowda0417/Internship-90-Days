class User:
    def __init__(self, name, email):
        self.name = name              # public
        self._email = email           # protected
        self.__password = "default"   # private

    def set_password(self, new_password):
        self.__password = new_password

    def verify_password(self, password):
        return password == self.__password


class ApplicationUser(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
        self._features = []

    def add_feature(self, feature):
        self._features.append(feature)

    def show_features(self):
        print("features accessible:", self._features)


class SecureApplication(ApplicationUser):
    def __init__(self, name, email, role):
        super().__init__(name, email, role)
        self.__secure_data = []

    def add_secure_data(self, data, password):
        if self.verify_password(password):
            self.__secure_data.append(data)
        else:
            print("access denied: wrong password")

    def view_secure_data(self, password):
        if self.verify_password(password):
            print("secure data:", self.__secure_data)
        else:
            print("access denied: wrong password")


# -------- main execution --------

user1 = SecureApplication("arjun", "arjun@gmail.com", "admin")

user1.set_password("1234")

user1.add_feature("dashboard")
user1.add_feature("reports")

user1.show_features()

user1.add_secure_data("confidential file", "1234")
user1.add_secure_data("salary data", "0000")

user1.view_secure_data("1234")
user1.view_secure_data("0000")
