class User:
    def __init__(self,
                 nickname: str,
                 password,
                 age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def get_nick(self):
        return self.nickname


class Users:
    def __init__(self):
        self.users: list[User] = []
        self.users_names: list[str] = []

    def __contains__(self, item) -> bool:
        return item in self.users_names

    def __getitem__(self, index):
        return self.users[index]

    def add_user(self, user: User) -> bool:
        if user.nickname in self.users_names:
            return False
        else:
            self.users.append(user)
            self.users_names.append(user.nickname)
            return True

    def del_user(self, user_name: str):
        if user_name in self.users_names:
            index_to_delete = self.users_names.index(user_name)
            self.users.pop(index_to_delete)
            self.users_names.pop(index_to_delete)
            print(f"{user_name} удалён")
        else:
            print("Данного пользователя не существует")

    def get_user(self, user_name: str) -> tuple[bool, User]:
        if user_name in self.users_names:
            return True, self.users[self.users_names.index(user_name)]
        else:
            return False, None


if __name__ == "__main__":
    user1 = User("Man", "1123", 19)
    users = Users()
    users.add_user(user1)
    print("Man" in users)
    print(users[0].nickname)
    users.del_user("woman")
    print(users.get_user("Man")[1])
    print(users.get_user("Man")[1].password == hash("1123"))
    users.del_user("Man")
