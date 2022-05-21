

# Clase del Node
class Node:
    def __init__(self, name):
        self.childs = {}
        self.name = name
        self.leaf = False

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

# Relacionem els nodes i assignem valors


def createTree():

    Cuina.childs.update({nA1: 1, nA3: 1.5})
    nA1.childs.update({Cuina: 1, nA2: 1.75, nA3: 0.5})
    nA2.childs.update({nA1: 1.75, nA4: 0.5})
    nA3.childs.update({Cuina: 1.5, nA1: 0.5, nA4: 1.75, nE3: 2.5, nE4: 2})
    nA4.childs.update({nA3: 1.75, nA2: 0.5, nB3: 2,
                      nB4: 2.5, nD3: 2.5, nD4: 3})

    nB1.childs.update({nB3: 1.75, nB2: 0.5})
    nB2.childs.update({nB4: 17.5, nB1: 0.5})
    nB3.childs.update({nA4: 2, nB1: 1.75, nB4: 0.5, nD4: 2.5})
    nB4.childs.update({nB2: 1.75, nB3: 0.5, nC4: 1.5})

    nC1.childs.update({nC2: 1, nC4: 1.75})
    nC2.childs.update({nC1: 1, nC3: 1, nC6: 0}) # a C6 no hi ha numero, suposem que es 0 ??
    nC3.childs.update({nC2: 1, nC8: 1.75})
    nC4.childs.update({nB4: 1.5, nC1: 1.75, nC7: 0.5})
    nC5.childs.update({nC6: 0.5, nC8: 0.5})
    nC6.childs.update({nC2: 0, nC5: 0.5, nC7: 0.5})  # Again distancia a C2
    nC7.childs.update({nC4: 0.5, nC6: 0.5})
    nC8.childs.update({nC3: 1.75, nC5: 0.5, nD3: 1.5})

    nD1.childs.update({nD2: 0.5, nD3: 1.75})
    nD2.childs.update({nD1: 0.5, nD4: 1.75})
    nD3.childs.update({nA4: 3.5, nC8: 1.5, nD1: 1.75, nD4: 0.5})
    nD4.childs.update({nA4: 3, nB3: 2.5, nD2: 1.75, nD3: 1.75})

    nE1.childs.update({nE2: 0.5, nE3: 1.75})
    nE2.childs.update({nE1: 0.5, nE4: 1.75})
    nE3.childs.update({nA3: 2.5, nE1: 1.75, nE4: 0.5})
    nE4.childs.update({nA3: 2, nE2: 1.75, nE3: 0.5})


def checkValidity(node):
    # Comprovar si el node arriba fins a mataro o es mataro
    # Si no pot arribar, retornara fals (no passa mai en el nostre cas)
    result = []
    print("Studing Node: ", node.name)
    if(node == desti):
        return True

    for child in node.childs:

        if(child == desti):
            # print("\t", child.name, " is ", desti.name)
            print("\t Reached ", desti, " !!!")
            return True
        if(child.leaf):
            print("\t", child.name, " doesn't lead to ", desti.name)
            return False
        else:
            print("\t Next child: ", child.name)
            result.append(checkValidity(child))

    # Si existeis un sol cami que sigui possible, retornem True, sino retornem False
    if True in result:
        return True
    print("Not existing path across ", node)
    return False

# Basicament mirem el diccionari on guardem nodes i el seu cost
# i agafem el que te un cost menor
# IMPORTANT: es fa despres de comprovar que es viable arribar al desti


def selectLessCost(options):

    cost = 100
    nextStep = None

    for key, value in options.items():
        if(value < cost):
            cost = value
            nextStep = key

    return {nextStep: cost}

# Funcio per sumar el cost del viatge


def AddCost(actualSet):
    global actual
    global cost_a

    for key, value in actualSet.items():
        actual = key
        cost_a += value


def Greedy():
    global actual
    global possiblePath
    global finalPath

    while(actual != desti):
        possiblePath.clear()

        for key, cost in actual.childs.items():

            if(checkValidity(key)):
                possiblePath[key] = cost
                print("Branca analitzada\n")

        print("\nEls possibles camins son per ", possiblePath, "\n\n")

        actualSet = selectLessCost(possiblePath)

        AddCost(actualSet)

        print("Següent parada, ", actual.name)

        finalPath.append(actual)


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

# Variables globals

nodes = []
# actual = moia
# desti = mataro
# cost_a = 0
# possiblePath = {}
# finalPath = []
# finalPath.append(actual)




# print("Estudiem el recorregut entre ", actual.name, " i ", desti.name, "\n")

# createTree()

# Greedy()

# print("---------------------------------------\n")
# print("El recorregut final (amb algoritme Greedy) passa per: ", finalPath, "\n")
# print("El cost del recorregut total es: ", cost_a)
# print("---------------------------------------\n")
