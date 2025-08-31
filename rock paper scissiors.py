import random

print("\n===Rock,Paper,Scissors===")
playerscore=0
computerscore=0
roundsplayed=0

while True:
    print("Enter Your choice")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit the game")

#Playerinput
    choice=input("Your choice (1-4):")

    if choice=="1":
        playerchoice= "Rock"
    elif choice=="2":
        playerchoice="Paper"
    elif choice=="3":
        playerchoice="Scissors"
    elif choice=="4":
        print("\n Thanks for playing")
        print(f"Final Score: player {playerscore} - {computerscore} Computer")
        print(f"Total rounds played: {roundsplayed}")
        break
    else:
        print("Invalid input(Please enter 1,2,3 or 4)")
        continue
#Computer Choice
    computerchoice=random.choice(["Rock", "Paper", "Scissors"])
    print(f"\nYou Chose: {playerchoice} - Computer Chose: {computerchoice}")
    roundsplayed+=1
#Decide Winner
    if playerchoice==computerchoice:
        print("Its a draw!")
    elif (playerchoice=="Rock" and computerchoice=="Scissors") or (playerchoice=="Paper" and computerchoice=="Rock") or (playerchoice=="Scissors" and computerchoice=="Paper"):
        print("You win this round")
        playerscore+=1
    else:
        print("Computer win this round")
        computerscore+=1


    print(f"Score---Player: {playerscore} --- Computer: {computerscore}\n")
    print("-" * 40)



