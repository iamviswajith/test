from node.Graph_Node import Graph_Node as Node

class Graph:
    def __init__(self, n):
        self.vertices = n
        self.graph = [None]*self.vertices

    def add_edge(self,src, dest):
        n_dest = Node(dest)
        n_dest.next = self.graph[src]
        self.graph[src] = n_dest

        n_src = Node(src)
        n_src.next = self.graph[dest]
        self.graph[dest] = n_src

    def print_graph(self):

        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")
