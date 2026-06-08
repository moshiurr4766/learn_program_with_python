"""Inheritance example."""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def profile(self):
        return f"{self.name} <{self.email}>"


class Admin(User):
    # Admin inherits name, email, and profile from User.
    def __init__(self, name, email, role):
        super().__init__(name, email)  # Calls parent constructor.
        self.role = role

    def profile(self):
        # Method overriding: child class changes parent behavior.
        return f"{super().profile()} - Role: {self.role}"


user = User("Moshiur", "moshiur@example.com")
admin = Admin("Nadia", "nadia@example.com", "Manager")

print(user.profile())
print(admin.profile())
