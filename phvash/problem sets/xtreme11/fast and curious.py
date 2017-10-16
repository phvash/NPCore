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
        print('node: ', node)
        if node not in visited:
            # add node to list of checked nodes
            visited.add(node)
            neighbours = graph.get(node, set())
            print('visited: ', visited)
            print('neighbours: ', neighbours)
            if visited.union(neighbours) == visited:
                closed_path = visited
                print('closed_path: ', closed_path)
                print('queue: ', queue)
                new_node = queue.pop(0)
                queue = [new_node]
                neighbours = graph.get(new_node, set())
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
                    print('queue: ', queue)
                visited = set()
                continue

            # add neigbours to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

graph = {
    5: {4, 2},
    4: {5, 2},
    2: {5, 3, 4},
    3: {2, 1}
}

print(traverse(graph, 5))