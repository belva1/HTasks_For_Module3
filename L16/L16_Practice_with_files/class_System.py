from class_User import User
from class_Admin import Admin


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