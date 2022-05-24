from asyncio.windows_events import NULL
import copy
import operator
import math

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

class Path:
    def __init__(self, destinyNode, path, cost):
        self.destinyNode = destinyNode # C1
        self.path = path # [A1, A2, A3, C1]
        self.cost = cost # 15
    
    def __str__(self):
        return str(self.path)

    def __repr__(self):
        return str(self.path)

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

#Metode en que done diversos camins i ens retorna el que te un cost menor en un diccionari
def selectLessCost(options):

    cost = math.inf
    nextStep = None

    for key, value in options.items():
        if(value < cost):
            cost = value
            nextStep = key

    return {nextStep: cost}

# Metode que realitza la recursivitat per trobar tots els camins possibles entre 2 nodes i els seus costs
def recursivity(node): 
    actualNode = node[-1]
    global cost_a
    global solution

    # Cas de que estem al desti
    if(actualNode == desti):
        finalPath.extend(node)

        q = tuple(node)
        solution[q] = cost_a
        #print(cost_a, " pasant per ", node) # NOTE: TO ACTIVATE/DEACTIVATE EVERY PATH PRINTING
        return

    # Cas de si l ultim es pocho
    if(actualNode.isVisited):
        # print(actualNode, " is already visited")
        return


    actualNode.isVisited = True

    #Bucle duro
    for child, cost in actualNode.childs.items():
        node.append(child)
        cost_a +=cost
        recursivity(node)
        node.pop(-1)
        cost_a -=cost
        Visit(node)

#Metode que marca com a visitats els nodes que li enviem per llista
#Relacionat amb el metode anterior
def Visit(list):
    copyList = []
    copyList = copy.copy(nodeList)
    
    for node in list:
        node.isVisited=True
        copyList.remove(node)
    Unvisit(copyList)

#Metode que marca com a no visitats els nodes que li arriben per una llista
#També relacionat amb el metode recursiu
def Unvisit(list):
    for node in list:
        node.isVisited=False

###
###Metodes per adaptar a 4 destins
###

#Metode que controla el input que posa l'usuari
def GetNodeInput(elementNumber):
    nodeName = input("%s%s%s" % ("Enter order ", elementNumber, " (Following format A1, A2, B1...) \n\t"))
    node = StringToNode(nodeName)

    if node == NULL:
        print("%s%s%s" % ("\tEmpty ", elementNumber, " order / Node not found / Wrong format)"))

    return node

#Metode que converteix l'string del usuari en el node
def StringToNode(nodeName):
    for node in nodeList:
        if node.__str__() == nodeName:
            return node
    return NULL

#Passant el nombre de destins que volem, usa els 2 metodes previs per agafar tants destins com volguem
def GetDestinies(maximumOrders):
    destinies = []
    for i in range(maximumOrders):
        node = GetNodeInput(i+1)
        if node != NULL:
            destinies.append(node)

    return destinies

#Metode per resetejar variables
#MOLT IMPORTANT
def ResetSolution():
    global solution
    global actual
    solution = {}
    actual.isVisited=False

#Metode encarregat de cridar al metode recursiu i agafar el de menor cost amb diversos prints
#Seria semblant a un main
def GetDestinyTopPath(destiny):
    global actual
    global desti
    global solution
    global finalPath

    desti = destiny
    print("\n\n---------------------------------------")
    print("Estudiem el recorregut entre ", actual.name, " i ", desti.name, "\n")

    # Per no tocar la llista directament, sino una copia
    refList = finalPath.copy()
    recursivity(refList)

    # Seleccionem la que te menor cost
    solution = selectLessCost(solution)

    
    print("\nEl recorregut final (amb algoritme Greedy) passa per: ", list(solution.keys()))

    print("El cost del recorregut total és: ", sum(solution.values()))
    print("---------------------------------------\n")

    path = list(solution.keys())
    cost = sum(solution.values())
    return Path(destiny, path, cost)

#El mateix que el select less cost
def GetBestPath(destiniesTopPaths):
    bestCost = math.inf

    for path in destiniesTopPaths:
        if path.cost < bestCost:
            bestCost = path.cost

    for path in destiniesTopPaths:
        if path.cost == bestCost:
            return path

    return NULL

#Not sure si es necessari, crec que la variable de finalPath es redundant (el path esta en solution)
def ResetFinalPath(currentActual):
    global finalPath
    finalPath = []
    finalPath.append(currentActual)

#Un altre metode principal, tipus main, que itera sobre tots els destins possibles a partir del node actual
#Crida als que calculen 
def GetCurrentDestiny(destinies):
    destiniesTopPaths = []
    global finalPath
    global actual
    currentActual = actual
    for destiny in destinies:
        ResetFinalPath(currentActual)
        # ResetSolution()
        destiniesTopPaths.append(GetDestinyTopPath(destiny))
        ResetSolution()
        
    return GetBestPath(destiniesTopPaths)

#Print
def PrintDestinyInfo(destinyPath):
    print("\n\n             SELECTED DESTINY: ", destinyPath.destinyNode)
    print("                         PATH: ", destinyPath.path)
    print("                         COST: ", destinyPath.cost, "\n\n")

#Fer la tornada a la cuina
def PathBackToCuina():
    global actual

    ResetFinalPath(actual)
    destinyPath = GetDestinyTopPath(Cuina)
    actual = Cuina
    PrintDestinyInfo(destinyPath)

    return destinyPath

#un altre main¿?¿?
def GetRobotPath(maximumOrders):
    global actual

    destinies = []
    destinies = GetDestinies(maximumOrders)

    finalRobotPath = []

    while destinies:
        destinyPath = GetCurrentDestiny(destinies)
        finalRobotPath.append(destinyPath)

        destinies.remove(destinyPath.destinyNode)
        actual = destinyPath.destinyNode
        PrintDestinyInfo(destinyPath)

    finalRobotPath.append(PathBackToCuina())
    
    return finalRobotPath

#Print de la solucio final
def PrintFinalPathsInfo(finalRobotPaths):
    finalRobotPath = []
    finalRobotCost = 0
    
    for path in finalRobotPaths:
        finalRobotPath.append(path.path)
        finalRobotCost += path.cost
    print("\n\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    print("            El recorregut final (amb algoritme A* amb càlcul d'heurística de Backtracking) passa per: \n                         ", finalRobotPath, "\n")

    print("            FINAL COST: ", finalRobotCost)
    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

#################################### Variables globals ###############################

## Nodes ##
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



# Mes variables globals

actual = Cuina
desti = NULL
cost_a = 0
solution = {}
finalPath = []
# finalPath.append(actual)

createTree()

finalRobotPath = GetRobotPath(4)
PrintFinalPathsInfo(finalRobotPath)