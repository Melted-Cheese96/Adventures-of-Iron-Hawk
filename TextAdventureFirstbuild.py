#main code for text adventure. WIP as of 25/9/18 
#import Fight as f
import BlackSmith as b



class Player:

    possibleWeapons = {'sword': 50}
    inventory = {'Weapon': None, 'gold': 1000}

    def __init__(self, name, health):
        self.name = name
        self.health = health


        
name = input('What is your name? ')
TestPlayer = Player(name, 100)
print('Name : ' + TestPlayer.name)
print('Current health : ' + str(TestPlayer.health))

b.StoreIntro(TestPlayer)
