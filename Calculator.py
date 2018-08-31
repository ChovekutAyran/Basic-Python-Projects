class calculator:
	def addition(a,b):
		add = a + b
		return add
		#This function allows you to add
	def subtraction(a,b):
		subt = a - b 
		return subt
		#This functiom allows you to subtract
	def multiplication(a,b):
		mult = a * b 
		return mult
		#This function allows you to mulitply
	def division(a,b):
		try:
			div = a / b
		except ZeroDivisionError:
			div = float('inf')
		return div
		#This function allows you to divide
print("Welcome to Python Calculator by 3DDI3")
while True:
	print("Select Operation.")
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Quit")

	choice = input("Enter choice 1/2/3/4/5: ")

	z = int(input("Enter first number: "))
	y = int(input("Enter second number: "))

	if choice == '1':
		print(z,"+",y,"=", calculator.addition(z,y))
	elif choice == '2':
		print(z,'-',y,'=', calculator.subtraction(z,y))
	elif choice == '3':
		print(z,'*',y,'=', calculator.multiplication(z,y))
	elif choice == '4':
		print(z,'/',y,'=', calculator.division(z,y))
	elif choice == "5" :
		print("Goodbye")
		break
	else:
		print("INVALID INPUT")
		continue
	calc_again = input("Do you want to calculate again? "+"Please type Y for YES or N for NO.")
	if calc_again == "Y" or calc_again == "y" or calc_again == "YES" or calc_again == "yes":
		continue
	elif calc_again == "N" or calc_again == "n" or calc_again == "NO" or calc_again == "no":
		print("Goodbye")
		break

