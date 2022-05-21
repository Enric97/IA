

#Clase del Node
class Tree:
    def __init__(self, name):
        self.childs = {}
        self.name = name
        self.leaf = False


    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

#Relacionem els nodes i assignem valors
def createTree():

    # No tenim en compte recorreguts en direcció inversa
    # Hi han dos maneres de afegir coses a un diccionari, fem servir ambes
    granollers.childs[mataro] = 14
    arc_triomf.childs[mataro] = 9
    clot_arago.childs[mataro] = 4
    tetuan.childs.update({clot_arago: 2, arc_triomf: 10, mataro: 4})
    calders.childs.update({granollers: 3, tetuan: 6})
    moia.childs.update({calders: 5, tetuan: 10})


def checkValidity(node):
    # Comprovar si el node arriba fins a mataro o es mataro
    # Si no pot arribar, retornara fals (no passa mai en el nostre cas)
    result=[]
    print("Studing Node: ", node.name)
    if(node==desti):
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
    
    #Si existeis un sol cami que sigui possible, retornem True, sino retornem False
    if True in result: 
        return True
    print("Not existing path across ", node)
    return False

#Basicament mirem el diccionari on guardem nodes i el seu cost
# i agafem el que te un cost menor
# IMPORTANT: es fa despres de comprovar que es viable arribar al desti
def selectLessCost(options):

    cost = 100
    nextStep = None

    for key, value in options.items():
        if(value<cost):
            cost=value
            nextStep=key

    return {nextStep: cost}

#Funcio per sumar el cost del viatge
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



# Variables globals
moia = Tree("Moià")
tetuan = Tree("Tetuan")
calders = Tree("Calders")
clot_arago = Tree("Clot aragó")
arc_triomf = Tree("Arc del triomf")
granollers = Tree("Granollers")
mataro = Tree("Mataró")
mataro.leaf = True

actual = moia
desti = mataro
cost_a = 0
possiblePath = {}
finalPath = []
finalPath.append(actual)

print("Estudiem el recorregut entre ", actual.name, " i ", desti.name, "\n")

createTree()

Greedy()

print("---------------------------------------\n")
print("El recorregut final (amb algoritme Greedy) passa per: ", finalPath, "\n")
print("El cost del recorregut total es: ", cost_a)
print("---------------------------------------\n")

