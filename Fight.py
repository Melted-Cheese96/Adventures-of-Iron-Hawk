import random
from time import sleep
import TextAdventureFirstbuild as main 

class Enemy:
    inventory = {'Weapon': None}
    
    def __init__(self, name, health):
        self.name = name
        self.health = health 




class Player:
    inventory = {'Weapon': None}

    def __init__(self, name, health):
        self.name = name
        self.health = health



damage = 0 
def DamageTaken(Damage):
    global damage
    damage = Damage
    print(type(damage))
    



def CombatSystem(Player, Enemy):
    enemyAlive = True
    fateList = ['You have struck the enemy with your fists!', 'You have been hit in the face by the enemy']
    while enemyAlive == True:
        fate = random.choice(fateList)
        if fate == fateList[0]:
            Enemy.health -= damage
            print(Enemy.health)
        elif fate == fateList[1]:
            print('You have been hit by the enemy')
            Player.health -= damage
            print(str(Player.health))



    
    
player = Player('Test1', 100)
enemy1 = Enemy('Test2', 100)

CombatSystem(player, enemy1)

DamageTaken(150)


if __name__ == '__main__':
    pass


