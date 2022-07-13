'''
why are perfect matches specifically this matche swhich are shown and no different?

Get all adjacent pairs (neighboors)
get all possible pairs 


Given an RNA string s=s1…sn, a bonding graph for s is formed as follows. First, assign each symbol of s to a node, and arrange these nodes in order around a circle, connecting them with edges called adjacency edges. Second, form all possible edges {A, U} and {C, G}, called basepair edges; we will represent basepair edges with dashed edges, as illustrated by the bonding graph in Figure 4.

Note that a matching contained in the basepair edges will represent one possibility for base pairing interactions in s, as shown in Figure 5. For such a matching to exist, s must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Problem:
    - it exists string s AGCUAGUCAU
    - first i need to create bonding graph
        - put A and U in a node and C with G with maximum size of two  
            - Bonding graph = {A, U}, {A, U}, {A, U}, {G, C}, {G, C}
    - second I need to create all possible basepair edges
    - what is a perfect match? - a graph with same C as G and A as U 

    First, let Kn denote the complete graph on 2n labeled nodes, in which every node is connected to every other 
    node with an edge, and let pn denote the total number of perfect matchings in Kn. For a given node x, there are 2n−1 ways 
    to join x to the other nodes in the graph, after which point we must form a perfect matching on the remaining 2n−2 nodes. 
    This reasoning provides us with the recurrence relation pn=(2n−1)⋅pn−1; using the fact that p1 is 1, this recurrence relation 
    implies the closed equation pn=(2n−1)(2n−3)(2n−5)⋯(3)(1).

    Kn = complete graph
    pn = total number perfect matches
    


Plan:
Execution!



AU AU AU GC GC

3  3  3 2 2 

'''