start = '''
"You wake up and get ready to go to Girls Who Code. You look at the clock and realize it's 8am, so you only have one hour to get there!"
'''

print(start)

time = 0

sub_or_bus = input("Do you want to take the bus or the subway?")

if sub_or_bus == "subway":
    time += 5
    loc_or_ex = input("Do you want to take express (10 min wait time) or local (2 min wait time)?")

    if loc_or_ex == "express": #This is the code for the express train
        time += 10
        stay_or_go = input("There's a sick passenger on the train. You can choose to get off or stay, which do you do?")
        if stay_or_go == "get off":
            time += 45
            print("It takes a really long time to find another train and get on it. You finally get off and take a 5 minute walk to GWC.")
            time += 5
            print("You lost! It took you " + str(time) + " minutes to get to GWC.")
        if stay_or_go == "stay":
            time += 30
            print("You stay on the train and arrive after 30 minutes. You take a 5 minute walk and are on time! It took you " + str(time) + " minutes to get to GWC.")

    if loc_or_ex == "local": #This is the code for the local train
        time += 12
        print("You come across train traffic. You wait an extra 10 minutes.")
        time += 33
        left_or_right = input("You exit and the sidewalks you usually use are blocked. Do you go left or right?")
        while left_or_right != "right":
            print("You walked around and couldn't find a route and ended up where you started.")
            time += 10
            left_or_right = input("You exit and the sidewalks you usually use are blocked. Do you go left or right?")
        if left_or_right == "right" and time < 61:
            time += 5
            print("You find an alternative route and get there on time! You get there in " + str(time) + " minutes.")
        if left_or_right == "right" and time > 60:
            print("You finally got there but it's too late! You took " + str(time) + " minutes.")
