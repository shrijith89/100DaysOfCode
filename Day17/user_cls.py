class User:
    i = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Test", 123)
user2 = User("Test1", 456)
user2.follow(user1)
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)
