class calculator:

	#This function allows you to add
	def addition(a, b):
		add = a + b
		return add
		

	#This functiom allows you to subtract	
	def subtraction(a, b):
		subt = a - b 
		return subt


	#This function allows you to mulitply
	def multiplication(a, b):
		mult = a * b 
		return mult
		

	#This function allows you to divide. Added Exception for ZeroDivisionError
	def division(a, b):
		try:
			div = a / b
		except ZeroDivisionError:
			div = int('0')
		return div


	#This function allows you to use modular arithmetic. Added Exception for ZeroDivisionError
	def modular(a, b):
		try:
			mod = a % b
		except ZeroDivisionError:
			mod = int('0')
		return mod



print("Welcome to Python Calculator by ChovekutAyran")


#Sets a while loop so that you can continuously calculate
while True:
	#With the following block of code, Python will give you the list of operations that you can use with the Calculator 
	print("Select Operation.")
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Modular Arithmetic")
	print("6.Quit")




	#With the following line, Python will ask you which operation you want to be executed 
	choice = input("Enter choice 1/2/3/4/5: ")


	#If your choice does not equal one of the given options the loop will restart
	if choice > "6" or choice <"1":
		print("INVALID INPUT")
		continue


	#If you choose "5" as the input, the while loop will break, thus quitting the Calculator 
	if choice == "6":
		print("Goodbye")
		break



	#With the following line, Python will ask you for the first numebr of the equation and will set it as an integer. Added exception for ValueError	
	try:
		z = int(input("Enter first number: "))

	except ValueError:
		print("INVALID INPUT")
		continue


	#With the following line, Python will ask you for the second number of the equation and will set it as an integer. Added exception for ValueError
	try:
		y = int(input("Enter second number: "))

	except ValueError:
		print("INVALID INPUT")
		continue




	#If you choose 1 as the input, Python will use the addition function 
	if choice == '1':
		print(z, "+", y, "=", calculator.addition(z,y))


	#If you choose 2 as the input, Python will use the subtraction function 
	elif choice == '2':
		print(z, '-', y, '=', calculator.subtraction(z,y))


	#If you choose 3 as the input, Python will use the multiplication function 
	elif choice == '3':
		print(z, '*', y, '=', calculator.multiplication(z,y))


	#If you choose 4 as the input, Python will use the division function 
	elif choice == '4':
		print(z, '/' ,y, '=', calculator.division(z,y))


	elif choice == '5':
		print(z, '%', y, '=', calculator.modular(z,y))


	#If you choose a value that is not given in the list, the output will be this 
	else:
		print("INVALID INPUT")
		continue




	#With the following line, Python asks you if you want to calculate again 
	calc_again = input("Do you want to calculate again? "+"Please type Y for YES or N for NO.")



	#If you set the output as Y, y, YES, or yes, Python will continue 
	if calc_again == "Y" or calc_again == "y" or calc_again == "YES" or calc_again == "yes":
		continue


	#If you set the output as N, n. NO, or no, Python will bid farewell with you and quit the Calculator
	elif calc_again == "N" or calc_again == "n" or calc_again == "NO" or calc_again == "no":
		print("Goodbye")
		break


	#If you do not set the input as one of the following the while loop will continue
	else:
		print("INVALID INPUT")
		continue
