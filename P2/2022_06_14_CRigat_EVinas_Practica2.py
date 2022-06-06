# import chess;
import re
import copy


class Casella:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.name = fila+columna
        self.isVisited = False
        # self.pos = -1

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna
    
    def getVisited(self):
        return self.isVisited
    
    # def getPos(self):
    #     return self.pos
    
    def visit(self):
        self.isVisited = True

    def unvisit(self):
        self.isVisited = False

    # def setPos(self, pos):
    #     self.pos=pos

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Board:
    # board = []
    def __init__(self):
        self.board = []

    def append(self, fila):
        self.board.append(fila)

    def getCasella(self, casella):
        for i in self.board:
            # print(i)
            for y in i:
                # print(str(y))
                if(str(y) == casella):
                    return y
        return "No existeix la casella"

    def checkAllVisited(self):
        for i in self.board:
            for y in i:
                if (not y.getVisited()): 
                    return False
        return True
    
    def getBoard(self):
        casellas = []
        for i in self.board:
            for y in i:
                casellas.append(y)
        return casellas

    def visitCasella(self, casella):
        self.getCasella(casella).visit()

    def unvisitCasella(self, casella):
        self.getCasella(casella).unvisit()


    def __str__(self):  # Per printear be
        return '\n'.join(map(str, self.board))

    def __repr__(self):
        return '\n'.join(map(str, self.board))

# Creacio de les caselles i afegim a Board
def createCasellas(board):

    leters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]

    fila = []

    for i in numbers:
        for y in leters:
            fila.append(Casella(y, i))
        board.append(fila)
        fila = []

# Metode principal per determinar posibles ubicacions a moure a partir d'una cela concreta
def KnightMouCasella(origen):

    possiblesPosicions = []
    # print("La casella origen es: ", origen)

    possiblesPosicions += calculNovesCeles(origen, 1, 2)
    possiblesPosicions += calculNovesCeles(origen, 2, 1)

    possiblesPosicions = validarPosicions(possiblesPosicions)
    # print("Les possibles destinacions son: ", possiblesPosicions)
    return possiblesPosicions

# Subfuncio del anterior. Donat unes coordenades i variança, calcula totes les cel.les possibles en ese marge
def calculNovesCeles(origen, fila, columna):
    novesFiles = []
    novesColumnes = []
    possiblesPosicions = []

    novesFiles.append(chr(ord(origen.getFila()) + fila))
    novesFiles.append(chr(ord(origen.getFila()) - fila))
    novesColumnes.append(chr(ord(origen.getColumna()) + columna))
    novesColumnes.append(chr(ord(origen.getColumna()) - columna))

    for i in novesFiles:
        for y in novesColumnes:
            possiblesPosicions.append(i+y)

    return possiblesPosicions

# Donat un conjunt de cel.les, validem que realment existeixen en el taulell
def validarPosicions(possiblesPosicions):
    validSolutions = []
    for i in possiblesPosicions:
        validSolutions += re.findall("[A-H][1-8]", i)
    

    # Opcional, ja es checkea en el recursive
    # for i in validSolutions:
    #     if(board.getCasella(i).getVisited()):
    #          validSolutions.remove(i)

    return validSolutions

# ----------


def recursivity(NomCasella):
    global solution
    # global pos
    # print(solution) # NOTA: ACTIVAR PER VEURE EL PROGRÉS DELS CAMINS ESCOLLITS
    casella = board.getCasella(NomCasella)
    # checkingMoves = []
    

    if(board.checkAllVisited()):
        return solution
 
    if(casella.getVisited()):
        return
    
    checkingMoves = KnightMouCasella(casella)

    casella.visit()
    # pos=pos+1
    # casella.setPos(pos)

    for move in checkingMoves:
        solution.append(move)
        recursivity(move)
        solution.pop(-1)
        Visit(solution)

#Metode que marca com a visitats les caselles que enviem per la llista
#Relacionat amb el metode anterior
def Visit(list):
    copyList = []
    copyList = copy.copy(board.getBoard())
    # print(copyList)
    for casella in list:
        # print(casella)
        # board.visitCasella(casella)
        copyList.remove(board.getCasella(casella))
    Unvisit(copyList)

#Metode que marca com a no visitats les caselles que arriben per una llista
#També relacionat amb el metode recursiu
def Unvisit(list):
    for casella in list:
        casella.unvisit()



pos = 0

# Solucio
solution = []

# Create board
board = Board()
createCasellas(board)

print(board)

# print(KnightMouCasella(board.getCasella("E4")))
# board.getCasella("A8").setPos(0)

inici = input("En quina cel.la vol iniciar el recorregut? (des de A1 fins E8)\n\t")

while not re.match("[A-H][1-8]", inici):
    print ("Entrada incorrecta.\n")
    inici = input("En quina cel.la vols iniciar el recorregut? (des de A1 fins E8)\n\t")

solution.append(inici)
recursivity(inici)
print(solution)
    

