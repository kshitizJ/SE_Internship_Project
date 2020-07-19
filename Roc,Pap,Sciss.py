# Importing random module for taking random choice.
import random

# Making a list of choices.
option = ["rock", "paper", "scissors"]

# Run variable acts as a boolean value.
flag = False

# While condition for taking user input till he/she decides to exit.
while(flag != True):

    # User and Computer points.
    usrPoints = 0
    comPoints = 0

    # Initializing two list, one for storing the winner and the scores, another for storing overall winner. They are also used to form a table
    values = []
    overall_values = []

    # No. of times user want to play the game.
    times = int(input("Enter no. of rounds you want to play with computer: "))

    #Empty print statement for new line.
    print()

    # Initializing while loop variable.
    time = 1

    # while loop to iterate no. of times user want to play the game
    while(time <= times):

        # Taking user input and assigning a random choice to computer.
        user = input("Enter your Choice\nRock\nPaper\nScissors\n\n")
        print()
        comp = random.choice(option)

        # To check if the input from the user matches one of the choice in the option list. If not than print Wrong input
        if user.lower() in option:

            # If user and computer value are equal than its a tie and to show the user and computer points and storing required information in a list.
            if user.lower() == comp:

                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("It's a Tie..")
                print("Your score = {}.".format(usrPoints))
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("Tie")
                values.append(usrPoints)
                values.append(comPoints)
            
            # If user's value is "rock" and computer's value is "paper" than computer is winner and computer's points are incremented and storing required information in a list.
            elif user.lower() == "rock" and comp == "paper":

                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("Computer is Winner..")
                print("Your score = {}.".format(usrPoints))
                comPoints += 1
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("Computer")
                values.append(usrPoints)
                values.append(comPoints)
            
            # If user's value is "rock" and computer's value is "scissors" than user is winner and user's points are incremented and storing required information in a list.
            elif user.lower() == "rock" and comp == "scissors":

                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("You are a Winner..")
                usrPoints += 1
                print("Your score = {}.".format(usrPoints))
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("User")
                values.append(usrPoints)
                values.append(comPoints)
            
            # If user's value is "paper" and computer's value is "rock" than user is winner and user's points are incremented and storing required information in a list.
            elif user.lower() == "paper" and comp == "rock":

                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("You are a Winner..")
                usrPoints += 1
                print("Your score = {}.".format(usrPoints))
                print("Computer score = {}.\n".format(comPoints))
            
                values.append(time)
                values.append("User")
                values.append(usrPoints)
                values.append(comPoints)

            # If user's value is "paper" and computer's value is "scissors" than computer is winner and computer's points are incremented and storing required information in a list.
            elif user.lower() == "paper" and comp == "scissors":
                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("Computer is Winner..")
                print("Your score = {}.".format(usrPoints))
                comPoints += 1
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("Computer")
                values.append(usrPoints)
                values.append(comPoints)
            
            # If user's value is "scissors" and computer's value is "paper" than user is winner and user's points are incremented and storing required information in a list.
            elif user.lower() == "scissors" and comp == "paper":
                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("You are a Winner..")
                usrPoints += 1
                print("Your score = {}.".format(usrPoints))
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("user")
                values.append(usrPoints)
                values.append(comPoints)
            
            # If user's value is "scissors" and computer's value is "rock" than computer is winner and computer's points are incremented and storing required information in a list.
            elif user.lower() == "scissors" and comp == "rock":
                print("Your choice = {}.".format(user.capitalize()))
                print("Computer choice = {}.".format(comp.capitalize()))
                print("Computer is Winner..")
                print("Your score = {}.".format(usrPoints))
                comPoints += 1
                print("Computer score = {}.\n".format(comPoints))

                values.append(time)
                values.append("Computer")
                values.append(usrPoints)
                values.append(comPoints)
        
            # Storing the whole list in the overall list and initializing it back to an empty list for next round.
            overall_values.append(values)
            values = []
            time += 1
        else:

            # If user enter values other than the option than print wrong input and this round won't be counted.
            print("Wrong input\nPlease enter only above options")
    

    # For printing an output in the form of a table.
    print("------------------------------------------------------------")
    print("|  Round  |   Winner   |  User Points  |  Computer Points  |")
    print("------------------------------------------------------------")

    for item in overall_values:

        print("|   ", item[0], " "*(3-len(str(item[0]))), "| ", item[1], " "*(8-len(item[1])), "|      ", item[2], " "*(6-len(str(item[2]))), "|        ", item[3], " "*(8-len(str(item[3]))), "|")

        print("------------------------------------------------------------")
    
    # Empty print statement for new line.
    print()
    
    # To print the over all winner of the game including points of all the rounds.
    if usrPoints > comPoints:
        print("---- You are a WINNER ----\n")
    elif usrPoints < comPoints:
        print("---- Computer is WINNER ----\n")
    else:
        print("---- It's a TIE ----\n")

    # To ask user if he/she wants to continue or quit.
    exit = input("Do you want to continue playing..\nPress (n/y)\n")

    print()
    if exit.lower() == "n":

        flag = True