from getpass import getpass as input

print("Rock! Paper! Scissors!")
print()
print()
print("Player 1!")
playerOne = input("select your move (R, P or S) ")
print("Player 2!")
playerTwo = input("select your move (R, P or S) ")

if playerOne == "R":
    if playerTwo == "R":
        print("Boulders! It's a tie!")
    elif playerTwo == "P":
        print("Player two's paper smothers player one's rock!")
    elif playerTwo == "S":
        print("Player one's rock crushes player two's scissors!")
elif playerOne == "P":
    if playerTwo == "R":
        print("Player one's paper smothers player two's rock!")
    elif playerTwo == "P":
        print("Papers everywhere, it's a tie!")
    elif playerTwo == "S":
        print("Player two's scissors slices player one's paper!")
elif playerOne == "S":
    if playerTwo == "R":
        print("Player two's rock crushes player one's scissors!")
    elif playerTwo == "P":
        print("Player one's scissors slices player two's paper!")
    elif playerTwo == "S":
        print("Dice it all, it's a tie!")
