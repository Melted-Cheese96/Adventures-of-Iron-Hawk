import string 
import random 
from time import sleep 

alphabet = string.ascii_lowercase

def generateBoard(): #Generates the board NOTE: STILL TESTING THIS 
    global grid 
    grid = {}
    for x in range(1,25):
        for item in alphabet:
            name = item + str(x)
            #grid[name] = 'enemy placeholder'
            grid[name] = ''
            
def displayBoard():
    for keys, values in grid.items():
        print(keys + ':' + values)

def changePos(original_position):
    enemy_choice = originalPosition
    while enemy_choice == original_position:
        enemy_choice = random.choice(alphabet) + str(random.randint(27))
    if grid[enemy_choice] == '':
        grid[enemy_choice] = 'enemy placeholder'
    else:
        changePos(enemy_choice)
            


def generateEnemies(): #This function generates the enemies 
    possible_choices = string.ascii_lowercase
    possible_choices = list(possible_choices)
    enemy_choice = random.choice(possible_choices) + str(random.randint(1,27))
    if grid[enemy_choice] == '':
        grid[enemy_choice] = 'enemy placeholder'
    else:
        changePos(enemy_choice)
    
    

    
def combat2(player, enemy): #This function is responsible for making the d20 randomizer. Basically the main combat system
    double_damage_enemies = ['Rogue'] #This is the list that contains the name of the player classes that do double damage.
    print('You will be fighting {}'.format(enemy.name))
    roll = input("Do you want to go into 'roll mode'? Or 'use healing staff'?")
    if roll.lower() == 'roll mode':
        while True:
            roll2 = input('Roll dice?')
            if roll2 == 'yes':
                print('Rolling dice...')
                d20Randomizer = random.randint(1,20)
                sleep(2)
                print('You rolled a {}'.format(d20Randomizer))
                if d20Randomizer >= 10:
                    print('You have rolled past the enemies AC!')
                    print('You do {} damage'.format(player.weaponDamage))
                    enemy.HP -= player.weaponDamage
                    print('Enemy now has {} health'.format(enemy.HP))

                elif d20Randomizer == 20:
                    print('Critical Hit!')
                    sleep(2)
                    enemy.HP -= player.weaponDamage + 20
                    print(enemy.HP)

                elif d20Randomizer <= 4:
                    print('The enemy has done damage to you!')
                    player.HP -= enemy.weaponDamage
                    print('Your health is now {}'.format(player.HP))
                    
                else:
                    print('You did not get past the enemies AC')
                    print('Restarting...')
                    sleep(2)
                if enemy.HP <= 0:
                    print('You have defeated the enemy!')
                    break 
                elif player.HP <= 0:
                    print('The enemy has defeated you, you die')
                    break
            elif roll2 == 'no':
                decision = input("Do you want to 'heal yourself'? Or 'run away'?")
                if decision.lower() == 'heal yourself':
                    HealPlayer(player)
                elif decision.lower() == 'run away': #Add this
                    pass 
    elif roll.lower() == 'use healing staff':
        HealPlayer(player)

generateBoard()
generateEnemies()
sleep(3)
displayBoard()

