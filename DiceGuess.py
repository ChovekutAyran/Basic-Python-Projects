#Imports the random module
import random


print("Welcome to Guess the Dice by ChovekutAyran")


#Sets a while loop so that you can continuoulsy play the game 
while True:

	#Sets a random number for the dices(Between 1 and 6) 
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)


	#Asks you for the numbers of the dices
	guess = input("Enter the first number: ")
	guess2 = input("Enter the second number: ")


	#Turns the answers into integers so that Python can compare the dices with your answers
	guess = int(guess)
	guess2 = int(guess2)



	#Compares the dices with your answers 
	if guess == dice1 and guess2 == dice2:
		print("Correct") 
		print("The answers are",dice1,dice2)
	else:
		print("Wrong")
		print("The answers are",dice1,"and",dice2)



	#Python asks you if you want to play again
	play_again = input("Do you want to play again?"+"Please type Y for YES or N for NO. ")


	#If you set the input as "Y", "y", "YES" or "yes" the while loop will continue 
	if play_again == "Y" or play_again == "y" or play_again == "YES" or play_again == "yes":
		continue

	#If you set the input as "N", "n", "NO" or "no", Python will bid farewell with you and will break the while loop, thus quitting the program 
	elif play_again == "N" or play_again == "n" or play_again == "NO" or play_again == "no":
		print("Goodbye")
		break 

	#If you do not set the input as one of the following the while loop will continue
	else:
		print("INVALID INPUT")
		continue
