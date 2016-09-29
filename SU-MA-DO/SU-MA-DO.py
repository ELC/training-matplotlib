from random import shuffle

from random import shuffle

def main(typerel=3, shuffledList=[]):
    selectedRelation = getRelation(typerel)
    for i in selectedRelation:
    	print(i, selectedRelation[i])
    if not shuffledList:        
        shuffledList = initList(typerel)
        
    listOfPoligons = generatePoligons(shuffledList, selectedRelation)
    return listOfPoligons

def getRelation(typerel):
    rel3x3 = {
       0 : [1,3,4]
      ,1 : [0,2,4]
      ,2 : [1,5]
      ,3 : [0,4,6]
      ,4 : [0,1,3,5,7]
      ,5 : [2,4,8]
      ,6 : [3,7]
      ,7 : [4,6,8]
      ,8 : [4,5,7]
      }

    rel4x4 = {
       0 : [0,1,4]
      ,1 : [1,4,5]
      ,2 : [1,2,5,6]
      ,3 : [2,3,7]
      ,4 : [2,6,7]
      ,5 : [4,5,8,9]
      ,6 : [5,6,9,10]
      ,7 : [6,7,10,11]
      ,8 : [8,9,13]
      ,9 : [8,12,13]
      ,10 : [9,10,13,14]
      ,11 : [10,11,14]
      ,12 : [14,11,15]
      }
    listOfRelations = {3:rel3x3}
    typeOfRelation = listOfRelations[typerel]
    dicOfPoligons = getDicOfPoligons(typeOfRelation)
    return dicOfPoligons

def initList(typerel):
    limit = typerel**2 + 1
    listOfNumbers = [i for i in range(1,limit)]
    shuffle(listOfNumbers)
    return listOfNumbers

def generatePoligons(sL,rel):
    return [sum(sL[j] for j in i) for i in rel.values()]


def getDicOfPoligons(rel):
    vertexes = []
    setOfCycles = set()
    def look(vertex, vertexes):
            related = (i for i in rel[vertex])
            vertexes.append(vertex)
            for i in related:
                if not i in vertexes:
                    look(i, vertexes)
                if i == lookingvalue:
                    vertexes.append(i)
                    if len(vertexes) != 3:
                        setOfCycles.add(frozenset(vertexes[:]))
                    del vertexes[-1]            
            del vertexes[-1]
            
    for vertex in rel:
        lookingvalue = vertex
        look(vertex, vertexes)
    return generateDic(setOfCycles)

def generateDic(setOfCycles):
	length = len(setOfCycles)
	setOfCycles = cleancycles(setOfCycles)
	return { number:poligon for number, poligon in zip(range(length),setOfCycles) }

	
def cleancycles(cycles):
	aux = [sorted(list(i)) for i in cycles]
	for i in aux[:]:
		aux2 = aux[:]
		aux2.remove(i)
		for j in aux2:
		    if all(k in i for k in j) or len(i) == 8 :
		        aux.remove(i)
		        break
	return sorted(aux)

"""
dic = 	getDicOfPoligons(rel2)
for k,v in dic.items():
	print(k,v)
	"""

a = [8,5,9,1,7,6,2,3,4]
print(main(3,a))

