class senders:
    def __init__(self,owner):
        self.observer = []
        self.owner = owner



    def add_remove_observer(self):
        self.observers = self.owner.followers.copy()

    def notify(self, event, user=None):
        if event == "like":
            self.owner.notification.append(f"{user.name} liked your post")
            pass
        if event == "comment":
            self.owner.notification.append(f"{user.name} commented on your post")
            pass
        if event == "post":
            for observer in self.observers:
                observer.update(f"{self.owner.name} has a new post")
            pass