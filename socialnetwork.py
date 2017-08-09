class User:

    def __init__(self,name):
        self.name = name
        self.friends = []

    def addFriend(self,friend):
        self.friends =  self.friends.append(friend)

    def getName(self):
        return self.name

    def getFriends(self):
        return self.friends



class Network:

    def __init___(self,name):
        self.users = []

    def getUsers(self):
        return self.users


def main():

    name = input("What is your name?")
    User(name)


# Runs your program.
if __name__ == '__main__':
    main()
