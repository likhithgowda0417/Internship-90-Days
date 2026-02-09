def admin_only(func):
    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role)
        else:
            print("access denied: admin only")
    return wrapper


@admin_only
def access_dashboard(user_role):
    print("welcome to admin dashboard")


access_dashboard("admin")
access_dashboard("user")

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0


print("sum:", MathUtils.add(10, 20))
print("is even:", MathUtils.is_even(8))
print("is even:", MathUtils.is_even(7))
