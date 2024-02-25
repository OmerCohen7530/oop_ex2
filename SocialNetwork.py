from User import User


class SocialNetwork:
    _initialized = None
    def __new__(cls, name):
        if cls._initialized is None:
            cls._initialized = super().__new__(cls)
            cls._initialized.name = name
            cls._initialized.users_list = []
            print(f"The social network {name} was created!")
        return cls._initialized

    def __init__(self, name):
        if not self._initialized:
            self._initialized = True


    def __str__(self):
        s= self.name + " social network:\n"
        for user in self.users_list:
            s =s+ str(user)+"\n"
        return s

    def sign_up(self, username, password):
        if 4 <= len(password) <= 8:
            user = User(username, password)
            self.users_list.append(user)
            return user
        else:
            raise Exception("password must be between 4 and 8 characters")

    def log_out(self, username):
        flag = False
        for user in self.users_list:
            if user.name == username:
                flag = True
                user.disconnect()
        if not flag:
            raise Exception("username does not exist")

    def log_in(self, username, password):
        flag = False
        for user in self.users_list:
            if user.name == username:
                flag = True
                user.connect(password)
        if not flag:
            raise Exception("username does not exist")