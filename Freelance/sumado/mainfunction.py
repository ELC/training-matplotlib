"""This program is a generator for the SU-MA-DO game. Offial page for the
game: http://www.ingverger.com.ar/sumado.php.

This program take an adjacency list and a list of vertexes. The adjacency
list represent the configuration, for example: 3x3, 4x4 or 5x5. The list of
vertexes are the numbers inside the "vertexes", if it isn't passed as an
input it would be randomly generated.

The Glosary for understanding this program is the following:
    Adjacency List: A data structure that represent a graph with the following
    format: `vertex`: neighbour_vertexes
    Example:
    1: 2,4,5
    2: 1,3,5
    3: 2,6
    4: 1,5
    5: 1,2,4,6
    6: 3,5

    Vertex: Equivalent to node in graph theory

    Cycle: Equivalent to cycle in graph theory
    Example: 1: 2
    2: 3
    3: 4
    4: 3
    Cycle = (1,2,3,4,1)

    Supercycle: A Cycle whose vertexes are part of another cycle
    Example: 1:2
    2:3
    3:4
    4:1,2
    Cycle = (1,2,3,4,1)
    Subcycle = (2,3,4,2)

    Elementary Cycle: A cycle with no subcycles
    Example: 1: 2
    2: 3
    3: 4
    4: 3
    Cycle = (1,2,3,4,1)

    Poligon: An Elementary Cycle with no repeated vertexes. Two Poligons are
    equal if they have the same vertexes.

    In this program Adjacency List are represented as dictionaries, vertexes as
    integers and poligons as tuples
"""


from Freelance.sumado.adjacency_lists import get_adj_list
from random import shuffle
import itertools
import json


def main(adj_id, vertex_list=None, adj_list=None):
    """Return all the poligons for a given adjacency list

    Arguments:
        adj_id: ID for retriving stored the adjacency list.
        vertex_list: List of values for the vertexes, reserved for testing
        adj_list: Explicit Adjacency List, use in case the one needed isn't
        stored
    """

    if adj_list is None:
        adj_list = get_adj_list(adj_id)

    poligon_vertexes = get_poligon_vertexes(adj_list)

    if vertex_list is None:
        adj_list_len = len(adj_list)
        vertex_list = initList(adj_list_len)

    poligons_list = generatePoligons(vertex_list, poligon_vertexes)

    output_raw = {"vertexes": vertex_list, "poligons": poligons_list}
    output = json.dumps(output_raw)
    return output


def get_poligon_vertexes(adj_list):
    """Return a list of poligons vertexes"""

    setofcycles = []

    for vertex, child in adj_list.items():
        pairs = get_pairs(child)
        for firstchild in pairs:
            paths = set()
            secondpair = pairs[firstchild]
            for otherchild in secondpair:
                pair_parent = (firstchild, otherchild, vertex)
                parents = lookfor_parents(pair_parent, adj_list)
                path = shortestpath(pair_parent, parents)
                paths.add(path)
            new_cycles = get_new_cycles(paths)
            setofcycles.extend(new_cycles)
        clean_vertex(adj_list, vertex)
    return setofcycles


def get_pairs(base_list):
    """Return dictionary with the combinations of `base_list` elements

    Parse the typical output of `combinations` into a dict format to
    manipulate it more easily.

    Args:
        base_list: A list of elements in which we need to compare each element
                    with the rest at most once
    """
    pairs = {}
    for a, b in itertools.combinations(base_list, 2):
        if a not in pairs:
            pairs[a] = []
        pairs[a].append(b)
    return pairs


def clean_vertex(adj, vertex):
    """Remove `vertex` from the neighbour nodes of every node in `adj`

    Given an adjacency list, it will remove an specific vertex from every
    list of neighbour vertexes in the adjacency list.
    """
    for i in adj.values():
        if vertex in i:
            i.remove(vertex)


def get_new_cycles(paths):
    """Return a list of the cycles with minimum length

    Given a list of cycles, it find the minimum length and then return a list
    of all the cycles with that length
    """
    minimum_length = min(len(i) for i in paths)
    minimum_cycles = (i for i in paths if len(i) == minimum_length)
    return minimum_cycles


def lookfor_parents(pair_parent, adj):
    """Return the parents for a given graph starting at `start`

    Breadth First Search implementation that given the adjacency list and a
    start vertex returns the parent for all vertexes with the special
    condition that the `omit` vertex cannot be the parent of other vertex and
    a break point when reaching the `final` vertex

    Args:
        pair_parent: a tuple pack with `start`, `omit` and `final`
        start initial node
        omit: node that cannot be parent of any other node
        final: node that stops the execution
        adj: dictionary with the adjacency list of a graph
    """
    final, start, omit = pair_parent
    parent = {start: None}
    frontier = [start]
    while frontier:
        nextfrontier = []
        for node in frontier:
            for rel_node in adj[node]:
                if rel_node not in parent:
                    parent[rel_node] = node
                    nextfrontier.append(rel_node)
                if rel_node == final:
                    return parent
        if omit in nextfrontier:
            nextfrontier.remove(omit)
        frontier = nextfrontier
    return parent


def shortestpath(pair_parent, parents):
    """Return the shortest cycle including `start`, `end` and `vertex`
    vertexes

    Finding the shortest path using the `parents` provided by
    `lookfor_parents`

    Args:
        pair_parent: a tuple pack with `start`, `omit` and `final`
        start: initial node
        omit: node that cannot be parent of any other node
        final: node that stops the execution
        adj: dictionary with the adjacency list of a graph
    """
    start, end, vertex = pair_parent
    path = set()
    path.add(vertex)
    nextnode = start
    path |= {nextnode}
    while nextnode != end:
        nextnode = parents[start]
        path.add(nextnode)
        start = nextnode
    path = tuple(path)
    return path


def initList(n):
    """Returns a list from 1 to `n` sorted randomly"""
    limit = n+1
    listofnumbers = [i for i in range(1, limit)]
    shuffle(listofnumbers)
    return listofnumbers


def generatePoligons(vertexes_values, poligon_vertexes):
    """Returns the poligons values given the vertexes for each poligon.

    Arguments:
        vertexes_values: list of vertexes values
        poligon_vertexes: list of poligons vertexes
    """

    poligon_values = tuple(sum(vertexes_values[vertex]
                               for vertex in poligon)
                           for poligon in poligon_vertexes)
    return poligon_values
