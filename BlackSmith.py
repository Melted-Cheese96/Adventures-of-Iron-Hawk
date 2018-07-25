#import TextAdventureFirstBuild as main
#import Fight as f
from time import sleep 


class Merchant:

    weaponStock = {'sword': 100, 'axe': 70, 'Small Knife': 10}
    

 


def StoreIntro(player1):
    merchant1 = Merchant()
    print('Welcome to the blacksmith store!')
    sleep(2)

    print('Here are the items that we have on sale') 

    print("Would you like to buy something, type either 'yes' or 'no'")
    buy = input()

    if buy.lower() == 'yes':
        print('Here are the items that you can choose from')
        print(merchant1.weaponStock)
        sleep(2)
        print('What do you want to buy?')
        item = input()
        if item.lower() == 'sword': #CONTINUE
            if player1.inventory['gold'] > 100:
                print('Purchasing item...')
                player1.inventory['gold'] -= 100
                player1.inventory['weapon'] = 'sword'
                print(player1.inventory)
        elif item.lower() == 'axe': #CONTINUE
            pass
        elif item.lower() == 'small knife': #CONTINUE
            pass
        else:
            print('Error, did you spell everything right? Try again')
    elif buy.lower() == 'no':
        print('Leaving store')




if __name__ == '__main__':
    pass
