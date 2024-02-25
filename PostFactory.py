from matplotlib import image as mpimg, pyplot as plt

import User
from Post import Post


class TextPost(Post):
    def __init__(self, type, info, owner):
        super().__init__(type, owner)
        self.info = info
        print(self)

    def __str__(self):
        s = self.owner.name + " published a post:\n"
        s = s +"\"" +self.info +"\"" + "\n"
        return s


class ImagePost(Post):
    def __init__(self, type, info, owner):
        super().__init__(type, owner)
        self.info = info
        print(self)

    def __str__(self):
        s = self.owner.name + " posted a picture" + "\n"
        return s

    def display(self):
        image = mpimg.imread(self.info)
        plt.imshow(image)
        plt.show()
        print("Shows picture")
        pass


class SalePost(Post):
    def __init__(self, type, info, price, place, owner):
        super().__init__(type, owner)
        self.info = info
        self._price = price
        self._place = place
        self._is_sold = False
        print(self)

    def __str__(self):
        s = self.owner.name + " posted a product for sale:\n"
        if self._is_sold:
            s = s + "Sold! "
        else:
            s = s + "For sale! "
        s = s + self.info + ", price: " + str(self._price) + ", pickup from: " + self._place + "\n"
        return s

    def discount(self, percent, password):
        if self.owner.connected:
            if password == self.owner.password:
                self._price = self._price * (1 - percent / 100)
                print(f"Discount on {self.owner.name} product! the new price is: {self._price}")
            else:
                raise Exception("wrong password")
        else:
            raise Exception("user is not connected")

    def sold(self, password):
        if self.owner.connected:
            if password == self.owner.password:
                self._is_sold = True
                print(f"{self.owner.name}'s product is sold")
            else:
                raise Exception("wrong password")
        else:
            raise Exception("user is not connected")


class PostFactory():
    @staticmethod
    def create_post(owner: User, type, info, price=None, place=None):
        if type == "Text":
            post_factory = TextPost(type, info, owner)
            return post_factory
        elif type == "Image":
            post_factory = ImagePost(type, info, owner)
            return post_factory
        elif type == "Sale":
            post_factory = SalePost(type, info, price, place, owner)
            return post_factory
