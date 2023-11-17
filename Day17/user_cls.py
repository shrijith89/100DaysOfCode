class User:
    i = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def method(self):
        print(self.i)


user1 = User("Test", 123)
user2 = User("Test1", 456)
user1.i = 20
user1.method()