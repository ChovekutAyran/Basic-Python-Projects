#The following block of code is the class of functions that come with the Calculator 
class calculator:
	def addition(a,b):
		#This function allows you to add
		add = a + b
		return add
		
	def subtraction(a,b):
		#This functiom allows you to subtract
		subt = a - b 
		return subt

	def multiplication(a,b):
		#This function allows you to mulitply
		mult = a * b 
		return mult
		
	def division(a,b):
		#This function allows you to divide. Added the Exception for the ZeroDivisionError
		try:
			div = a / b
		except ZeroDivisionError:
			div = float('inf')
		return div


print("Welcome to Python Calculator by 3DDI3")
while True:
	#With the following block of code, Python will give you the list of operations that you can use with the Calculator 
	print("Select Operation.")
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Quit")





	#With the following line, Python will ask you which operation you want to be executed 
	choice = input("Enter choice 1/2/3/4/5: ")


	#With the following line, Python will ask you for the first numebr of the equation and will set it as an integer 
	z = int(input("Enter first number: "))

	#With the following line, Python will ask you for the second number of the equation and will set it as an integer 
	y = int(input("Enter second number: "))




	#If you choose 1 as the input, Python will use the addition function 
	if choice == '1':
		print(z,"+",y,"=", calculator.addition(z,y))

	#If you choose 2 as the input, Python will use the subtraction function 
	elif choice == '2':
		print(z,'-',y,'=', calculator.subtraction(z,y))

	#If you choose 3 as the input, Python will use the multiplication function 
	elif choice == '3':
		print(z,'*',y,'=', calculator.multiplication(z,y))

	#If you choose 4 as the input, Python will use the division function 
	elif choice == '4':
		print(z,'/',y,'=', calculator.division(z,y))

	#If you choose 5 as the input, Python will quit the Calculator 
	elif choice == "5" :
		print("Goodbye")
		break

	#If you choose a value that is not given in the list, the output will be this 
	else:
		print("INVALID INPUT")
		continue




#With this block of code, Python asks you if you want to calculate again 
	calc_again = input("Do you want to calculate again? "+"Please type Y for YES or N for NO.")

	#If you set the output as Y, y, YES, or yes, Python will continue 
	if calc_again == "Y" or calc_again == "y" or calc_again == "YES" or calc_again == "yes":
		continue

	#If you set the output as N, n. NO, or no, Python will bid farewell with you and quit the Calculator
	elif calc_again == "N" or calc_again == "n" or calc_again == "NO" or calc_again == "no":
		print("Goodbye")
		break
