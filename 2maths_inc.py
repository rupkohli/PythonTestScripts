#program to write numbers in increasing order
import sys
import random


global numList

###############################
#
#
#
###############################
def orderInc():
	#print ("enter a list of numbers and i will arrange them in increasing order")
	numList = []
	numb = 1
	while numb != "0":
		numb = input()
		numList = numList + [numb]

	
	numList.sort()

	print("arranging numbers in increasing order")
	print (numList)	

	print("Are the numbers shown correctly in increasing order(Y / N) ?")
	ans = input()
	if ans == 'Y':
		print("Bravo") 
	else: 
		print("Wrong answer computer ji\n")


	numList.sort(reverse=True)

	print("arranging numbers in decreasing order")
	print (numList)	

	print("Are the numbers shown correctly in decreasing order(Y / N) ?")
	ans = input()
	if ans == 'Y':
		print("Bravo") 
	else: 
		print("Wrong answer computer ji\n")

	#print (len(numList))
	

###############################
#
#
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
#
#
###############################
def numberStoriesAdd():
	# messages = ['It is certain',
	#  'It is decidedly so',
	#  'Yes definitely',
	#  'Reply hazy try again',
	#  'Ask again later',
	#  'Concentrate and ask again',
	#  'My reply is no',
	#  'Outlook not so good',
	#  'Very doubtful']
	# print(messages[random.randint(0, len(messages) - 1)])

	print ("Add the following numbers")

	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)
	print(str(num1) , " + ", str(num2), " = ")
	
	sumNum = num1 + num2
	
	getSum = input()

	while  int(getSum) != int(sumNum):
		print ("Try again ")
		getSum = input()
	
	print ("Correct answer!!\n")


def doubleDigitAdd():

	print ("Add the following numbers")

	num1 = random.randint(0, 99)
	num2 = random.randint(0, 99)
	print(str(num1) , " + ", str(num2), " = ")
	
	sumNum = num1 + num2
	
	getSum = input()

	while  int(getSum) != int(sumNum):
		print ("Try again ")
		getSum = input()
	
	print ("Correct answer!!\n")

# print("Lets check your addition")

playAdd = 1

print ("Maths Fun\n")

print ("Lets arrange the numbers in order - hold your breath and think of 5 numbers\n")
while (playAdd):
	orderInc()

	print ("Play again? Enter 1 else press the <return> key to exit game")
	playAdd = input()

playAdd = 1

print ("Addition Level I - Simple Addition")
while (playAdd):
	singleDigitAdd()

	print ("Play again? Enter 1 else press the <return> key to exit game")
	playAdd = input()

playAdd = 1

print ("Addition Level II - Number stories")
while (playAdd):
	numberStoriesAdd()

	print ("Play again? Enter 1 else press the <return> key to exit game")
	playAdd = input()

playAdd = 1

print ("Addition Level III - 2 Digit Addition")
while (playAdd):
	doubleDigitAdd()

	print ("Play again? Enter 1 else press the <return> key to exit game")
	playAdd = input()

