# This class runs the first step of the game which prompts the user to either
# play in test mode or game mode before it begins

class Words:
    def startGame():
        print("++\n++ The great guessing game\n++\n")
        mode = str(input("Type 't' for test mode or 'p' for play mode: ")) # Prompts user input

        # Prompts User to retry until program reads a valid input
        gameStart = False
        while not gameStart:
            if mode == 't' or mode == 'p':
                gameStart = True
            else:
                mode = str(input("Please try again: "))
        return mode # returns either 'p' for play mode or 't' for test mode

    if __name__ == "__startGame__":
        startGame()
