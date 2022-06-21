from asyncio.windows_events import INFINITE
import copy


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

    def getGuanyador(self):
        if(self.players[0].wins > self.players[1].wins): return self.players[0]
        return self.players[1]

    def __str__(self):
        return '\n'.join(map(str, self.board))

    def __repr__(self):
        return '\n'.join(map(str, self.board))




def miniMax (taulell):
    global OtotalWins
    global StotalWins
    print(taulell)
    taulell.getPuntuacioPartida()
    print("------------------------")

    if(len(taulell.getCasellesBuides())==0): #Si s'ha acabat el taulell
        guanyador = taulell.getGuanyador()
        if(guanyador.name == "O"):
            OtotalWins +=1
        else:
            StotalWins +=1
        # return taulell.getPuntuacioTotal()  #Printejem las puntuacions
        return

    casellesBuides = taulell.getCasellesBuides()
    placeholder = 0 #Valor placeholder de punts
    nextCasella = {} #variable que ens indicara la proxima casella

    if (str(taulell.actualPlayer) == "O"): #Fem que O sigui max
        for casella in casellesBuides:      #Mirem totes les caselles buides
            puntuacio = taulell.marcarCasella(casella[0],casella[1]) #Mirem els punts que ens donaria esa casella
            if( puntuacio >= placeholder):    #Si esa casella ens dona mes punts que el que tenim en el placeholder
                placeholder = puntuacio  #actualitzem camps
                nextCasella[tuple(casella)] = placeholder
            
            taulell.buidarCasella(casella[0],casella[1])    #marquem com a buida sempre, perque sempre visitem (es la condicio del if)

        highest = max(nextCasella.values())
        allPossibleCasellas = [k for k, v in nextCasella.items() if v == highest]
            # print( allPossibleCasellas)

       
        for crisella in allPossibleCasellas:
            taulell2 = copy.deepcopy(taulell)
            taulell2.marcarCasella(crisella[0],crisella[1])    #tornem a marcar sol la casella que ens interessa
            taulell2.actualPlayer.win(placeholder)   #Indiquem els punts que ha guanyat amb aquesta jugada
            taulell2.changePlayer()  #Cambiem de jugador
            miniMax(taulell2)

    else:   #Exactament el mateix, sol que la condicio es <= (busquem que doni els menors punts possibles)
        placeholder= 0  #Donat que busquem el minim, el placeholder el fiquem al maxim
        for casella in casellesBuides:
            puntuacio = taulell.marcarCasella(casella[0],casella[1])
            if(puntuacio >= placeholder):
                placeholder = puntuacio  #actualitzem camps
                nextCasella[tuple(casella)] = placeholder
            
            taulell.buidarCasella(casella[0],casella[1])    #marquem com a buida sempre, perque sempre visitem (es la condicio del if)

        highest = max(nextCasella.values())
        allPossibleCasellas = [k for k, v in nextCasella.items() if v == highest]
            # print( allPossibleCasellas)


        for crisella in allPossibleCasellas:
            taulell2 = copy.deepcopy(taulell)
            taulell2.marcarCasella(crisella[0],crisella[1])    #tornem a marcar sol la casella que ens interessa
            taulell2.actualPlayer.win(placeholder)   #Indiquem els punts que ha guanyat amb aquesta jugada
            taulell2.changePlayer()  #Cambiem de jugador
            miniMax(taulell2)




OtotalWins=0
StotalWins=0
player1 = Jugador("O")
player2 = Jugador("S")
totalPlayers = [player1, player2]

taulellOriginal = Taulell(totalPlayers)


miniMax(taulellOriginal)

# totalPlayersGame2 = [player2, player1]
# taulell2Game = Taulell(totalPlayersGame2)

# miniMax(taulell2Game)
print("Tenim 2 jugadors MAX, tot i que indiquem com a MAX el jugador O (perque es el que comença)")
print("Tot i així, indiquem al jugador S com a MIN (tot i buscar també max) ")
print("Començant amb moviment del jugador O (MAX): ")
print("\t O (jugador MAX) guanya "+ str(round(OtotalWins/(OtotalWins+StotalWins)* 100,2))+" % dels cops (" +str(OtotalWins)+")")
print("\t S (jugador 'MIN') guanya "+ str(round(StotalWins/(OtotalWins+StotalWins)* 100,2))+" % dels cops (" +str(StotalWins)+")" )
