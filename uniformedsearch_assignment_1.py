import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque
import heapq


#This assignment is to trace breadth first, depth first, and uniform cost search through
# a directed search graph

print("Hi AI overlords")


def breadth_first_search(graph,start_node,goal_node):
    visited = set([start_node])
    queue = deque([(start_node,0)])
    traversal = []
    while queue:
        current, cost = queue.popleft()
        traversal.append(current)

        if current == goal_node:
            return traversal, cost

        for neighbor,weight in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,cost + weight))
    return traversal, None

def depth_first_search(graph,start_node,goal_node):
    visited = set([start_node])
    queue = deque([(start_node, 0)])
    traversal = []
    while queue:
        current, cost = queue.pop()
        traversal.append(current)
        if current == goal_node:
            return traversal, cost
        for neighbor,weight in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, cost + weight))
    return traversal,None


def uniform_cost_search(graph,start_node,goal_node):
    order = 0 #used for tie breaking : it is the insertion order
    frontier = [(0, order, start_node)] #starting cost of 0
    best_cost = {start_node: 0}  #cheapest path
    explored = set()
    traversal = []
    while frontier:
        cost, _,current = heapq.heappop(frontier)

        if current in explored:
            continue
        explored.add(current)
        traversal.append(current)
        if current == goal_node:
            return traversal, cost

        for neighbor,weight in graph[current]:
            new_cost = cost + weight
            if neighbor not in explored and new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                order += 1
                heapq.heappush(frontier, (new_cost,order, neighbor))
    return traversal, None





def build_graph(edge_list):
    graph = {}
    for source, dest, weight in edge_list:
        graph.setdefault(source, []).append((dest, weight))
        graph.setdefault(dest, [])  # make sure destination-only nodes exist too
    return graph


def draw_graph(graph):
    G = nx.DiGraph()
    G.add_nodes_from(graph)
    for source, neighbors in graph.items():
        for dest, weight in neighbors:
            G.add_edge(source, dest, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=800,
            node_color="lightblue", arrowsize=20, alpha = 1.0)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))
    plt.show()


# Raw list: [source, destination, weight]
edges = [
    ["S", "A", 2],  #S->A with weight 2
    ["S", "B", 1],
    ["S", "C", 4],
    ["A", "D", 2],
    ["A", "G", 9],
    ["B", "D", 2],
    ["B", "E", 5],
    ["C", "E", 1],
    ["C", "F", 3],
    ["D", "G", 2],
    ["E", "G", 2],
    ["F", "G", 1]

]

my_graph = build_graph( edges)
#draw_graph(my_graph)
bfs_traversal, bfs_cost = breadth_first_search(my_graph, "S", "G")
print("BFS Traversal::", bfs_traversal)
print("BFS Cost::", bfs_cost)
dfs_traversal, dfs_cost = depth_first_search(my_graph, "S", "G")
print("DFS Traversal::", dfs_traversal)
print("DFS Cost::", dfs_cost)
ucs_traversal, ucs_cost = uniform_cost_search(my_graph, "S", "G")
print("UCS Traversal::", ucs_traversal)
print("UCS Cost::", ucs_cost)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
