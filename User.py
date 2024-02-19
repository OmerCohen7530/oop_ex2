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
        if self not in user.followers:
            user.followers.append(self)
            self.post_update()
            print(f"{self.name} started following {user.name}")

    def unfollow(self, user):
        if self in user.followers:
            user.followers.remove(self)
            self.post_update()
            print(f"{self.name} unfollowed {user.name}")

    def publish_post(self,type,info, price= None, place= None):
        if self.connected:
            post_factory = PostFactory()
            post = post_factory.create_post(self, type, info, price, place)
            self.post_list.append(post)
            self.post_update()
            return post
        return None

    def post_update(self):
        for post in self.post_list:
            post.observers = self.followers

    def connect(self, password):
        if self.password == password:
            self.connected = True
            print(f"{self.name} connected")

    def disconnect(self):
        self.connected = False
        print(f"{self.name} disconnected")

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for note in self.notification:
            print(note)
        pass

    def update(self, event):
        self.notification.append(event)
        pass
