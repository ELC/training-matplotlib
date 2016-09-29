from random import shuffle

rel = {
       1 : (2,3)
      ,2 : (1,3,4)
      ,3 : (1,2,4)
      ,4 : (2,3)
      }

rel2 = {
       1 : [2,4,5]
      ,2 : [1,3,5]
      ,3 : [2,6]
      ,4 : [1,5,7]
      ,5 : [1,2,4,6,8]
      ,6 : [3,5,9]
      ,7 : [4,8]
      ,8 : [5,7,9]
      ,9 : [5,6,8]
      }

rel3 = {
       1 : [2,4,5]
      ,2 : [1,3,5]
      ,3 : [2,6]
      ,4 : [1,5]
      ,5 : [1,2,4,6]
      ,6 : [3,5]
      }

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
	cleancycles(setOfCycles)
	return { number:poligon for number, poligon in zip(range(length),setOfCycles) }

def foo(sub, lst):
    '''Checks if sub is in lst.

    Expects both arguments to be lists
    '''
    if len(lst) < len(sub):
        return False
    return sub == lst[:len(sub)] or foo(sub, lst[1:])

def cleancycles(cycles):
	aux = [list(i) for i in cycles]
	print(aux)
	for i in aux[:]:
		deletelist = set()
		aux2 = aux[:]
		aux2.remove(i)
		for j in aux2:
			if foo(j,i):
				deletelist.add(frozenset(i))
	print(deletelist)

dic =getDicOfPoligons(rel)
for k,v in dic.items():
	print(k,v)

