from random import shuffle
import timeit
import itertools


def get_adj_list(number):
    triangle = {
    	0:[3,1]
    	,1: [0,2,3,4]
    	,2: [1,4]
    	,3: [0,1,4,5]
    	,4: [1,2,3,5]
    	,5: [3,4]
    }
    
    rel2x3 = {
        0: [1, 3, 4]
        , 1: [0, 2, 4]
        , 2: [1, 5]
        , 3: [0, 4]
        , 4: [0, 1, 3, 5]
        , 5: [2, 4]
    }

    rel3x3 = {
        0: [1, 3, 4]
        , 1: [0, 2, 4]
        , 2: [1, 5]
        , 3: [0, 4, 6]
        , 4: [0, 1, 3, 5, 7, 8]
        , 5: [2, 4, 8]
        , 6: [3, 7]
        , 7: [4, 6, 8]
        , 8: [4, 5, 7]
    }

    rel4x4 = {
        0: [1, 4]
        , 1: [0, 2, 4, 5]
        , 2: [1, 3, 6, 7]
        , 3: [2, 7]
        , 4: [0, 1, 5, 8]
        , 5: [1, 4, 6, 9]
        , 6: [2, 5, 7, 10]
        , 7: [2, 3, 6, 11]
        , 8: [4, 9, 12, 13]
        , 9: [5, 8, 10, 13]
        , 10: [6, 9, 11, 14]
        , 11: [7, 10, 14, 15]
        , 12: [8, 13]
        , 13: [8, 9, 12, 14]
        , 14: [10, 11, 13, 15]
        , 15: [11, 14]
    }

    rel5x5 = {
        0: [1, 5]
        , 1: [0, 2, 6]
        , 2: [1, 3, 6, 8]
        , 3: [2, 4, 8]
        , 4: [3, 9]
        , 5: [0, 6, 10]
        , 6: [1, 2, 5, 7, 10, 11]
        , 7: [6, 8, 12]
        , 8: [2, 3, 7, 9, 13, 14]
        , 9: [4, 8, 14]
        , 10: [5, 6, 15, 16]
        , 11: [6, 12, 16]
        , 12: [7, 11, 13, 17]
        , 13: [8, 12, 18]
        , 14: [8, 9, 18, 19]
        , 15: [10, 16, 20]
        , 16: [10, 11, 15, 17, 21, 22]
        , 17: [16, 12, 18]
        , 18: [13, 14, 17, 19, 22, 23]
        , 19: [14, 18, 24]
        , 20: [15, 21]
        , 21: [16, 20, 22]
        , 22: [16, 18, 21, 23]
        , 23: [18, 22, 24]
        , 24: [19, 23]
    }
    listofrelations = {"t":triangle, "2": rel2x3, "3": rel3x3, "4": rel4x4, "5": rel5x5}
    return listofrelations[number]


def main(nro_rel=3, shuffledlist=None):
    
    if shuffledlist is None:
        shuffledlist = []
        
    adj_list = get_adj_list(nro_rel)
    poligon_list = get_dict_poligons(adj_list)

    if not shuffledlist:
        shuffledlist = initList(typerel)

    listofpoligons = generatePoligons(shuffledlist, poligon_list)

    return listofpoligons


def get_dict_poligons2(rel):
    def shortestpath(start, end):
        nextnode = start
        partialpath = {nextnode}
        parent = lookfor_parents(rel, end, vertex,start)
        while nextnode != end:
            nextnode = parent[start]
            partialpath.add(nextnode)
            start = nextnode
        return partialpath

    setofcycles = {}
    setofuniques = set()
    count = 0
    cycles = []
    tested = set()
    for vertex, child in rel.items():
        pairs =  itertools.permutations(child,2)
        for firstchild in child:
            paths = set()
            for otherchild in (i for i in child if i != firstchild):
                tested.add(frozenset([firstchild,otherchild]))
                path = {vertex}
                centralpath = shortestpath(firstchild, otherchild)
                path |= centralpath 
                paths.add(frozenset(path))
            minimum = min(len(i) for i in paths)
            cycle = (i for i in paths if len(i) == minimum)
            for i in cycle:
                unique = frozenset(i)
                if unique not in setofuniques:
                    setofuniques.add(unique)
                    setofcycles[count] = tuple(i)
                    count += 1
    
    return setofcycles

