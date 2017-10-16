""" 
Depth-First search as the name hints at, 
explores possible vertices (from a supplied root) 
down each branch before backtracking. 

This property allows the algorithm to be implemented 
succinctly in both iterative and recursive forms. 
Below is a listing of the actions performed 
upon each visit to a node.

    - Mark the current vertex as being visited.
    - Explore each adjacent vertex that is not included in the visited set.
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

