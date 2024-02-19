from abc import ABC
import User


class Post(ABC):
    def __init__(self, type, owner: User):
        self.owner = owner
        self.type = type
        self.observers = []

        self.notify("new post")

    def __str__(self):
        pass

    def like(self, user):
        if self.owner.connected:
            if self.owner != user:
                print(f"notification to {self.owner.name}: ",end='')
                print(f"{user.name} liked your post")
                self.notify("like",user)

    def comment(self, user, comment):
        if self.owner.connected:
            if self.owner != user:
                print(f"notification to {self.owner.name}: ", end='')
                print(f"{user.name} commented on your post: {comment}")
                self.notify("comment",user)

    def notify(self, event, user=None):
        if event == "like":
            self.owner.notification.append(f"{user.name} liked your post")
            pass
        if event == "comment":
            self.owner.notification.append(f"{user.name} commented on your post")
            pass
        if event == "new post":
            for observer in self.observers:
                observer.update(f"{self.owner.name} has a new post")
