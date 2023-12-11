import random

def dice_roll():

    game = True if (input("If you want to game, put yes/no:-").lower()) == 'yes'.lower() else False

    dice_face = {

        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
        
        }

    while game:
        dice1 = random.choice(list(dice_face.items()))
        dice2 = random.choice(list(dice_face.items()))

        print(f"You've got {dice1[0]} {dice1[1]} and {dice2[0]} {dice2[1]} ")
        #print(dice_face)

        break

dice_roll()