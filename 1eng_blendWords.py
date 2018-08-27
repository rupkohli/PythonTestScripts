#program to print the blend words
#playing with lists
#adding a new value in the list


import sys
# import json

blBlend = ['black', 'blue', 'blend', 'blow', 'blink', 'bless', 'blood']
chBlend = ['chair', 'chess', 'chest', 'cheek', 'chips', 'chill', 'chalk', 'choice', 'champ', 'chug']
drBlend = ['dress', 'draw', 'drink', 'drill', 'drum', 'drown', 'drake']
shBlend = ['ship', 'sharp', 'shit', 'shirt', 'shrimp', 'shine', 'shop', 'shh', 'shampoo']
stBlend = ['stop', 'stomp', 'start', 'still', 'stick', 'stone', 'star', 'stool', 'stress']

# #JSON BLOCKS OF BLEND WORDS
# blendBL = {
#    "blBlend": [
#       {
#          "1": "black",
#          "2": "blue",
#          "3": "blend",
#          "4": "blow",
#          "5": "blink",
#          "6": "bless",
#          "7": "blood"
#       }
#    ]
# }

# blendCH = {
#    "chBlend": [
#       {
#          "1": "chair",
#          "2": "chess",
#          "3": "chest",
#          "4": "cheek",
#          "5": "chips",
#          "6": "chill",
#          "7": "chalk",
#          "8": "choice",
#          "9": "champ",
#          "10": "chug"
#       }
#    ]
# }

# blendDR = {"drBlend": [{1:'dress', 2:'draw', 3:'drink', 4:'drill', 5:'drum', 6:'drown', 7:'drake'}]}

# blendSH = {"shBlend": [{1:'ship', 2:'sharp', 3:'shit', 4:'shirt', 5:'shrimp', 6:'shine', 7:'shop', 8:'shh', 9:'shampoo'}]}

# blendST = {"stBlend": [{1:'stop', 2:'stomp', 3:'start', 4:'still', 5:'stick', 6:'stone', 7:'star', 8:'stool', 9:'stress'}]}


# ######################
# #
# # Blend words using JSON
# #
# ######################

# pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
# stringOfJsonData = json.dumps(blendCH)
# print("blendCH \n", stringOfJsonData)


######################
######################
#
# Blend words - array based
#
######################
######################
def arrPlayBlends:
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

		print ("Enter more blend words for blend family  " + str(playBlend.upper()))
		addMoreWords = input()
			
		while (addMoreWords):
			print ("word added", addMoreWords[0:2])

			if playBlend == 'bl':
				if addMoreWords[0:2] == "bl":
					blBlend = blBlend + [addMoreWords]
				else:
					print ("Not a valid ", playBlend.upper(), "blended word.\n")
			elif playBlend == 'ch':
				chBlend = chBlend + [addMoreWords]
			elif playBlend == 'dr':
				drBlend = drBlend + [addMoreWords]
			elif playBlend == 'sh':
				shBlend = shBlend + [addMoreWords]
			elif playBlend == 'st':
				stBlend = stBlend + [addMoreWords]
				
			print ("Add another blend word for " + playBlend.upper() + "? Enter word else press the <return> key")
			addMoreWords = input()
			
			
		print ("Play again? Enter 1 else press the <return> key to exit game")
		play = input()
		#print (play)

###################
#
# Play blends using an array
#
###################
arrPlayBlends()

print ("See you again")


	

