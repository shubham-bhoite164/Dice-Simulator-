# this will import the random module
import random

# If we wanna play that whoever gets higher value wins
def main():
    player1 = 0
    player1wins = 0

    player2 = 0
    player2wins = 0

    rounds = 1

    while rounds != 5:
        print("Round" + str(rounds))
        player1 = dice_roll()
        print(player1)
        player2 = dice_roll()
        print(player2)

        rounds = rounds + 1

        if player1>player2:
            print("Player 1 won")
            player1wins = player1wins + 1

        elif player2>player1:
            print("Player 2 won")
            player2wins = player2wins + 2

        else:
            print("It's a draw")

        print()

        if player1wins>player2wins:
            print("Player1 won the entire game")

        elif player2wins>player1wins:
            print("Player2 won the entire game")

        else:
            print("It's a Draw")


# To gerenate the Random values for dice
def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll
print(dice_roll())
print(dice_roll())
print(dice_roll())
print(dice_roll())

print()
print()

main()
