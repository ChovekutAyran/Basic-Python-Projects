#Imports the random module 
import random

#Imports the time module  
import time


print("Welcome to Player vs. PC(Dice) by ChovekutAyran")


#Slows the time 
time.sleep(1.5)


#Gives you the options that you can select
print("Select:")
print("1.Play")
print("2.Quit")



#Asks if you want to play the game or quit 
choice = input("Enter choice 1/2: ")



#Sets a while loop so that you can continuously play the game 
while True:


	#If you set the input the as "1" the program will continue
	if choice == "1":
		pass

	#if you set the input as "2" the loop will break, thus ending the program
	if choice == "2":
		print("Goodbye")
		break
	



	#Sets a random number for you(Between 1 and 6)
	player = random.randint(1,6)

	#Sets a radnom number for your opponent(Between 1 and 6)
	ai = random.randint(1,6)


	#Prints your number 
	print("You rolled",player)

	#Prints your oppenent's number(Using time.sleep to slow down the results)  
	print("The computer is rolling the dices...")
	time.sleep(1)
	print("The computer rolled...")
	time.sleep(2)
	print(ai)


	#Compares your number with your opponent's number 
	if player > ai :
		print("You win")
	elif player == ai :
		print("Tie game")
	else:
		print("You lose")


	#Asks you if you want to play again
	play_again = input("Do you want to play again?"+"Please type Y for YES or N for NO. ")


	
	#If you set the input as "Y" or "y" or "YES" or "yes", the while loop will continue
	if play_again == "Y" or play_again == "y" or play_again == "YES" or play_again == "yes":
		continue

	#If you set the input as "N" or "n" or "NO" or "no", Python will bid farewell with you and break the while loop, thus ending the program 
	elif play_again == "N" or play_again == "n" or play_again == "NO" or play_again == "no":
		print("Goodbye")
		break

	#If you do not set the input as one of the following, Python will restart the loop 
	else:
		print("INVALID INPUT")
		continue
