class User:
    def __init__(self, name : str, age: int, email: str, address: str, phone_number: str):
        self.name: str = name
        self.age: int = age
        self.email: str = email
        self.address: str = address
        self.phone_number: str = phone_number

    def __str__(self) -> str:
        return f'user: {self.name}. age: {self.age}. email: {self.email}. address: {self.address}. phone number: {self.phone_number}'

    def set_name(self, new_name) -> str:
        self.name = new_name
        return f"new name: {self.name}."

    def set_age(self, new_age) -> str:
        if 18 <= new_age <= 128:
            self.age = new_age
            return f'new age: {self.age}.'
        else:
            return f'invalid age.'

    def set_email(self, new_email) -> str:
        if '@' in new_email:
            self.email = new_email
            return f'new email: {self.email}.'
        else:
            return f'enter please correct email.'

    #  print_info(self), який виводитиме інформацію про користувача

    def set_address(self, new_address) -> str:
        self.address = new_address
        return f'new address: {self.address}'

    def set_phone_number(self, new_phone_number) -> str:
        if new_phone_number.startswith('+380'):
            self.phone_number = new_phone_number
            return f'new phone_number: {self.phone_number}'
        else:
            return f'enter please correct phone number.'


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


class System:
    def __init__(self):
        self.users: list = []
        self.admins: list = []

    def add_user(self, new_user: User) -> None:
        self.users.append(new_user)

    def add_admin(self, new_admin: Admin) -> None:
        self.admins.append(new_admin)

    def remove_user(self, removed_user: User) -> None:
        if removed_user in self.users:
            self.users.remove(removed_user)
            print('user removed successfully.')
        else:
            print('no such user in System.')

    def remove_admin(self, removed_admin: Admin) -> None:
        if removed_admin in self.users:
            self.users.remove(removed_admin)
            print('admin removed successfully.')
        else:
            print('no such admin in System.')

    def get_all_users(self) -> None:
        for cur_user in self.users:
            print(cur_user)

    def get_all_admins(self) -> None:
        for cur_admin in self.admins:
            print(cur_admin)


# user_1: User = User('Lera', 18, '848belval848@gmail.com', '111 street', '+380636307608')
# user_2: User = User('Amy', 28, 'Amyworker28@gmail.com', '112 street', '+380636307609')
# user_3: User = User('Bob', 98, 'Bobynineeight@gmail.com', '1 street', '+380111111111')
# system: System = System()
# system.add_user(user_1)
# system.add_user(user_2)
# system.add_user(user_3)
# system.get_all_users()
# system.remove_user(user_2)
# system.get_all_users()
#
# admin_1: Admin = Admin('Bill', 42, 'billmillie@gmail.com', '2 street', '+380111111112', 2)
# admin_2: Admin = Admin('Charu', 42, 'charu@gmail.com', '222 street', '+380111111122', 1)
#
# # print(admin_1)
# # print(admin_2)
# # admin_1.get_access_level()
# # admin_2.get_access_level()
#
# system.add_admin(admin_1)
# system.add_admin(admin_2)
# system.get_all_admins()