def get_dict_poligons(rel):
    def shortestpath(start, end):
        nextnode = start
        partialpath = {nextnode}
        parent = lookfor_parents(rel, end, vertex,start)
        while nextnode != end:
            nextnode = parent[start]
            partialpath.add(nextnode)
            start = nextnode
        return partialpath

    setofcycles = {}
    setofuniques = set()
    count = 0
    cycles = []
    checked = set()
    for vertex, child in rel.items():
        pairs = {}
        for a,b in itertools.permutations(child,2):
        	if a not in pairs:
        		pairs[a] = []
        	pairs[a].append(b)
        for firstchild in pairs:
            paths = set()
            secondpair = pairs[firstchild]
            for otherchild in secondpair:
                path = {vertex}
                centralpath = shortestpath(firstchild, otherchild)
                path |= centralpath 
                paths.add(frozenset(path))
            minimum = min(len(i) for i in paths)
            cycle = (i for i in paths if len(i) == minimum)
            for i in cycle:
                unique = frozenset(i)
                if unique not in setofuniques:
                    setofuniques.add(unique)
                    setofcycles[count] = tuple(i)
                    count += 1
    return setofcycles


def lookfor_parents(adj, s, omit,start):
    parent = {s: None}
    frontier = [s]
    while frontier:
        nextfrontier = []
        for u in frontier:
            for v in adj[u]:
                if v not in parent:
                    parent[v] = u
                    nextfrontier.append(v)
                if v == start:
                    return parent
        if omit in nextfrontier:
            nextfrontier.remove(omit)
        frontier = nextfrontier
    return parent

def initList(typerel):
    limit = typerel ** 2 + 1
    listofnumbers = [i for i in range(1, limit)]
    shuffle(listofnumbers)
    return listofnumbers


def generatePoligons(sl, rel):
    h = {sum(sl[j] for j in i) for i in rel.values()}
    return h


"""

Testing

"""


def testing():
    def getinfofromrel(reltype):
        rel = get_adj_list(reltype)
        nodes = getnumberofnodes(rel)
        edges = getnumberofedges(rel)
        return nodes, edges

    def getnumberofnodes(rel):
        return len(rel)

    def getnumberofedges(rel):
        return sum(len(j) for j in rel.values())

    def formatTime(totaltime):
        totaltime *= 1000000
        totaltime = int(totaltime)
        return totaltime

    def timecalulation(totaltime):
        totaltime = formatTime(totaltime)
        diff = getformatteddifference(relativetime)
        return totaltime, diff

    def getformatteddifference(relativet):
        diff = relativet[-1] - relativet[0]
        if diff != 0:
            diff = (diff / relativet[0]) * 100
            diff = int(diff)
            diff = "+" + str(diff) + "%"
        else:
            diff = "-"
        return diff

    def printhead():
        nodes, edges = getinfofromrel(typerel)
        print("\nTest for", i
              , "\n Number of Nodes:", nodes
              , "\n Number of Edges:", edges
              , "\n Total parts:", nodes + edges)

    def printfooter():
        print(" Time in microseconds: ", ttime
              , "\n Difference with first:", difference
              , "\n Pass = ", passed
              )

    def test(reltype):
        start_time = timeit.default_timer()
        output = main(reltype, inputtest)
        time = timeit.default_timer() - start_time
        relativetime.append(time)
        time, diff = timecalulation(time)
        return output, time, diff

    testcases = {
        "triangle": ([i for i in range(1,7)],{7,11,10,15})
        ,"2x3": ([1, 2, 3, 4, 5, 6]
                , {8, 10, 16})

        , "3x3": ([8, 5, 9, 1, 7, 6, 2, 3, 4]
                  , {20, 16, 27, 13, 17, 14})

        , "4x4": ([7, 2, 6, 10, 8, 13, 1, 12, 15, 11, 3, 16, 5, 9, 4, 14]
                  , {17, 22, 23, 28, 19, 47, 35, 29, 28, 27, 32, 23, 34})

        , "5x5": (
            [9, 1, 14, 23, 17, 16, 8, 18, 2, 25, 7, 22, 5, 20, 21, 11, 15, 6,
             12,
             13, 19, 4, 10, 3, 24]
            , {34, 23, 39, 42, 67, 48, 45, 55, 31, 53, 52, 33, 48, 43, 49, 29,
               43,
               46, 25, 52})
    }
    print("Testing Main Function")

    relativetime = []
    passes = []

    for i in sorted(testcases):
        typerel = i[0]

        printhead()

        inputtest = testcases[i][0]
        result, ttime, difference = test(typerel)

        expectedoutput = testcases[i][1]
        passed = result == expectedoutput
        passes.append(passed)

        printfooter()
    if all(passes):
        print("EXITO")
    else:
        print("FRACASO")
testing()
