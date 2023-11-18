# This class adds a list from the parameter of its function into another list (nested list)
# and its other function prints the content of that new big list

class Game:
    def storeCurrentGame(currentGame, entireGame):
        entireGame.append(currentGame) #stores list within list
        return entireGame
    
    def printGameReport(game, entireGame):
        # Prints the content of the list based on the games completed
        for H in range(0,game):
            print("%0d%13s%13s%4d%15d%21.2f" % (entireGame[H][0],entireGame[H][1],entireGame[H][2],entireGame[H][3],entireGame[H][4],entireGame[H][5]))

    if __name__ == "__storeCurrentGame__":
        storeCurrentGame()

    if __name__ == "__printGameReport__":
        printGameReport()
