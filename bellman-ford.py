G = {'A': ('B', 'H'),
     'B': ('A', 'C', 'H'),
     'C': ('B', 'D', 'F', 'I'),
     'D': ('C', 'E', 'F'),
     'E': ('D', 'F'),
     'F': ('C', 'D', 'E', 'G'),
     'G': ('F', 'H', 'I'),
     'H': ('A', 'B', 'G', 'I'),
     'I': ('C', 'G', 'H'),
     }
W = {('A', 'B'): 4, ('A', 'H'): 8, ('B', 'A'): 4, ('B', 'C'): 8, ('B', 'H'): 11, ('C', 'B'): 8, ('C', 'D'): 7,
     ('C', 'F'): 4, ('C', 'I'): 2, ('D', 'C'): 7,
     ('D', 'E'): 9, ('D', 'F'): 14, ('E', 'D'): 9, ('E', 'F'): 10, ('F', 'C'): 4, ('F', 'D'): 14, ('F', 'E'): 10,
     ('F', 'G'): 2, ('G', 'F'): 2, ('G', 'H'): 1, ('G', 'I'): 6,
     ('H', 'A'): 8, ('H', 'B'): 11, ('H', 'G'): 1, ('H', 'I'): 7, ('I', 'C'): 2, ('I', 'G'): 7, ('I', 'H'): 8}


def bellmanford(G, W, s):
    # s starting vertex
    # G -> graph (adj list) 'A':('B', 'D')
    # W -> weights of the edges
    SP = {}
    P = {}
    for i in G.keys():
        SP[i] = float('inf')
        P[i] = "null"
    SP[s] = 0
    number_of_vertices = len(G.keys())
    for i in range(number_of_vertices - 1):
        for (u, v) in W.keys():
            if SP[v] > SP[u] + W[(u, v)]:
                SP[v] = SP[u] + W[(u, v)]
                P[v] = u
    # check for negative cycle
    for (u, v) in W.keys():
        if SP[v] > SP[u] + W[(u, v)]:
            SP[v] = "undefined"

    return SP


print(bellmanford(G, W, 'A'))


def bellmanford2(G, W, s, l):
    # l vertex that we want to find the shortest path
    # s starting vertex
    # G -> graph (adj list) 'A':('B', 'D')
    # W -> weights of the edges
    SP = {}
    P = {}
    for i in G.keys():
        SP[i] = float('inf')
        P[i] = "null"
    SP[s] = 0
    number_of_vertices = len(G.keys())
    for i in range(number_of_vertices - 1):
        for (u, v) in W.keys():
            if SP[v] > SP[u] + W[(u, v)]:
                SP[v] = SP[u] + W[(u, v)]
                P[v] = u
    # check for negative cycle
    for (u, v) in W.keys():
        if SP[v] > SP[u] + W[(u, v)]:
            SP[v] = "undefined"
    if SP[l] == "undefined":
        return "undefined"
    else:
        x = l
        shortest_path = []
        shortest_path.append(l)
        while P[l] != "null":
            shortest_path.append(P[l])
            l = P[l]
        shortest_path.reverse()
        shortest_path.append(SP[x])
        return shortest_path


print(bellmanford2(G, W, 'B', 'E'))
