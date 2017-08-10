import turtle
import math

myTurtle = turtle.Turtle()
x_pos = 0
y_pos = 0


def drawCircle(x, y):
    myTurtle.penup()
    myTurtle.goto(x_pos+x, y_pos+y)
    myTurtle.speed(0)
    for i in range(0,360):
        myTurtle.pendown()
        myTurtle.forward(1)
        myTurtle.right(1)

drawCircle(-100, 100)
lena_pos = [-100, 100]
drawCircle(100, 100)


class User:

    def __init__(self,name,password,id):
        self.name = name
        self.friends = []
        self.password = password
        self.id = id

    def addFriend(self,friend):
        self.friends.append(friend)

    def getName(self):
        return self.name

    def getFriends(self):
        return self.friends



class Network:

    def __init__(self):
        self.userlist = {1: "lena", 2: "leyla"}
        self.coordinates = {1: [-100,100], 2: [100,100]}

    def addUser(self,user,num,x,y):
        self.userlist[num] = user
        self.coordinates[num] = [x,y]

    def getUsers(self):
        return self.userlist

    def getCoordinates(self):
        return self.coordinates


def main():

    run = True
    network = Network()
    number_users = 2
    x = 0
    y = 0

    while run == True:
        answer = input("What do you want to do?")

        if answer == "exit":
            break

        if answer == "make profile":
            number_users += 1
            drawCircle(0,0)
            name = input("What is your name?")
            user_password = input("What do you want your password to be?")
            user = User(name,user_password,number_users)
            network.addUser(name,number_users,x,y)
            print(network.getUsers())
            print(user.password)
            print(user.id)
            print(network.getCoordinates())

        if answer == "add friend":
            friend = input("Who?")
            userlist = network.getUsers()
            friendlist = user.getFriends()
            if friend in userlist.values():
                if friend not in friendlist:
                    user.addFriend(friend)
                     #here we want to find the key of the "friend" name and use that to find the value of the corresponding key
                     #in the coordinates list to find the "friend"'s coordinates and draw a line to it
                else:
                    print("already friends")
            else:
                print("not in network")
            print(user.friends)

        x += 100
        y -= 100




# Runs your program.
if __name__ == '__main__':
    main()
