from dto import Game, Deck, Card, Player

def main():
    myGame = Game.Game()
    myGame.addPlayer(500)
    gamenum = 1
    cont = True
    while cont:
        print("Starting Game #{}".format(str(gamenum)))
        myGame.playHand()
        ++gamenum
        if input("Continue?").upper() in ["NO","N","QUIT","EXIT"]:
            cont = False

if __name__ == "__main__":
    main()

