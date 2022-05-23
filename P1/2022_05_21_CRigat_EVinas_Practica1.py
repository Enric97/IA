from asyncio.windows_events import NULL
import copy
import operator


# Clase del Node

class Node:
    def __init__(self, name):
        self.childs = {}
        self.name = name
        self.isVisited = False

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


def createTree():

    Cuina.childs.update({nA1: 1, nA3: 1.5})
    nA1.childs.update({Cuina: 1, nA2: 1.75, nA3: 0.5})
    nA2.childs.update({nA1: 1.75, nA4: 0.5})
    nA3.childs.update({Cuina: 1.5, nA1: 0.5, nA4: 1.75, nE3: 2.5, nE4: 2})
    nA4.childs.update({nA3: 1.75, nA2: 0.5, nB3: 2,
                      nB4: 2.5, nD3: 3.5, nD4: 3})

    nB1.childs.update({nB3: 1.75, nB2: 0.5})
    nB2.childs.update({nB4: 1.75, nB1: 0.5})
    nB3.childs.update({nA4: 2, nB1: 1.75, nB4: 0.5, nD4: 2.5})
    nB4.childs.update({nB2: 1.75, nB3: 0.5, nC4: 1.5})

    nC1.childs.update({nC2: 1, nC4: 1.75})
    # a C6 no hi ha numero, suposem que es 0 ??
    nC2.childs.update({nC1: 1, nC3: 1, nC6: 0})
    nC3.childs.update({nC2: 1, nC8: 1.75})
    nC4.childs.update({nB4: 1.5, nC1: 1.75, nC7: 0.5})
    nC5.childs.update({nC6: 0.5, nC8: 0.5})
    nC6.childs.update({nC2: 0, nC5: 0.5, nC7: 0.5})  # Again distancia a C2
    nC7.childs.update({nC4: 0.5, nC6: 0.5})
    nC8.childs.update({nC3: 1.75, nC5: 0.5, nD3: 1.5})

    nD1.childs.update({nD2: 0.5, nD3: 1.75})
    nD2.childs.update({nD1: 0.5, nD4: 1.75})
    nD3.childs.update({nA4: 3.5, nC8: 1.5, nD1: 1.75, nD4: 0.5})
    nD4.childs.update({nA4: 3, nB3: 2.5, nD2: 1.75, nD3: 0.5})

    nE1.childs.update({nE2: 0.5, nE3: 1.75})
    nE2.childs.update({nE1: 0.5, nE4: 1.75})
    nE3.childs.update({nA3: 2.5, nE1: 1.75, nE4: 0.5})
    nE4.childs.update({nA3: 2, nE2: 1.75, nE3: 0.5})


def selectLessCost(options):

    cost = 100
    nextStep = None

    for key, value in options.items():
        #heuristic = calculHeuristica
        # if(heuristic< actual.Heuristic and not key.isVisited)
        if(value < cost):
            cost = value
            nextStep = key

    return {nextStep: cost}


def AddCost(actualSet):
    global actual
    global cost_a

    for key, value in actualSet.items():
        actual = key
        cost_a += value


def recursivity(node):
    actualNode = node[-1]
    global cost_a
    global solution

    # Cas de que estem al desti
    if(actualNode == desti):
        finalPath.extend(node)

        q = tuple(node)
        solution[q] = cost_a

        print(cost_a, " pasant per ", node)
        # node.pop(-1)
        # print(node)
        return

    # Cas de si l ultim es pocho
    if(actualNode.isVisited):
        # print(actualNode, " is already visited")
        # node.pop(-1)
        return

    actualNode.isVisited = True

    for child, cost in actualNode.childs.items():
        node.append(child)
        cost_a +=cost
        recursivity(node)
        node.pop(-1)
        cost_a -=cost
        Visit(node)


def Visit(list):
    copyList = []
    copyList = copy.copy(nodeList)
    
    for node in list:
        node.isVisited=True
        copyList.remove(node)
    Unvisit(copyList)

def Unvisit(list):
    for node in list:
        node.isVisited=False

def Greedy():
    global actual
    global pathOptions
    global finalPath

    while(actual != desti):

        if(not actual.isVisited):
            pathOptions.clear()

            actual.isVisited = True

            pathOptions = selectLessCost(actual.childs)

            AddCost(pathOptions)

            print("Següent parada, ", actual.name)

            finalPath.append(actual)

def GetNodeInput(elementNumber):
    nodeName = input("%s%s%s" % ("Enter order ", elementNumber, " (Following format A1, A2, B1...)"))
    node = StringToNode(nodeName)

    if node == NULL:
        print("%s%s%s" % ("Empty ", elementNumber, " order / Node not found / Wrong format)"))

    return node

def StringToNode(nodeName):
    for node in nodeList:
        if node.__str__() == nodeName:
            return node
    return NULL

def GetDestinies(maximumOrders):
    destinies = []
    for i in range(maximumOrders):
        destinies.append(GetNodeInput(i+1))
    return destinies

def RobotPath(maximumOrders):
    global destinies
    destinies = GetDestinies(maximumOrders)
    


# def NodeCreation(list):

Cuina = Node("Cuina")

nA1 = Node("A1")
nA2 = Node("A2")
nA3 = Node("A3")
nA4 = Node("A4")

nB1 = Node("B1")
nB2 = Node("B2")
nB3 = Node("B3")
nB4 = Node("B4")

nC1 = Node("C1")
nC2 = Node("C2")
nC3 = Node("C3")
nC4 = Node("C4")
nC5 = Node("C5")
nC6 = Node("C6")
nC7 = Node("C7")
nC8 = Node("C8")

nD1 = Node("D1")
nD2 = Node("D2")
nD3 = Node("D3")
nD4 = Node("D4")

nE1 = Node("E1")
nE2 = Node("E2")
nE3 = Node("E3")
nE4 = Node("E4")

nodeList = []
nodeList.extend((Cuina, nA1, nA2, nA3, nA4,
nB1, nB2, nB3, nB4,
nC1, nC2, nC3, nC4, nC5, nC6, nC7, nC8,
nD1, nD2, nD3, nD4,
nE1, nE2, nE3, nE4))


# Variables globals

actual = Cuina
desti = nE2

destinies = []

cost_a = 0
solution = {}
finalPath = []
finalPath.append(actual)

createTree()

print("Estudiem el recorregut entre ", actual.name, " i ", desti.name, "\n")


# Greedy()
# Per no tocar la llista directament, sino una copia
refList = finalPath.copy()
recursivity(refList)

# Seleccionem la que te menor cost
solution = selectLessCost(solution)

print("---------------------------------------\n")
print("El recorregut final (amb algoritme Greedy) passa per: ", list(solution.keys()), "\n")

print("El cost del recorregut total es: ", sum(solution.values()))
print("---------------------------------------\n")


RobotPath(4)