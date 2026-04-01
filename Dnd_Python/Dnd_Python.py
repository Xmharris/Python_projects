import json
from tkinter import N
from Char import Character




def attack(player : Character, opponant: Character):
    ### Basic Attack where two Character objects compair strenght of themself, their weapons, and their pets combined###
    player_dmg = player.weapons.values + player.companion['basic_attack']
    opponant_dmg = opponant.weapons.values + opponant.companion.values
    round = 0
    while player.is_alive(player) and opponant.is_alive(opponant):

        round += 1
        print(f"Round {round}:")
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

    player = Character(pname,lvl=1, hp_max=10 , hp=10, exp=0, companion={}, weapons={"Fist" : 5}, invantory={})
    skell = Character("Skelly", lvl=1, hp_max=5,hp=5, exp=0,companion={}, weapons={"Bone" : 3}, invantory={'Magic Bean': "Just a regular bean so it appears"})
    mouse = Character('Squeek', 1, 2, 5, 5, {}, {})
    pirate = Character('Black Beard', 10, 40, 40, 30, {'Polly': 5}, {'Sword': 8, 'Peg Leg': 5})

    monsters = [skell, mouse, pirate]
    player.print_character()

    select = None
    
    while select != 'stop' :
        player.level_check()
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
                       
              
        try:
           select = int(input("Choose a number or 'stop' to exit "))
        except:
            select = "stop"

        
        if select == 1:
            print("You have chosen to print your pet!")
            print("Here is your test question....")
            answer = input("What do you type in python to print someting on the screen? ")
            if answer == "print()":
                print("That is correct!")
                player.create_pet()
                player.gain_xp(20)
                print("Exp + 20")
            else:
                print("Your test went arry!! incorrect.")
                player.take_dmg(5)

            continue
        elif select == 2:
            print("/nExplore a function!")
            print("Here is your question.... ")
            answer = input("If you wanted to create a function to build_a_bridge across the dangerious cavern what is the first comand word you type *hint its 3 letters long* ___ build_a_bridge(supplies): ").islower()
            if answer == "def":
                print("You did it!")
                player.gain_xp(25)
                print("Exp + 25")
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
                    player.gain_xp(40)
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
                    player.gain_xp(20)
                else:
                    print("You barely excape with your life. ")

        elif select == 4:
            print("Riddle me this... ")
            answer = (input("What does Skelly have in his pocket?"))
            print(answer)
            if answer == "a magic bean":
                print("You got it!")
                player.gain_xp(20)
                print(f"{player.name} + 20 exp")
                print("Bonus question")
                answer = input("What is the <Type> of the magic bean")
                if answer == "dictionary key value pair":
                    player.invantory.get(skell.invantory['Magic Bean'])

  
           
        elif select == 5:
                print("Monster Creation!")
                print("This is where you learn about data classes and how to use them.")
                for m in monsters:
                    print(f"-"*10,
                          f"Name: {m.name}",
                          f"Hp: {m.hp}",
                          f"Lvl: {m.lvl}",
                          f"Xp: {m.exp}",
                          f"Pets: {m.companion}",
                          f"Weapons: {m.weapons}",
                          f"Inventory: {m.invantory}",
                          f"-" * 10,
                          sep='\n'
                          )
        elif select == 0:
                 player.print_character()

        else:
           select == "stop"
           break


    # print("Save Menu")
    # save = (input("Save your character yes or no?"))
    # if save == "yes":
    #     player.save_character()

                

          

           
            




menu()