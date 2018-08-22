#program to write numbers in expanded format

def expFormat():
	print ("enter a 2-digit number and I will print the number in expanded format")

	two_digit = input()

	print ("You entered " + two_digit)


	numExpandOnes = int(two_digit) % 10
	numExpandTens = int(two_digit) // 10

	print (" ")
	print("expanded form of " + str(two_digit) + " = " + str(numExpandTens) + " Tens and " + str(numExpandOnes) + " Ones")
	print (" ")
	

print("you want to play expanded format number game (1/0)")
print (" ")
	
moreExpForm = input()

while int(moreExpForm) == 1:
	expFormat()
	
	print("you want to play expanded format number game (1/0)")
	moreExpForm = input()
	if int(moreExpForm) != 1 :
		print ("see you again")
		break




