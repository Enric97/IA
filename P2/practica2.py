# import chess;
import re


class Casella:
    def __init__(self, fila, columna):
        self.childs = {}
        self.fila = fila
        self.columna = columna
        self.name = fila+columna
        self.isVisited = False

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna
    
    def getVisited(self):
        return self.isVisited

    def visit(self):
        self.isVisited = True

    def unvisit(self):
        self.isVisited = False

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
    print("La casella origen es: ", origen)

    possiblesPosicions += calculNovesCeles(origen, 1, 2)
    possiblesPosicions += calculNovesCeles(origen, 2, 1)

    possiblesPosicions = validarPosicions(possiblesPosicions)
    print("Les possibles destinacions son: ", possiblesPosicions)
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
    return validSolutions

# ----------


def recursivity(NomCasella):
    global solution
    casella = board.getCasella(NomCasella)
    checkingMoves = []
    checkingMoves = KnightMouCasella(board.getCasella(casella))

    if(board.checkAllVisited()):
        return solution
    
    if(casella.getVisited()):
        return
    
    casella.visit()

    for move in checkingMoves:
        solution.append(move)
        recursivity(move)
        solution.pop(-1)


    

solution = []



# Create board
board = Board()
createCasellas(board)

print(board)

# KnightMouCasella(board.getCasella("C8"))

recursivity("E8")

print(solution)
