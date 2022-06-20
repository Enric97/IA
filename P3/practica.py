

from asyncio.windows_events import INFINITE


class Jugador:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.winGames = 0

    def win(self, number=1):
        self.wins += number

    def resetWins(self):
        self.wins = 0

    def winGame(self):
        self.winGames +=1

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def puntuació(self):
        return str("El jugador "+self.name+ " té "+ str(self.winGames)+ " partides guanyades")

class Casella:

    def __init__(self):
        self.player = "-"

    def marcarCasella(self, jugador):
        self.player = jugador

    def reiniciarCasella(self):
        self.player = "-"

    def __str__(self):
        return str(self.player)

    def __repr__(self):
        return str(self.player)


class Taulell:

    def __init__(self, totalPlayers):
        self.board = []
        self.players = totalPlayers
        self.actualPlayer = self.players.pop(0)
        self.players.append(self.actualPlayer)
        self.createBoard()


    def createBoard(self):  # Files i columnes modificables
        filesTotals = 3
        columnesTotals = 3
        fila = []

        for i in range(filesTotals):
            for y in range(columnesTotals):
                fila.append(Casella())
            self.board.append(fila)
            fila = []

    def getCasellesBuides(self):
        caselles = []

        for i in range (3):
            for y in range (3):
                if(self.board[i][y].player== "-"): # o str(self.board[i][y])
                    caselles.append([i,y])

        return caselles

    def buidarCasella(self, fila, columna):
        self.board[fila][columna].reiniciarCasella()

    def marcarCasella(self, fila, columna):
        self.board[fila][columna].marcarCasella(self.actualPlayer)
        return self.checkBoardBasedOnLastMove(fila,columna)
        
    def checkBoardBasedOnLastMove(self, fila, columna):
        # jugador = self.board[fila][columna].player
        # jugador = self.actualPlayer
        casellesPerVisitar = []
        # S'ha de posar +2 perque no inclou el final
        for filaActual in range(fila-1, fila+2):
            if(filaActual in range(0, 3)):  # Comprovem que es una fila valida
                for columnaActual in range(columna-1, columna+2):
                    if(columnaActual in range(0, 3)):  # Comprovem que es una columna valida
                        casellesPerVisitar.append([filaActual, columnaActual])

        casellesPerVisitar.remove([fila, columna]) #Eliminem la casella desde la que partim
        # print(casellesPerVisitar)
        return self.getQuantitatPunts(casellesPerVisitar, fila, columna)

    def getQuantitatPunts(self, caselles, filaOrigen, columnaOrigen):
        jugador = self.actualPlayer
        punts = 0

        if(self.actualPlayer.name=="O"):
            for casella in caselles:    
                # print("Fila: ",casella[0])
                # print("Columna: ",casella[1])
                # print((casella[0]==filaOrigen) & (casella[1] == (columnaOrigen+1)))
                if(((casella[0]==(filaOrigen+1)) & (columnaOrigen==casella[1]))
                    | ((casella[0]==filaOrigen) & (casella[1] == (columnaOrigen+1)))
                    | ((casella[0]==(filaOrigen+1)) & (casella[1]==(columnaOrigen+1)))
                    | ((casella[0]==(filaOrigen-1)) & (casella[1]== (columnaOrigen+1)))):

                    player = self.board[casella[0]][casella[1]].player  
                    if((player != "-") & (player is not jugador)):      
                        punts +=1


        else:
            for casella in caselles:    #Mirem totes les caselles
                if(((casella[0]==filaOrigen-1) & (columnaOrigen==casella[1]))
                    |( (casella[0]==filaOrigen) & (casella[1] == columnaOrigen-1))
                    | ((casella[0]==filaOrigen-1) & (casella[1]==columnaOrigen-1))
                    | ((casella[0]==filaOrigen+1) & (casella[1]== columnaOrigen-1))):

                    player = self.board[casella[0]][casella[1]].player  
                    if((player != "-") & (player is not jugador)):      
                        punts +=1
        return punts

    def changePlayer(self):
        self.actualPlayer = self.players.pop(0)
        self.players.append(self.actualPlayer)

    def getPuntuacioTotal(self):
        for player in self.players:
            print(player.puntuació())
    
    def getPuntuacioPartida(self):
        for player in self.players:
            print ("El jugador "+str(player)+" porta "+str(player.wins)+ " punts")

    def __str__(self):
        return '\n'.join(map(str, self.board))

    def __repr__(self):
        return '\n'.join(map(str, self.board))




def miniMax (taulell):
    print(taulell)
    taulell.getPuntuacioPartida()
    print("------------------------")

    if(len(taulell.getCasellesBuides())==0): #Si s'ha acabat el taulell
        if(taulell.players[0].wins > taulell.players[1].wins): #Puntuem al jugador amb mes wins
            taulell.players[0].winGame()
        else:
            taulell.players[1].winGame()
        return taulell.getPuntuacioTotal()  #Printejem las puntuacions

    casellesBuides = taulell.getCasellesBuides()
    placeholder = 0 #Valor placeholder de punts
    nextCasella = None  #variable que ens indicara la proxima casella

    if (str(taulell.actualPlayer) == "O"): #Fem que O sigui max
        for casella in casellesBuides:      #Mirem totes les caselles buides
            if(taulell.marcarCasella(casella[0],casella[1]) >= placeholder):    #Si esa casella ens dona mes punts que el que tenim en el placeholder
                placeholder = taulell.marcarCasella(casella[0],casella[1])  #actualitzem camps
                nextCasella = casella
            taulell.buidarCasella(casella[0],casella[1])    #marquem com a buida sempre, perque sempre visitem (es la condicio del if)

        taulell.marcarCasella(nextCasella[0],nextCasella[1])    #tornem a marcar sol la casella que ens interessa
        taulell.actualPlayer.win(placeholder)   #Indiquem els punts que ha guanyat amb aquesta jugada
        taulell.changePlayer()  #Cambiem de jugador
        return miniMax(taulell)

    else:   #Exactament el mateix, sol que la condicio es <= (busquem que doni els menors punts possibles)
        placeholder= 0    #Donat que busquem el minim, el placeholder el fiquem al maxim
        for casella in casellesBuides:
            if(taulell.marcarCasella(casella[0],casella[1]) >= placeholder):
                placeholder = taulell.marcarCasella(casella[0],casella[1])
                nextCasella = casella
            taulell.buidarCasella(casella[0],casella[1])

        taulell.marcarCasella(nextCasella[0],nextCasella[1])
        taulell.actualPlayer.win(placeholder)
        taulell.changePlayer()
        return miniMax(taulell)








player1 = Jugador("O")
player2 = Jugador("S")
totalPlayers = [player1, player2]

taulell = Taulell(totalPlayers)


# taulell.marcarCasella(0,1)
# taulell.marcarCasella(2,1)
# taulell.marcarCasella(1,1)
# taulell.checkBoardBasedOnLastMove(1,1)
# taulell.getPuntuacio()
# print(taulell.getCasellesBuides())
# print(taulell)

miniMax(taulell)