import random
from time import sleep

#background objects/functions
congratulations_set = ("Well done!", "Bravo!", "Nice work!")
def player_input():
    player_input = input("Enter a number between 1 and 10 here: ")
    while player_input != '1' and \
          player_input != '2' and \
          player_input != '3' and \
          player_input != '4' and \
          player_input != '5' and \
          player_input != '6' and \
          player_input != '7' and \
          player_input != '8' and \
          player_input != '9' and \
          player_input != '10'and \
          player_input != 'q':
        print()
        print("You have entered an invalid value.")
        player_input = input("Please enter a number between 1 and 10: ")
    if player_input == 'q':
        player_input = 'q'
    else:
        player_input = int(player_input)
    return player_input


quit = 0

while quit != 'q':
    print("""
Welcome to the game of can-you-beat-the-computer?

Game rules:
1. The aim of the game is to compete with the computer to be the first to reach a target sum.
   You can choose the target sum or let it be randomly generated (the randomly generated sum will be between 100 to 150).

2. To start the game, you will select a number between 1 and 10.
    
3. The computer will then select a number between 1 and 10 to add to your number.

4. You and the computer will continue to take turns to select a number between 1 and 10 to
   add to the total sum.

5. The player who manages to get the total sum to be equal to the target number wins!
    Demo:
    You select "15" as the target number
    You select "1"        -> Total sum is now "1"
    Computer selects "10" -> Total sum is now "11"
    You select "4"        -> Total sum is now "15". Since "15" is the target number,
                             you win!

6. At any point in the game, you may enter 'q' to quit the game.""")
    print()
    choice = input("Enter 'c' for your own choice of the target sum or 'r' for a randomly generated target sum: ")
    while choice != 'c' and choice != 'r' and choice != 'q':
        print()
        print("Invalid option. Please select choice again.")
        choice = input("Enter 'c' for your own choice of the target sum or 'r' for a randomly generated target sum: ")              
    if choice == "c":
        print()
        target = input("Enter a target sum: ")
        if target.isnumeric() and target != '0' and target != 'q':
            target = int(target)
            while target > 200 or target < 49:
                print()
                if target > 200:
                    d = "large"
                else:
                    d = "small"
                print("You have chosen a rather ",d," number!",sep = "")
                b = input("Enter 'y' to confirm this target sum or 'n' to reset it: ")
                while b != 'y' and b != 'n' and b !='q':
                    print()
                    print("Invalid option. The current target sum selected is ",target,".",sep = "")
                    b = input("Please enter 'y' to confirm it or 'n' to reset it: ")
                if b == "y":
                    proceed = 1
                    break
                elif b == 'n':
                    print()
                    target = input("Enter a target sum: ")
                    if target.isnumeric() and target != '0' and target != 'q':
                        target = int(target)
                        proceed = 1
                    elif target == 'q':
                        quit = 'q'
                        proceed = 1
                        break
                    else:
                        proceed = 0
                    while proceed == 0:
                        print()
                        target = input("Invalid input. Enter a target number again: ")
                        if target.isnumeric() and target != '0':
                            target = int(target)
                            proceed = 1
                            break
                        elif target == 'q':
                            target = 50
                            proceed = 1
                            quit = 'q'
                            break
                        else:
                            proceed = 0
                else:
                    quit = 'q'
                    proceed = 1
                    break
        elif target == 'q':
            quit = 'q'
            proceed = 1
        else:
            proceed = 0
        while proceed == 0:
            print()
            target = input("Invalid input. Enter a target number again: ")
            if target.isnumeric() and target != '0':
                target = int(target)
                while target > 200 or target < 49:
                    print()
                    if target > 200:
                        d = "large"
                    else:
                        d = "small"
                    print("You have chosen a rather ",d," number!",sep = "")
                    b = input("Enter 'y' to confirm this target sum or 'n' to reset it: ")
                    while b != 'y' and b != 'n' and b !='q':
                        print()
                        print("Invalid option. The current target sum selected is ",target,".",sep = "")
                        b = input("Please enter 'y' to confirm it or 'n' to reset it: ")
                    if b == "y":
                        proceed = 1
                        break
                    elif b == 'n':
                        print()
                        target = input("Enter a target sum: ")
                        if target.isnumeric() and target != '0' and target != 'q':
                            target = int(target)
                            proceed = 1
                        elif target == 'q':
                            quit = 'q'
                            proceed = 1
                            break
                        else:
                            proceed = 0
                        while proceed == 0:
                            print()
                            target = input("Invalid input. Enter a target number again: ")
                            if target.isnumeric() and target != '0':
                                target = int(target)
                                proceed = 1
                                break
                            elif target == 'q':
                                target = 50
                                proceed = 1
                                quit = 'q'
                                break
                            else:
                                proceed = 0
                    else:
                        quit = 'q'
                        proceed = 1
                        break
            elif target == 'q':
                proceed = 1
                quit = 'q'
            else:
                proceed = 0
    elif choice == 'r':
        sleep(0.5)
        target = random.randint(100,150)
    else:
        quit = 'q'
    if quit != 'q':
        print()
        print("The target sum is ",target,". ","The game begins!",sep="")
        print()
        player_choice = player_input()
        if isinstance(player_choice,int):
            total = player_choice
            if total == target:
                print()
                print("You win. But that was not a meaningful game, was it?")
            while total < target:
                if quit == 'q':
                    break
                if total%11 == target%11:
                    comp_guess = random.randint(1,10)
                    print()
                    print("Thinking...")
                    sleep(1)
                    print("Computer selects ",comp_guess,".",sep="")
                    total = total + comp_guess
                    sleep(0.5)
                    print("Total is now ",total,".",sep="")
                    print()
                    player_choice = player_input()
                    if isinstance(player_choice,int):
                        total = total + player_choice
                        sleep(0.5)
                        print("Total is now ",total,".",sep="")
                        while total > target:
                            print()
                            total = total - player_choice
                            print("You overshot the target!"," The last total before you overshot was ",total,"."," Try a different number.",sep="")
                            player_choice = player_input()
                            if isinstance(player_choice,int):
                                total = total + player_choice
                            else:
                                quit = 'q'
                                break
                        if total==target:
                            sleep(0.5)
                            print()
                            print(random.choice(congratulations_set),"You win!")
                            break
                        if total < target:
                            total = total
                    else:
                        break                    
                elif total%11 < target%11:
                    comp_guess = target%11-total%11
                    print()
                    print("Thinking...")
                    sleep(1)
                    print("Computer selects ",comp_guess,".",sep="")
                    total = total + comp_guess
                    sleep(0.5)
                    print("Total is now ",total,".",sep="")
                    if total==target:
                        print()
                        sleep(0.5)
                        print("Computer wins!")
                        break
                    print()
                    player_choice = player_input()
                    if isinstance(player_choice,int):
                        total = total + player_choice
                        sleep(0.5)
                        print("Total is now ",total,".",sep="")
                    else:
                        break
                else:
                    comp_guess = (target%11+11)-total%11
                    print()
                    print("Thinking...")
                    sleep(1)
                    print("Computer selects ",comp_guess,".",sep="")
                    total = total + comp_guess
                    print("Total is now ",total,".",sep="")
                    if total==target:
                        print()
                        sleep(0.5)
                        print("Computer wins!")
                        break
                    print()
                    player_choice = player_input()
                    if isinstance(player_choice,int):
                        total = total + player_choice
                        sleep(0.5)
                        print("Total is now ",total,".",sep="")
                    else:
                        break
    print()
    quit = input('Game has ended. Enter "q" to close programme or "a" to play again: ')
    if quit=='q':
        break    
