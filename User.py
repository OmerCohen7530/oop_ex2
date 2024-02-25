from PostFactory import PostFactory


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.connected = True
        self.followers = [] #everyone who follows me
        self.post_list = []
        self.notification=[]


    def __str__(self):
        s = ("User name: "+self.name +
             ", Number of posts: " + str(len(self.post_list)) +
             ", Number of followers: "+str(len(self.followers)))
        return s

    def follow(self, user):
        if user == self:
            raise Exception("You cannot follow yourself")
        if self.connected:
            if self not in user.followers:
                user.followers.append(self)
                user.update_observers()
                print(f"{self.name} started following {user.name}")
            else:
                raise Exception(f"User {self.name} already follow")
        else:
            raise Exception("user is not connected")

    def unfollow(self, user):
        if user == self:
            raise Exception("You cannot follow yourself")
        if self.connected:
            if self in user.followers:
                user.followers.remove(self)
                user.update_observers()
                print(f"{self.name} unfollowed {user.name}")
            else:
                raise Exception(f"User {self.name} already unfollow")
        else:
            raise Exception("user is not connected")

    def publish_post(self, type, info, price= None, place= None):
        if self.connected:
            if self.connected:
                post_factory = PostFactory()
                post = post_factory.create_post(self, type, info, price, place)
                self.post_list.append(post)
                return post
        else:
            raise Exception("user is not connected")
        return None


    def connect(self, password):
        if not self.connected:
            if self.password == password:
                self.connected = True
                print(f"{self.name} connected")
            else:
                raise Exception("wrong password")
        else:
            raise Exception("user is already connected")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print(f"{self.name} disconnected")
        else:
            raise Exception("user is already disconnected")

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for note in self.notification:
            print(note)
        pass

    def update(self, event):
        self.notification.append(event)
        pass

    def update_observers(self):
        for post in self.post_list:
            post.add_remove_observer()