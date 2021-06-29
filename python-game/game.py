# Kelvin Phat, Joshua Nwabuzor



# monster room- you will need to rename this function.
def monster_room():
    # some prompts
    # '\n' is to print the line in a new line
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")
    # ask for input
    answer = input("> ").lower()

    if answer == "1":
        print("You manage to escape the room filled with monsters.")
        route_1()
    elif answer == "2":
        game_over("You died")
    else:
        game_over("Don't you know how to type something properly?")

def route_1():
    print("\nYou made it out alive!")
    print("Well, you don't have time to think because you have come accross to path ways. (left or right)")
    answer = input("> ").lower()
    if answer == "left":
        game_over("Cursed end")
    elif answer == "right":
        print("Cursed end")
    else:
        game_over("Don't you know how to type something properly?")

def route_2():
    print("\nYou gather up enough courage to fight the monster.")
    print("However, you need a weapon to fight the beast.")
    print("Conveniently there are weapons on the floor. You see a sword and a credit card.")
    print("Which one do you choose? (sword or credit card)")
    answer = input("> ").lower()
    if answer == "sword":
        print("You pick up the mighty sword! As the beast lunges towards you, you take your blade and")
        print("with a strong grip, you slice the beast's head off!")
        game_over("You win!")
    elif answer == "credit card":
        print("You pick up the credit card. For some reason, you are able to deal considerable damage to the beast with this handy card.")
        print("You slash the beast multiple times, knocking the beast back to hell.")
        game_over("You win!")
    else:
        game_over("Don't you know how to type something properly?")

        
# function to ask play again or not
def play_again():
  # use print statement to ask if user wants to play again
  print("\nDo you want to play again? (y or n)")
  # get input
  answer = input("> ").lower()
  # evaluate input using conditional 
  if "y" in answer:
    start()
  else:
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
    print("\nYou are standing in a dark room.\nWhat do you do?")
    print("1) Stand still")
    print("2) Look for some sort of light")
    # get user input using input() and save 
    answer = input("> ").lower()

    # use a loop to manage game -- 
    if answer == "1":
        game_over("Nothing happened.")
    if answer == "2":
        monster_room()
    else:
        game_over("Don't you know how to type something properly?")

# calling start function. 
start()