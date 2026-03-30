from tkinter import N
from Char import Character
import Char


def attack(player : Character, opponant: Character):
    player_dmg = player.weapons.values + player.companion['basic_attack']
    opponant_dmg = opponant.weapons.values + opponant.companion.values
    round = 0
    while player.is_alive(player) and opponant.is_alive(opponant):
        round += 1
        print("Round 1:")
        if player_dmg > opponant_dmg:
            opponant.take_dmg(opponant, player_dmg)
            print(f"Opponant took {player_dmg} damage")
        else: 
            player.take_dmg(player, opponant_dmg)
            print(f"Player took {opponant_dmg} damage ")
        if player.is_alive == False:
            print("You Died")
        if opponant.is_alive == False:
            print("Opponant Died")
            player.gain_xp(player, opponant.lvl* 10)
            for loot in opponant.weapons:
                player.weapons.get(loot)

def basic_combat(player : Character, opponant: Character):
    return

def menu():
    print("Welcome to ZUPY101")
    print("This is where your character will live and we will write the fucnctions to levvel him up")
    pname =  input("What is your name traveler?")

    player = Character(name=pname,lvl=1, hp=10 ,exp=0, companion={}, weapons={"Fist" : 5})
    skell = Character("Skelly", lvl=1, hp=5, exp=0,companion={}, weapons={"Bone" : 3})
    
    player.print_character()

    select = None
    
    while select != 'stop' :
        print(
            f"-"*20,
            f"Time to start your adventure!",
            f"Choose a path",
            f"1) Print a pet",
            f"2) Explore a function",
            f"3) Explore Cave of Wonders",
            f"4) Answer a riddle",
            f"5) Create a Monster",
            f"0) Print your character stats",
            f"-"*20,
            sep="\n",
            )
                       
              
        select = int(input("Choose a number or 'stop' to exit "))
        
        if select == 1:
            print("You have chosen to print your pet!")
            print("Here is your test question....")
            answer = input("What do you type in python to print someting on the screen? ")
            if answer == "print()":
                print("That is correct!")
                player.create_pet()
                player.gain_xp(10)
                print("Exp + 10")
            else:
                print("Your test went arry!! incorrect.")
                player.take_dmg(5)

            continue
        elif select == 2:
            print("/nExplore a function!")
            print("Here is your question.... ")
            answer = input("If you wanted to create a function to build_a_bridge across the dangerious cavern what is the first comand word you type *hint its 3 letters long* ___ build_a_bridge(supplies): ")
            if answer == "def":
                print("You did it!")
                player.gain_xp(15)
                print("Exp + 15")
            else:
                print("The bridge colllapsed! incorrect")
                player.take_dmg(5)
            continue

        elif select == 3:
            print("Welcome to the Cave of Wonders!")
            choose = int(input("You see a \n1) Beautiful sword\n2) Shiny ring\nWhich do you grab? "))
            
            if choose == 1:
                print("You have awoke the sleeping dead! 5 skeletons arrive! Prepair for battle ")
                answer = input("write a loop statement to hit each skeleton to knock them out ")
                if answer == "for loop":
                    basic_combat(player, skell)
                    player.weapons["Great Python Sward"] = 20
                    print("You received a Great Sword!")
                else:
                    print("Outch you got boned!")
                    player.take_dmg(10)
           
            elif choose == 2:
                print("You grab the ring and make a run for it!")
                print("Question.... ")
                answer = input("Explain what % (Modulo) is to your instructor.")
                if answer == "Remainder of devision":
                    print("Correct!")
                    player.weapons["Ruby Ring"] = 20
                else:
                    print("You barely excape with your life. ")
           
        elif select == 4:
                print("Monster Creation!")
                print("This is where you learn about data classes and how to use them.")

        elif select == 0:
                 player.print_character()

        else:
           select == "stop"
           break
                

          

           
            




menu()