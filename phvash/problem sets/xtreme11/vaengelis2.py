# visit all the nodes of a graph (connected component)
def traverse(graph, start):
    # keep track of all visited nodes
    # this prevents an infinite loop in case of cyclic component
    visited = set()
    
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are no nodes left unchecked
    while queue:
        # pop the shallowest (first node) from the queue
        node = queue.pop(0)
        if node not in visited:
            # add node to list of checked nodes
            visited.add(node)
            neighbours = graph[node]

            # add neigbours to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    if set(graph.keys()).difference(visited)) == set():
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
