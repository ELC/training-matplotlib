from random import shuffle
import timeit

def main(typerel=3, shuffledList=[]):
	
	selectedRelation = getRelation(typerel)

	if not shuffledList:
		shuffledList = initList(typerel)
	
	listOfPoligons = generatePoligons(shuffledList, selectedRelation)
	
	return listOfPoligons

def getRelation(typerel):
    start_time = timeit.default_timer()
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
       0 : [1,4]
      ,1 : [0,2,4,5]
      ,2 : [1,3,6,7]
      ,3 : [2,7]
      ,4 : [0,1,5,8]
      ,5 : [1,4,6,9]
      ,6 : [2,5,7,10]
      ,7 : [2,3,6,11]
      ,8 : [4,9,12,13]
      ,9 : [5,8,10,13]
      ,10 : [6,9,11,14]
      ,11 : [7,10,14,15]
      ,12 : [8,13]
      ,13 : [8,9,12,14]
      ,14 : [10,11,13,15]
      ,15 : [11,14]
      }
      
    rel5x5 = {
       0 : [1,5]
      ,1 : [0,2,6]
      ,2 : [1,3,6,8]
      ,3 : [2,4,8]
      ,4 : [3,9]
      ,5 : [0,6,10]
      ,6 : [1,2,5,7,10,11]
      ,7 : [6,8,12]
      ,8 : [2,3,7,9,13,14]
      ,9 : [4,8,14]
      ,10 : [5,6,15,16]
      ,11 : [6,12,16]
      ,12 : [7,11,13,17]
      ,13 : [8,12,18]
      ,14 : [8,9,18,19]
      ,15 : [10,16,20]
      ,16 : [10,11,15,17,21]
      ,17 : [16,12,18]
      ,18 : [13,14,17,19,22,23]
      ,19 : [14,18,24]
      ,20 : [15,21]
      ,21 : [16,20,22]
      ,22 : [16,18,21,23]
      ,23 : [18,22,24]
      ,24 : [19,23]
      }
    listOfRelations = {3:rel3x3, 4:rel4x4, 5:rel5x5 }
    typeOfRelation = listOfRelations[typerel]
    print("timer1",timeit.default_timer() - start_time)
    
    dicOfPoligons = getDicOfPoligons(typeOfRelation)
    return dicOfPoligons

def getDicOfPoligons(rel):
    start_time = timeit.default_timer()
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
    print("timer2",timeit.default_timer() - start_time)
    start_time = timeit.default_timer()
    result = generateDic(setOfCycles)
    print("timer3",timeit.default_timer() - start_time)
    return result


def generateDic(setOfCycles):
	length = len(setOfCycles)
	setOfCycles = cleancycles(setOfCycles)
	return { number:poligon for number, poligon in zip(range(length),setOfCycles) }
	
def cleancycles(cycles):
	aux = [list(i) for i in cycles]
	for i in aux[:]:
		aux2 = aux[:]
		aux2.remove(i)
		for j in aux2:
		    if all(k in i for k in j) or len(i) > 4 :
		        aux.remove(i)
		        break
	return sorted(aux)

def initList(typerel):
    limit = typerel**2 + 1
    listOfNumbers = [i for i in range(1,limit)]
    shuffle(listOfNumbers)
    return listOfNumbers

def generatePoligons(sL,rel):
    return [sum(sL[j] for j in i) for i in rel.values()]


"""

Testing

"""
def testing():
	testcases = {
		"3x3": ([8,5,9,1,7,6,2,3,4], [20, 16, 27, 13, 17, 14])
		,"4x4": ([7,2,6,10,8,13,1,12,15,11,3,16,5,9,4,14], [17, 22, 23, 28, 19, 47, 35, 29, 28, 27, 32, 23, 34])
		,"5x5": ([9,1,14,23,17,16,8,18,2,25,7,22,5,20,21,11,15,6,12,13,19,4,10,3,24],[34, 23, 39, 42, 67, 48, 45, 55, 31, 53, 52, 33, 48, 43, 49, 29, 43, 46, 25, 52])
		}
	print("Testing Main Function")
	for i in testcases:
		a = testcases[i][0]
		expected = testcases[i][1]
	
		typerel = len(a) ** 0.5
		
		print("\nTest for", i)
		
		start_time = timeit.default_timer()
		result = main(typerel,a)
		totalTime = timeit.default_timer() - start_time
		
		passed = result == expected
		
		print(" Total Time: ", totalTime, "\n Pass = ", passed)
	

testing()

