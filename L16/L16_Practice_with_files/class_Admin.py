from class_User import User


class Admin(User):
    def __init__(self, name: str, age: int, email: str, address: str, phone_number: str, access_level: int):
        super().__init__(name, age, email, address, phone_number)
        self.access_level: int = access_level

    def __str__(self) -> str:
        return f'admin: {self.name}. age: {self.age}. email: {self.email}. address: {self.address}. phone number: {self.phone_number}. access level: {self.access_level}.'

    def get_access_level(self):
        if self.access_level == 2:
            print('access level: Super Admin')
        else:
            print('access level: Admin')