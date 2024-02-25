import User
from senders import senders


class Post(senders):
    def __init__(self, post_type, owner: User):
        super().__init__(owner)
        # self.owner = owner
        self.type = post_type
        # self.observers: User = []
        self.add_remove_observer()
        self.notify("post")

    def __str__(self):
        pass

    # def add_remove_observer(self):
    #     self.observers = self.owner.followers.copy()

    def like(self, user):
        if self.owner.connected:
            if self.owner != user:
                print(f"notification to {self.owner.name}: ", end='')
                print(f"{user.name} liked your post")
                self.notify("like", user)
        else:
            raise Exception("user is not connected")

    def comment(self, user, comment):
        if self.owner.connected:
            if self.owner != user:
                print(f"notification to {self.owner.name}: ", end='')
                print(f"{user.name} commented on your post: {comment}")
                self.notify("comment", user)
        else:
            raise Exception("user is not connected")

    # def notify(self, event, user=None):
    #     if event == "like":
    #         self.owner.notification.append(f"{user.name} liked your post")
    #         pass
    #     if event == "comment":
    #         self.owner.notification.append(f"{user.name} commented on your post")
    #         pass
    #     if event == "post":
    #         for observer in self.observers:
    #             observer.update(f"{self.owner.name} has a new post")
    #         pass
