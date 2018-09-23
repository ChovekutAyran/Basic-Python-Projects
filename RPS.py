#Rock, Paper, Scissors
#While loops are used so that you can quit when prompted.


#Imports sys module.
import sys 

#Imports time module.
import time as t

#imports random module.
import random as r




#Sets a while loop so that you can continuosly play.
while True:


	print("Welcome to Rock, Paper, Scissors by ChovekutAyran")
	print("Select:")
	print("1.Play against another Player")
	print("2.Play against the Computer")
	print("3.Quit")


	select = input("Enter Your Choice(1/2/3): ")




	if select < "1" or select > "3":
		print("INVALID INPUT")
		continue


	#If the gamemode is set to 1, the match will be PvP.
	if select == "1":


		while True:

			#Asks P1 for his/hers name.
			playerName1 = input("What is your name, P1?\n")

			t.sleep(0.5)

			#Asks P2 for his/hers name.
			playerName2 = input("What is your name, P2?\n")




			while True:


				#Asks P1 for his/hers choice between rock, paper or scissors. %s is replaced with the playerName1 variable via the sys module.
				playerChoice1 = input("%s, do you choose Rock, Paper or Scissors? (Select with 1/2/3)\n" % playerName1)

				if playerChoice1 < "1" or playerChoice1 > "3":
					print("INVALID INPUT")
					continue


				#Asks P2 for his/hers choice between rock, paper or scissors. %s is replaced with the playerName2 variable via the sys module.
				playerChoice2 = input("%s, do you choose Rock, Paper or Scissors? (Select with 1/2/3)\n" % playerName2)

				if playerChoice2 < "1" or playerChoice2 > "3":
					print("INVALID INPUT")
					continue



				#If P1's and P2's choice are the same, a tie game will be declared.
				if playerChoice1 == playerChoice2:
					print("Tie Game!")




				#Outcomes where P1 wins.
				if playerChoice1 == "1" and playerChoice2 == "3":
					print("%s wins!" % playerName1)


				elif playerChoice1 == "2" and playerChoice2 == "1":
					print("%s wins!" % playerName1)


				elif playerChoice1 == "3" and playerChoice2 == "2":
					print("%s wins!" % playerName1)




				#Outcomes where P2 wins.
				if playerChoice2 == "1" and playerChoice1 == "3":
					print("%s wins!" % playerName2)


				elif playerChoice2 == "2" and playerChoice1 == "1":
					print("%s wins!" % playerName2)


				elif playerChoice2 == "3" and playerChoice1 == "2":
					print("%s wins!" % playerName2)




				t.sleep(1)


				playAgain1 = input("Do you want to play again? (Type Y for YES or N for NO then press Enter.)\n")




				if playAgain1 == "Y" or playAgain1 == "y":
					t.sleep(1)
					continue


				elif playAgain1 == "N" or playAgain1 == "n":
					print("Thanks for playing!\nGoodbye.")
					break


				else:
					print("INVALID INPUT")
					continue




			#These if statemnts break the loops if they are true.
			if playAgain1 == "N" or playAgain1 == "n":
				break


		if playAgain1 == "N" or playAgain1 == "n":
			break


	#If the wanted gamemode is 2, the match will be PvE.
	if select == "2":


		while True:


			#Asks the player for his/hers name.
			playerName = input("What is your name?\n")




			print("Your Turn!")

			t.sleep(0.4)


			while True:


				#Asks the player for his/hers choice between rock, paper or scissors. %s is replaced with the playerName variable via the sys module.
				playerChoice = input("%s do you choose Rock, Paper or Scissors? (Select with 1/2/3)\n" % playerName)


				if playerChoice < "1" or playerChoice > "3":
					print("INVALID INPUT")
					continue


				t.sleep(0.5)



				print("Computer's Turn!")

				t.sleep(0.4)


				#List of options that the computer has.
				options = ["Rock","Paper","Scissors"]

				#Sets a random choice from the list.
				computerChoice = r.choice(options)


				print("the Computer chose",computerChoice)

				t.sleep(0.5)




				#outcomes where the player wins.
				if playerChoice == "1" and computerChoice == "Scissors":
					print("You Win!")


				elif playerChoice == "2" and computerChoice == "Rock":
					print("You Win!")


				elif playerChoice == "3" and computerChoice == "Paper":
					print("You Win!")




				#Outcomes where the computer wins.
				if computerChoice == "Rock" and playerChoice == "3":
					print("The Computer Wins!")


				elif computerChoice == "Paper" and playerChoice == "1":
					print("The Computer Wins!")


				elif computerChoice == "Scissors" and playerChoice == "2":
					print("The Computer Wins!")




				#Outcomes where a tie game is declared.
				if playerChoice == "1" and computerChoice == "Rock":
					print("Tie Game!")


				elif playerChoice == "2" and computerChoice == "Paper":
					print("Tie Game!")


				elif playerChoice == "3" and computerChoice == "Scissors":
					print("Tie Game!")




				t.sleep(1)


				playAgain = input("Do you want to play again? (Type Y for YES or N for NO then press Enter.)\n")




				if playAgain == "Y" or playAgain == "y":
					t.sleep(1)
					continue


				elif playAgain == "N" or playAgain == "n":
					print("Thanks for playing!\nGoodbye.")
					break




			#These if statements break the outside loops if they are true.
			if playAgain == "N" or playAgain == "n":
				break


			if playAgain == "N" or playAgain == "n":
				break


	#If you select 3 instead of any gamemode the if statement will be true, thus breaking the loop.
	if select == "3":
		print("Goodbye.")
		break
