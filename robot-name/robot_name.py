import string
import random

class Robot(object):

    all_robots = []

    def __init__(self):
        self.name = self.create_name()

    def create_name(self):
        letters = random.choices(list(string.ascii_uppercase), k=2)
        numbers = random.choices(range(0,9),k=3)
        name = ''.join(letters) + ''.join(str(x) for x in numbers)
        if name not in self.all_robots:
            self.all_robots.append(name)
        else:
            print("This robot already exist! We will try to use a different name.")
            self.create_name()
        return name

    def reset(self):
        self.all_robots.remove(self.name)

    def __str__(self):
        return f"{self.name}"
