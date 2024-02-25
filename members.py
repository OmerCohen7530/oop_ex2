class members:
    def __init__(self):
        self.post_list = []
        self.notification = []


    def update(self, event):
        self.notification.append(event)
        pass

    def update_observers(self):
        for post in self.post_list:
            post.add_remove_observer()