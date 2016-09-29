from random import shuffle

import itertools
from relations_dicts import get_adj_list


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
    h = tuple(sum(sl[j] for j in i) for i in rel.values())
    print(h)
    return h
