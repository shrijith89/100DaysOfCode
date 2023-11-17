class User:

    def __init__(self, name, id):
        self.name = name
        self.id = id


user1 = User("Test", 123)
user2 = User("Test1", 456)

print(user2.name)