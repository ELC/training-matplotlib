from random import shuffle

import itertools
from relations_dicts import get_adj_list


def main(rel_id, shuffledlist=None):
    """Return the tuple of poligon numbers"""
    
    adj_list = get_adj_list(rel_id)
    poligon_list = get_dict_poligons(adj_list)
    
    
    if shuffledlist is None:
        adj_list_len = len(adj_list)
        shuffledlist = initList(adj_list_len)
        
    
    listofpoligons = generatePoligons(shuffledlist, poligon_list)

    return listofpoligons
    

def get_dict_poligons(rel):
    def shortestpath(start, end):
        nextnode = start
        partialpath = {nextnode}
        parent = lookfor_parents(rel, end, vertex, start)
        while nextnode != end:
            nextnode = parent[start]
            partialpath.add(nextnode)
            start = nextnode
        return partialpath

    setofcycles = []
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
            cycle = (tuple(i) for i in paths if len(i) == minimum)
            expand = (i for i in cycle if i not in setofcycles)
            setofcycles.extend(expand)
            
    return setofcycles

##############################################################################
def lookfor_parents(adj, start, omit, final):
    """Return the parent tree for a given graph starting at `start`
    
    BFS implementation that given the adjacency list and a start node returns 
    the parent for all nodes with the special condition that the `omit` node 
    cannot be the parent of other node
    
    Args:
        adj: dictionary with the adjacency list of a graph
        start: initial node
        omit: node that cannot be parent of any other node
        final: node that stops the execution
    
    """
    parent = {start: None}
    frontier = [start]
    while frontier:
        nextfrontier = []
        for u in frontier:
            for v in adj[u]:
                if v not in parent:
                    parent[v] = u
                    nextfrontier.append(v)
                if v == final:
                    return parent
        if omit in nextfrontier:
            nextfrontier.remove(omit)
        frontier = nextfrontier
    return parent

def initList(n):
    """Returns a list from 1 to `n` sorted randomly"""
    limit = n+1
    listofnumbers = [i for i in range(1, limit)]
    shuffle(listofnumbers)
    return listofnumbers


def generatePoligons(sl, poligon_list):
    return tuple(sum(sl[j] for j in i) for i in poligon_list)
