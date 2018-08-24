###############################
#
# MATHS FUN
#
# Rupinder Kohli - 23 Aug 2018
#
# For Kirat
###############################
import sys
import traceback
import random


global numList

###############################
#
# Arrange numbers in order
#
###############################
def orderInc():
	#print ("enter a list of numbers and i will arrange them in increasing order")
	numList = []
	numb = 1
	while numb != 0:
		numb = input()
		numb = int(numb)
		if numb != 0:
			 numList = numList + [numb]

	
	numList.sort()

	print("arranging numbers in increasing order")
	print (numList)	

	print("Are the numbers shown correctly in increasing order(Y / N) ?")
	ans = input()
	if ans == 'Y' or ans == 'y':
		print("Bravo") 
	else: 
		print("Wrong answer computer ji\n")


	numList.sort(reverse=True)

	print("arranging numbers in decreasing order")
	print (numList)	

	print("Are the numbers shown correctly in decreasing order(Y / N) ?")
	ans = input()
	if ans == 'Y' or ans == 'y':
		print("Bravo") 
	else: 
		print("Wrong answer computer ji\n")

	#print (len(numList))
	

###############################
#
#Adding 2 single digit numbers
#
###############################
def singleDigitAdd():
	
	print ("Add the following numbers")

	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)
	print(str(num1) , " + ", str(num2), " = ")
	
	sumNum = num1 + num2
	
	getSum = input()

	while  int(getSum) != int(sumNum):
		print ("Try again ")
		getSum = input()
	
	print ("Correct answer\n")

###############################
#
#Working with number stories
#
###############################
def numberStoriesAdd():
	storiesStart = ['Jane has',
	 'Mary ate ',
	 'Tim has',
	 'I have',
	 'Kartik has',
	 'Pam has',
	 'Susan has',
	 'Chitra has',
	 'Tom has']
	
	objects = ['Idlies', 
	'cookies',
	'apples',
	'walnuts',
	'balls',
	'cake slices',
	'mathis']

	storiesPreEnd = "How many"  
	storiesEnd = "do I have in all?"  
	
	quesBeg = storiesStart[random.randint(0, len(storiesStart) - 1)]
	quesObj = objects[random.randint(0, len(objects) - 1)]

	
	num1 = random.randint(1, 9)
	num2 = random.randint(1, 9)
	

	print (quesBeg , str(num1), quesObj,". I bought",
	str(num2), "more", storiesPreEnd, quesObj, storiesEnd, "\n")

	print(str(num1) , " + ", str(num2), " = ")
	
	sumNum = num1 + num2
	print("    ")
	getSum = input()

	while  int(getSum) != int(sumNum):
		print ("Try again ")
		getSum = input()
	
	print ("Correct answer!!\n")

###############################
#
#Working with 2-digit addition
#
###############################

def doubleDigitAdd():

	print ("Add the following numbers")

	num1 = random.randint(0, 99)
	num2 = random.randint(0, 99)
	if num1 < 10:
		print("   ", str(num2) , "\n + ", str(num1), "\n", "-"*5)
	else:
		print("   ", str(num1) , "\n + ", str(num2), "\n", "-"*5)
	
	sumNum = num1 + num2
	
	getSum = input()

	while  int(getSum) != int(sumNum):
		print ("Try again ")
		getSum = input()
	
	print ("Correct answer!!\n")

#######################
#
#MAIN CODE
#
#######################
# print("Lets check your addition")


print ("Maths Fun\n")

playMath = 1
while(playMath):

	print ("Select option to play -\n1. Arrange numbers in Order\n2. Addition Level I - Simple Addition\n3. Addition Level II - Number stories\n4. Addition Level III - 2 Digit Addition\n")
	mathFunX = input()

	if mathFunX == '1':
		playAdd = 1
		print ("Lets arrange the numbers in order - hold your breath and think of a few numbers, end list with 0\n")
		while (playAdd):
			orderInc()

			print ("Play again? Enter 1 else press the <return> key to exit level")
			playAdd = input()

	elif mathFunX == '2':

		playAdd = 1
		print ("Addition Level I - Simple Addition")

		while (playAdd):
			singleDigitAdd()

			print ("Play again? Enter 1 else press the <return> key to exit level")
			playAdd = input()

	elif mathFunX == '3':

		playAdd = 1
		print ("Addition Level II - Number stories")
		while (playAdd):
			numberStoriesAdd()

			print ("Play again? Enter 1 else press the <return> key to exit level")
			playAdd = input()

	elif mathFunX == '4':

		playAdd = 1
		print ("Addition Level III - 2 Digit Addition")
		while (playAdd):
			doubleDigitAdd()

			print ("Play again? Enter 1 else press the <return> key to exit level")
			playAdd = input()

	print("Do you want to play MATHS FUN again (1/0)?")
	playMath = input()

