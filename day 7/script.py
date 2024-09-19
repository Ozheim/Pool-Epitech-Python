import random

with open("hangman/list.txt", "r") as file:
    listinFile= file.read()
    liste = listinFile.split()
    

with open("hangman/bestScore.txt", "r") as file:
    bestScore = file.read()
    if bestScore:
        bestScore = int(bestScore)
    else:
        bestScore = 0

def hangmanGame():
    wordChoice = random.randint(0, 10)
    finalChoice = liste[wordChoice]
    listOfLetterInWord = list(finalChoice)
    hideList = ['_'] * len(listOfLetterInWord)
    print(''.join(hideList))
    letterTried = []
    numberOfTry = 0
    
   
    while "_" in hideList and numberOfTry < 20:
        askingUser = input("Essaye une lettre : ").lower()

        if askingUser in letterTried:
            print("Oups, tu as déjà essayé cette lettre ! +3 pénalité")
            numberOfTry += 3
            continue

        letterTried.append(askingUser)
        print("Lettres essayées : ", " ".join(letterTried))

        if askingUser in listOfLetterInWord:
            print("Bien joué !")
            for i, letter in enumerate(listOfLetterInWord):
                if letter == askingUser:
                    hideList[i] = letter
            print(''.join(hideList))
        else:
            print("Non ! +3 pénalité")
            numberOfTry += 3
            print(numberOfTry)
    

    if "_" not in hideList:
        print("Félicitations, tu as gagné !")
    else:
        print("Tu as perdu, le mot était :", finalChoice)
    
    if numberOfTry < bestScore or bestScore == 0:  
        print(f"Nouveau meilleur score : {numberOfTry} essais !")
        with open("hangman/bestScore.txt", "w") as file:
            file.write(str(numberOfTry))

    else:
        print(f"Ton score : {numberOfTry}. Meilleur score actuel : {bestScore}.")


hangmanGame()





# creeer une liste des lettres déja joué et des nombres essaie a realiser 
# demander une lettre a l'utilisateur 
# boucler tant que le nibmre d'essaie est inférieur a nombre essaie defini, et que il y a pas de tirer dans hidden word
# test la lettre joué dans la lsite des lettres déja joué,
# ajouter la lettre dans la liste des lettes déja joué, 
# tester si la lettre est dans la lite vare
#boucler avec un index et une lettre sur ton vare, si la lettre est la meme que la lettre du user, hiddenword[i]= lettre joué, print que la lettre est dans le mot, print hidden word 
# else, print la lette pas la, ajouter au nombre essaie + 1 
# test si il y a des tiret dans hidden word, parti fini 

