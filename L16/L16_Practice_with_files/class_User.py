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

    def set_address(self, new_address) -> str:
        self.address = new_address
        return f'new address: {self.address}'

    def set_phone_number(self, new_phone_number) -> str:
        if new_phone_number.startswith('+380'):
            self.phone_number = new_phone_number
            return f'new phone_number: {self.phone_number}'
        else:
            return f'enter please correct phone number.'