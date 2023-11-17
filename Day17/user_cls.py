class User:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def method(self):
        print(self.name)


user1 = User("Test", 123)
user2 = User("Test1", 456)
