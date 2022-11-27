graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '4': ['8'],
    '7': ['8'],
    '2': [],
    '8': []
}
# set to keep track of visited nodes
visited = set()

print("DFS : ")


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


# Driver code
dfs(visited, graph, '5')
print(" ")

# BFS
# List for visited nodes
visited = []
# initialize a queue
queue = []


# function to implement BFS

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    # Loop to visit each node
    while queue:
        m = queue.pop(0)

        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Driver code
print("BFS : ")
bfs(visited, graph, '5')
