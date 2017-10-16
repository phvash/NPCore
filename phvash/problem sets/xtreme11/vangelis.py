def cyclic(graph):
    """Return True if the directed graph has a cycle.
    The graph must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False

    """
    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(graph)]
    while stack:
        for v in stack[-1]:
            if v in path_set:
                return 1
            elif v not in visited:
                visited.add(v)
                path.append(v)
                path_set.add(v)
                stack.append(iter(graph.get(v, ())))
                break
        else:
            path_set.remove(path.pop())
            stack.pop()
    return 0

def build_graph(list_of_nos, no_of_pairs):
    graph = {}
    for no in range(no_of_pairs):
        node_one = list_of_nos[no*2]
        node_two = list_of_nos[((no*2)) + 1]
        
        neighbours_of_one = graph.get(node_one, set())
        neighbours_of_one.add(node_two)
        graph[node_one] = neighbours_of_one

        neighbours_of_two = graph.get(node_two, set())
        neighbours_of_two.add(node_one)
        graph[node_two] = neighbours_of_two

    return graph
    
# demog = build_graph([0, 1, 0, 2, 1, 2, 2, 3, 0, 3], 5)
# print(cyclic(demog))
# demog2 = build_graph([0, 1, 0, 3, 1, 2, 1, 5, 3, 4], 5)
# print(cyclic(demog2))

# t = int(input())
# for l in range(t):
#     n, m = input().strip(' ').split(" ")
#     num_list = [int(j) for j in input().strip(' ').split(' ')]
#     print(cyclic(build_graph(num_list, int(m))))

print(cyclic({1: (2,), 2: (3,), 3: (1,)}))
print(cyclic(({1: (2,), 2: (3,), 3: (4,)})))
