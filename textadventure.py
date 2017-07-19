start = '''
"You wake up and get ready to go to Girls Who Code. You look at the clock and realize it's 8am, so you only have one hour to get there!"
'''

print(start)

time = 0

sub_or_bus = input("Do you want to take the bus or the subway?")

while sub_or_bus != "subway" or "bus":
    print("That's not a valid answer! Try again.")
    sub_or_bus = input("Do you want to take the bus or the subway?")


if sub_or_bus == "subway":
    time += 5


    loc_or_ex = input("Do you want to take express (10 min wait time) or local (2 min wait time)?")

    while loc_or_ex != "express" or "local":
        print("Not a valid answer! Try again.")
        loc_or_ex = input("Do you want to take express (10 min wait time) or local (2 min wait time)?")


        if loc_or_ex == "express": #This is the code for the express train
            time += 10
            stay_or_go = input("There's a sick passenger on the train. You can choose to get off or stay, which do you do?")
            while stay_or_go != "get off" or "stay":
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
            while left_or_right != "left" or "right":
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




if sub_or_bus == "bus":
    time += 5
    wait_or_geton = input("There's a fast bus 10 minutes away and a slower bus at the station. Do you wait or get on?")

    while wait_or_geton != "wait" or "get on":
        print("That's not a valid answer! Try again.")
        wait_or_geton = input("There's a fast bus 10 minutes away and a slower bus at the station. Do you wait or get on?")

    if wait_or_geton == "wait":
        time += 10
        stay_or_getoff = input("The bus driver knocks off someone's rearview mirror and now they're arguing with the car's owner. Do you stay or get off?")
        while stay_or_getoff != "stay" or "get off":
            print("That's not a valid answer. Try again.")
            stay_or_getoff = input("The bus driver knocks off someone's rearview mirror and now they're arguing with the car's owner. Do you stay or get off?")
        if stay_or_getoff == "get off":
            time += 30
            print("You wait 15 minutes for the next bus and ride it for 15 minutes. You get off and walk for 5 minutes.")
            print("You made it on time! It took you " + str(time) + " minutes to get to GWC.")
        if stay_or_getoff == "stay":
            print("There's a heated argument between the bus driver and the car driver. It's entertaining, but unfortunately takes as long as a TV show. You wait 30 minutes.")
            time += 30
            print("The drive takes 15 minutes, and when you finally get off you have to walk for 5 minutes.")
            time += 20
            print("You get to GWC but you're late! You took " + str(time) + " minutes.")

    if wait_or_geton == "get on":
        time += 10
        fight_or_flight = input("After 10 minutes, a guy comes on the bus and starts threatening to beat a woman up. Do you ignore him or do you stand up for the woman?")
        while fight_or_flight != "ignore him" or "stand up":
            print("That's not a valid answer! Try again.")
            fight_or_flight = input("After 10 minutes, a guy comes on the bus and starts threatening to beat a woman up. Do you ignore him or do you stand up for the woman?")
        if fight_or_flight == "stand up":
            print("You try to reason with the man and then he starts fighting you, but you're able to beat him. The fight takes 20 minutes.")
            time += 20
            print("The guy gets kicked off and the drive takes 15 minutes. You walk 5 minutes to GWC and make it there on time! It took you " + str(time) + " minutes.")
        if fight_or_flight == "ignore him":
            print("The situation quickly escalates and the guy starts beating everyone up. The bus driver has to detain the guy by tazing him and kicking him off the bus. This takes 40 minutes.")
            time += 40
            print("The drive takes 15 minutes, and you have to walk 5 minutes to get to GWC. You have a black eye, and the rest of your day was very miserable.")
            time += 20
            print("You were very late! You took " + str(time) + " minutes.")
