# import matplotlib.pyplot as plt
# # x axis values
# x = [1, 2, 3]
# # corresponding y axis values
# y = [2, 4, 1]
#
# # plotting the points
# plt.plot(x, y)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('My first graph!')
#
# # function to show the plot
# plt.show()
#

# from collections import defaultdict
#
# graph = defaultdict(list)
#
# def add_edge(graph, u, v):
#     graph[u].append(v)
#
# def generate_edges(graph):
#     edges = []
#
#     for node in graph:
#         for neighbor in graph[node]:
#             edges.append((node, neighbor))
#
#     return edges
#
# add_edge(graph, 'a', 'b')
# add_edge(graph, 'b', 'c')
# add_edge(graph, 'c', 'd')
# add_edge(graph, 'd', 'e')
# add_edge(graph, 'e', 'a')
#
# print (generate_edges(graph))

# Python program to print DFS traversal for complete graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v]= True
        print (v,)

        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        V = len(self.graph) #total vertices

        # Mark all the vertices as not visited
        visited =[False]*(V)

        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)


# Driver code
# Create a graph given in the above diagram
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
#
# print ("Following is Depth First Traversal")
# g.DFS()

# This code is contributed by Neelam Yadav



# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

# This class represents a directed graph
# using adjacency list representation
class Graph2:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
# g = Graph2()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
#
# print ("Following is Breadth First Traversal (starting from vertex 2)")
# g.BFS(2)

# This code is contributed by Neelam Yadav


class graph_V:
    def __init__(self):
        self.graph = defaultdict(list)
        self.dfs_visited = []
        self.bfs_visited = []
        self.queue = []
        self.edges = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.edges += 1
        self.dfs_visited = [False] * self.edges
        self.bfs_visited = [False] * self.edges

    def DFS(self, s):
        self.dfs_visited[s] = True

        print(s,)
        if s in self.graph[s]:
            for v in self.graph[s]:
                if self.dfs_visited[v] is False:
                    self.DFS(v)

    def BFS(self, s):
        self.bfs_visited[s] = True
        self.queue.append(s)

        while self.queue:
            v = self.queue.pop(0)
            print (v, )
            for n in self.graph[v]:
                if self.bfs_visited[n] is False:
                    self.queue.append(n)
                    self.bfs_visited[n] = True

    def find_mother(self):

        self.dfs_visited = [False] * self.edges
        x = None
        for v in self.graph:
            if self.dfs_visited[v] is False:
                self.DFS(v)
                x = v
        self.dfs_visited = [False] * self.edges
        self.DFS(x)

        if any(vertex == False for vertex in self.dfs_visited):
            print("No mother vertex")
        else:
            print("Mother vertex is ", x)

    """
        DFS applications
            -   Detecting cycle in a graph
            -   Path Finding
            -   Topological Sorting
            -   To test if a graph is bipartite
            -   Finding Strongly Connected Components of a graph
            -   Solving puzzles with only one solution,
        
        BFS application
            -   Shortest Path and Minimum Spanning Tree for unweighted graph 
            -   Peer to Peer Networks
            -   Crawlers in Search Engines
            -   Social Networking Websites
            -   GPS Navigation systems
            -   Broadcasting in Network
            -   In Garbage Collection
            -   Cycle detection in undirected graph
            -   Ford–Fulkerson algorithm
            -   To test if a graph is Bipartite
            -   Path Finding
            -   Finding all nodes within one connected component
    """

# gv = graph_V()
# gv.add_edge(1,0)
# gv.add_edge(0,3)
# gv.add_edge(3,4)
# gv.add_edge(0,2)
# gv.add_edge(2,1)
# # gv.add_edge(3,3)
# # gv.DFS(0)
# # print("#########")
# # gv.BFS(2)
#
# gv.find_mother()



class Graphs_t():
    def __init__(self, v):
        self.graphs = defaultdict(list)
        self.V = v

    def add_edge(self, u, v):
        self.graphs[u].append(v)

    def DFS_util(self, s, visited):

        visited[s] = True
        # print( s, )
        for v in self.graphs[s]:
            if visited[v] == False:
                self.DFS_util(v, visited)

    def DFS(self,v):

        visited = [False]*(len(self.graphs))
        self.DFS_util(v,visited)

    def find_mother(self):
        visited = [False] * self.V

        for i in range(self.V):
            if visited[i] == False:
                self.DFS_util(i,visited)
                x = i

        visited = [False] * (len(self.graphs))

        self.DFS_util(x, visited)

        if any(i == False for i in  visited):
            print( "No mom ")
        else:
            print (x, " is the mom")

    def DFC_ts(self, u, v, TC):

        TC[u][v] = 1

        for i in self.graphs[v]:
            if TC[u][i] == False:
                self.DFC_ts(u, i, TC)

    def transitiveClosure(self):
        TC = [[0 for i in range(self.V)] for j in range(self.V)]

        for i in range(self.V):
            self.DFC_ts(i,i,TC)

        print("      0, 1, 2, 3, 4, 5, 6")
        for i in range(len(TC)):
            print (i,"  ",[j for j in TC[i]])



gt = Graphs_t(7)
gt.add_edge(4, 0)
gt.add_edge(2, 1)
gt.add_edge(3, 4)
gt.add_edge(4, 2)
gt.add_edge(2, 6)
gt.add_edge(5, 2)
gt.add_edge(3, 5)
# gt.add_edge(6, 3)

# gt.DFS(0)

gt.find_mother()

gt.transitiveClosure()