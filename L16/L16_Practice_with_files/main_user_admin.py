from class_User import User
from class_Admin import Admin
from class_System import System


user_1: User = User('Lera', 18, '848belval848@gmail.com', '111 street', '+380636307608')
user_2: User = User('Amy', 28, 'Amyworker28@gmail.com', '112 street', '+380636307609')
user_3: User = User('Bob', 98, 'Bobynineeight@gmail.com', '1 street', '+380111111111')
system: System = System()
system.add_user(user_1)
system.add_user(user_2)
system.add_user(user_3)
system.get_all_users()
system.remove_user(user_2)
system.get_all_users()

admin_1: Admin = Admin('Bill', 42, 'billmillie@gmail.com', '2 street', '+380111111112', 2)
admin_2: Admin = Admin('Charu', 42, 'charu@gmail.com', '222 street', '+380111111122', 1)

# print(admin_1)
# print(admin_2)
# admin_1.get_access_level()
# admin_2.get_access_level()

system.add_admin(admin_1)
system.add_admin(admin_2)
system.get_all_admins()