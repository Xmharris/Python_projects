import json
from tkinter.messagebox import QUESTION
from Character import Character
import zupy_questions
import random

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

# def basic_combat(player : Character, opponant: Character):
#     return

def menu():
    print("Welcome to ZUPY101")
    print("This is where your character will live and we will write the fucnctions to levvel him up")
    pname =  input("What is your name traveler? ")

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
            f"1) Adopt a pet",
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

        num = None
        if select == 1:
            print("You must first answer a question before you can create your companion.")
            num = random.randint(1,16)
            q = zupy_questions.questions.get(num)
            a = zupy_questions.answers.get(num)
            answer = input(q)

            if answer == a:
                print("That is correct!")
                
            else:
                print("Your test went arry!! incorrect. You still get a companion")
                player.take_dmg(5)
                print(f"{player.name} took 5 damage!")
            player.create_pet()
            player.gain_xp(20)
            print("Exp + 20")
               
        elif select == 2:

            num = random.randint(1,16)
            q = zupy_questions.questions.get(num)
            a = zupy_questions.answers.get(num)
            answer = input(q)

            if answer == a:
                print("That is correct!")
                player.gain_xp(20)
                player.invantory['Dodge in a Bottle'] = "Use to avoid receiving damage (uses automaticly one time)"
                dodge = True
                
            else:
                print("Bridge collapsed")
                if not dodge:
                    player.take_dmg(5)
                    print(f"{player.name} took 5 damage!")
                else:
                    dodge = False
                    print ("You dodged the attack")
            print("Exp + 20")
           

        elif select == 3:
            print("Welcome to the Cave of Wonders!")
            choose = int(input("You see a \n1) Beautiful sword\n2) Shiny ring\nWhich do you grab? "))
            
            if choose == 1:
                print("You have awoke the sleeping dead! 5 skeletons arrive! Prepair for battle ")
                answer = input("write a loop statement to hit each skeleton to knock them out ")
                if answer == "for loop":
                    # basic_combat(player, skell)
                    player.weapons["Great Python Sward"] = 20
                    print("You received a Great Sword!")
                    player.gain_xp(40)
                else:
                    if not dodge:
                        player.take_dmg(5)
                        print(f"{player.name} took 5 damage!")
                    else:
                        dodge = False
                        print ("You dodged the attack")
                    

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
            if answer == "magic bean":
                print("You got it!")
                player.gain_xp(20)
                print(f"{player.name} + 20 exp")

            print("Bonus Round")
            count = 0
            wrong = False
            while not wrong:

                num = random.randint(1,16)
                q = zupy_questions.questions.get(num)
                a = zupy_questions.answers.get(num)
                answer = input(q)

                if answer == a:
                    print("That is correct! 30 Exp!")
                    player.gain_xp(30)
                    count += 1
                    if count % 3 == 0:
                        player.create_pet()

                else:
                    wrong = True
                    print(f"Incorrect. You made it {count} rounds")
                    break
                
  
           
        elif select == 5:
                print("Monster Creation!")
                print("This is where you learn about data classes and how to use them.")
                print("Here are the current monsters:")
                for m in monsters:
                    print(f"-"*10,
                          f"Name: {m.name}",
                          f"Max Hp: {m.hp_max}",                        
                          f"Lvl: {m.lvl}",
                          f"Xp: {m.exp}",
                          f"Pets: {m.companion}",
                          f"Weapons: {m.weapons}",
                          f"Inventory: {m.invantory}",
                          f"-" * 10,
                          sep='\n'
                          )
                fight = input("Want to fight one? Type the name or 'No' to run")
                if fight not in monsters or fight == 'No':
                    print("You ran away")
                    continue
                else:
                    attack(player,fight)
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