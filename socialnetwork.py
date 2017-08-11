import turtle
import math

myTurtle = turtle.Turtle()
x_pos = 0
y_pos = 0


def drawCircle(x, y):
    myTurtle.penup()
    myTurtle.goto(x_pos+x, y_pos+y)
    myTurtle.speed(0)
    myTurtle.pendown()
    myTurtle.circle(50,360,360)

drawCircle(-100, 100)
myTurtle.write("lena", font=("Arial", 16, "normal"))

drawCircle(100, 100)
myTurtle.write("leyla", font=("Arial", 16, "normal"))

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
            drawCircle(x,y)
            name = input("What is your name?")
            myTurtle.write(name, font=("Arial", 16, "normal"))
            user_password = input("What do you want your password to be?")
            user = User(name,user_password,number_users)
            network.addUser(name,number_users,x,y)
            print(network.getUsers())
            print(user.password)
            print(user.id)
            print(network.getCoordinates())
            x += 100
            y -= 100

        if answer == "add friend":
            myTurtle.penup()
            myTurtle.goto(0,0)
            myTurtle.pendown()
            friend = input("Who?")
            userlist = network.getUsers()
            friendlist = user.getFriends()
            if friend in userlist.values():
                if friend not in friendlist:
                    user.addFriend([friend,0])
                    print(user.getFriends())
                    for key, people in network.getUsers().items():
                        if people == friend:
                            friend_key = key
                            print(key)
                    friend_coordinates = network.getCoordinates()[friend_key]
                    myTurtle.goto(friend_coordinates[0],friend_coordinates[1])
                    myTurtle.penup()
                else:
                    print("already friends")
            else:
                print("not in network")
            print(user.friends)
        if answer =="like":
            likedperson = input("Who?")




# Runs your program.
if __name__ == '__main__':
    main()
