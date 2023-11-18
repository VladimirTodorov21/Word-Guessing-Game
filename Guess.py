# This program runs 4 source files that contribute to running a guessing game program. This file is the main file
# that imports the other 3 files and is responsible for the user interface, semantics and game logic. The code prompts
# the user to guess the word, guess a letter, give up and be told what the word is or quit the application in which a
# game report will be shown for all the games played

class Guess:
    def main():
        # import created classes with methods
        import StringDatabase
        import Game
        import Words

        # import python pre-defined classes and methods
        import msvcrt
        import os

        # Variables initialized and are used for the Game Report at the end of the program once the user quits
        game = 0
        CurrentWord = StringDatabase.StringDatabase.WordFile()
        status = ""
        badGuesses = 0
        missedLetters = 4
        score = 0
        finalScore = 0
        
        # Dictionary containing the point values for all letters
        frequencies = {"a":8.17, "b":1.49, "c":2.78, "d":4.25, "e":12.70, "f":2.23, "g":2.02, "h":6.09, "i":6.97, "j":0.15, "k":0.77,
                       "l":4.03, "m":2.41, "n":6.75, "o":7.51, "p":1.93, "q":0.10, "r":5.99, "s":6.33, "t":9.06, "u":2.76, "v":0.98,
                       "w":2.36, "x":0.15, "y":1.97, "z":0.07}
        
        # Lists used to store the Game Report Variables
        currentGame = []
        entireGame = []

        # Loop conditional and initialized starting variables for the guessing game
        gameContinue = True
        LettersGuessed = "Letters Guessed"
        CurrentGuess = ["_","_","_","_"]

        # Calls function from Game class to either play in test mode or play mode
        mode = Words.Words.startGame()

        # Main Game
        while gameContinue:
            # Clears the output screen each the the entire loop is re-executed
            os.system('clear')

            print("++\n++ The great guessing game\n++\n")

            # Only if game is in test mode will the UI display what the current randomized word is
            if mode == "t":
                print("Current Word: " + CurrentWord)
            print("Current Guess:  " + CurrentGuess[0] + CurrentGuess[1] + CurrentGuess[2] + CurrentGuess[3])
            print(LettersGuessed)
            print("\ng = guess, t = tell me, l for a letter, and q to quit\n")

            # Prompts user for input
            option = str(input('Enter Option: '))

            # Prompts user to retry until the program receives a valid input
            correctOption = False
            while not correctOption:
                if option == 'g' or option == 't' or option == 'l' or option == 'q':
                    correctOption = True
                else:
                    option = str(input("Invalid option. Please re-enter: "))
            
            # Option for guessing the word
            if option == 'g':
                guess = str(input("\nMake your guess: ")) # User input
                if guess.lower() == CurrentWord.lower(): # case insensitive result is compared to the word
                    print("\n@@\n@@ FEEDBACK: You're right, Einstein!\n@@")

                    game += 1
                    status = "Success"

                    # Determines the score based on the letters the word contains
                    for B in range(0,4):
                        for C in range(0,26):
                            if CurrentWord[B] == list(frequencies)[C]:
                                score += list(frequencies.values())[C]
                
                    #Each Bad Guess will remove 10% of the final result
                    if badGuesses >= 1:
                        score = score*(1-(badGuesses*0.10))

                    finalScore += score # Final Score keeps growing

                    # Store all Game report variables in the list and call the function from Game to put
                    # that list into another list (nested list)
                    currentGame = [game,CurrentWord,status,badGuesses,missedLetters,round(score,2)]
                    Game.Game.storeCurrentGame(currentGame, entireGame)

                    # New word is randomized after player guesses correctly
                    CurrentWord = StringDatabase.StringDatabase.WordFile()

                    # Game Report Variables initialized
                    CurrentGuess = ["_","_","_","_"]
                    LettersGuessed = "Letters Guessed"
                    badGuesses = 0
                    missedLetters = 4
                    score = 0
                    
                    print("\n\nPress any key to Continue...")
                    msvcrt.getch()
                else:
                    badGuesses += 1

                    print("\n@@\n@@ FEEDBACK: Try again, Loser!\n@@")
                    print("\n\nPress any key to Continue...")
                    msvcrt.getch()

            # Option for program to tell user the word
            elif option == 't':
                print("\n@@\n@@ FEEDBACK: You really should have guessed this... '" + CurrentWord + "'\n@@")

                game += 1
                status = "Gave up"

                # Determine the score based on the missing letters that have not been found (resulting in negative score)
                # and add to that score the letters found from guessing a letter correctly (positive)
                for D in range(0,4):
                    for E in range(0,26):
                        if CurrentWord[D] == list(frequencies)[E]:
                            score -= list(frequencies.values())[E]
                        if CurrentGuess[D] == list(frequencies)[E]:
                            score += list(frequencies.values())[E]

                finalScore += score # Final Score keeps growing

                # Store all Game report variables in the list and call the function from Game to put
                # that list into another list (nested list)
                currentGame = [game,CurrentWord,status,badGuesses,missedLetters,round(score,2)]
                Game.Game.storeCurrentGame(currentGame, entireGame)

                # New word is randomized after player guesses correctly
                CurrentWord = StringDatabase.StringDatabase.WordFile()

                # Game Report Variables initialized
                CurrentGuess = ["_","_","_","_"]
                LettersGuessed = "Letters Guessed"
                badGuesses = 0
                missedLetters = 4
                score = 0

                print("\n\nPress any key to Continue...")
                msvcrt.getch()

            # Option for guessing a letter
            elif option == 'l':
                letterGuess = str(input("\nEnter a letter: ")) # User Input
                LettersGuessed += ' ' + letterGuess # String for attempts for guessing letters is updated

                # Loop looks through the word if input corresponds to one of the letters in the word
                feedBack = True
                for A in range(0,4):
                    if letterGuess == CurrentWord[A:A+1]:
                        CurrentGuess[A] = letterGuess
                        missedLetters -= 1

                        print("\n@@\n@@ FEEDBACK: Woo hoo, you found 1 letter\n@@")
                        print("\n\nPress any key to Continue...")
                        msvcrt.getch()
                        feedBack = False
        
                # No letters in the word are found
                if feedBack == True:
                    print("\n@@\n@@ FEEDBACK: Not a single match, genius\n@@")
                    print("\n\nPress any key to Continue...")
                    msvcrt.getch()

            # Option to quit
            elif option == 'q':
                os.system('clear')
                print("++\n++ Game Report\n++\n")
                print("%0s%10s%12s%15s%18s%8s" % ("Game","Word","Status","Bad Guesses","Missed Letters","Score"))
                print("%0s%10s%12s%15s%18s%8s" % ("----","----","------","-----------","--------------","-----"))
                
                # Prints the content of all lists within the list from the Game class
                # and prints nothing even if user has not completed a single game
                if game >= 1:
                    Game.Game.printGameReport(game, entireGame)

                print("\nFinal Score: %.2f" % (finalScore))
                gameContinue = False # Exit loop and Program has terminated

    if __name__ == "__main__":
        main()
