

class Jugador:

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def win(self):
        self.wins += 1

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Casella:

    def __init__(self):
        self.player = "Empty"

    def marcarCasella(self, jugador):
        self.player = jugador

    def reiniciarCasella(self):
        self.player = "Empty"

    def __str__(self):
        return str(self.player)

    def __repr__(self):
        return str(self.player)


class Taulell:

    def __init__(self):
        self.board = []
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

    def buidarCasella(self, fila, columna):
        self.board[fila][columna].reiniciarCasella()

    def marcarCasella(self, fila, columna, player):
        self.board[fila][columna].marcarCasella(player)

    def checkBoardBasedOnLastMove(self, fila, columna):
        jugador = self.board[fila][columna].player
        casellesPerVisitar = []
        # S'ha de posar +2 perque no inclou el final
        for filaActual in range(fila-1, fila+2):
            if(filaActual in range(0, 3)):  # Comprovem que es una fila valida
                for columnaActual in range(columna-1, columna+2):
                    if(columnaActual in range(0, 3)):  # Comprovem que es una columna valida
                        casellesPerVisitar.append([filaActual, columnaActual])

        casellesPerVisitar.remove([fila, columna]) #Eliminem la casella desde la que partim
        # print(casellesPerVisitar)
        self.checkCasella(jugador, casellesPerVisitar)

    def checkCasella(self, jugador, caselles):
        player = ""
        for casella in caselles:    #Mirem totes les caselles
            player = self.board[casella[0]][casella[1]].player     #Mirem quin jugador a marcat la casella
            if((player != "Empty") & (player is not jugador.name)):      #si el que ha marcat la casella es diferent a ell mateix i no es empty, li sumem un punt
                jugador.win()


    def __str__(self):
        return '\n'.join(map(str, self.board))

    def __repr__(self):
        return '\n'.join(map(str, self.board))


taulell = Taulell()
player1 = Jugador("O")
player2 = Jugador("S")
# taulell.marcarCasella(0, 1, player2)
# print(taulell)
taulell.marcarCasella(0,1,player1)
taulell.marcarCasella(2,1,player1)
taulell.marcarCasella(1,1,player2)
taulell.checkBoardBasedOnLastMove(1,1)
print(player2.wins)
