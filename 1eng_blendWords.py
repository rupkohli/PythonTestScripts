#program to print the blend words
#playing with lists
#adding a new value in the list


import sys

blBlend = ['black', 'blue', 'blend', 'blow', 'blink', 'bless', 'blood']
chBlend = ['chair', 'chess', 'chest', 'cheek', 'chips', 'chill', 'chalk', 'choice', 'champ', 'chug']
drBlend = ['dress', 'draw', 'drink', 'drill', 'drum', 'drown', 'drake']
shBlend = ['ship', 'sharp', 'shit', 'shirt', 'shrimp', 'shine', 'shop', 'shh', 'shampoo']
stBlend = ['stop', 'stomp', 'start', 'still', 'stick', 'stone', 'star', 'stool', 'stress']

play = 1

print ("let's play the blend words challenge")

	
while (play):
	print ("Choose blend word family - bl, ch, dr, sh, st")
	playBlend = input()

	print("Showing blend words for blend family " + playBlend)

	if playBlend == 'bl':
		count = int(0)
		for count in range(len(blBlend)):
			print(str(count) + " - " + str(blBlend[count]))
			print()


	elif playBlend == 'ch':
		count = int(0)
		for count in range(len(chBlend)):
			print(str(count) + " - " + str(chBlend[count]))
			print()
	
	elif playBlend == 'dr':
		count = int(0)
		for count in range(len(drBlend)):
			print(str(count) + " - " + str(drBlend[count]))
			print()
	
	elif playBlend == 'sh':
		count = int(0)
		for count in range(len(shBlend)):
			print(str(count) + " - " + str(shBlend[count]))
			print()
	
	elif playBlend == 'st':
		count = int(0)
		for count in range(len(stBlend)):
			print(str(count) + " - " + str(stBlend[count]))
			print()
	
	print ("Add more blend words? Enter 9 else press the <return> key")
	
	addMoreBlendWords = input()

	print ("Enter more blend words for blend family  " + str(playBlend))
	
	while (addMoreBlendWords):
		addMoreWords = input()
		#print ("word added")

		if playBlend == 'bl':
			blBlend = blBlend + [addMoreWords]
		elif playBlend == 'ch':
			chBlend = chBlend + [addMoreWords]
		elif playBlend == 'dr':
			drBlend = drBlend + [addMoreWords]
		elif playBlend == 'sh':
			shBlend = shBlend + [addMoreWords]
		elif playBlend == 'st':
			stBlend = stBlend + [addMoreWords]
			
		print ("Add another blend word for " + playBlend + "? Enter word else press the <return> key")
		addMoreBlendWords = input()
		#print("yes add word")
		
	print ("Play again? Enter 1 else press the <return> key to exit game")
	play = input()
	#print (play)

	

	

