"""Inheritance example."""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def profile(self):
        return f"{self.name} <{self.email}>"


class Admin(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

    def profile(self):
        return f"{super().profile()} - {self.role}"


user = User("Moshiur", "moshiur@example.com")
admin = Admin("Nadia", "nadia@example.com", "Manager")

print(user.profile())
print(admin.profile())

