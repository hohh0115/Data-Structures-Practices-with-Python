# -*- coding: utf-8 -*-

"""

"""

import sys

class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    vertex_list = {}
    edge_matrix = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertex_list:
            self.vertex_list[vertex.name] = vertex
            for row in self.edge_matrix: # 對矩陣新增一行
                    row.append(0)
            self.edge_matrix.append([0] * (len(self.edge_matrix) + 1)) # 對矩陣新增一列
            self.edge_indices[vertex.name] = len(self.edge_indices) # 紀錄頂點在矩陣的第幾列
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertex_list and v in self.vertex_list:
            self.edge_matrix[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edge_matrix[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edge_matrix)):
                print('[', self.edge_matrix[i][j], ']' , end='')
            print(' ')

def main():
    myGraph = Graph()
    for i in range(ord('A'), ord('E')):
        myGraph.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AC', 'AD', 'BC', 'CD']  # 無向圖形的邊
    for edge in edges:
        myGraph.add_edge(edge[:1], edge[1:])

    myGraph.print_graph()

if __name__ == '__main__':
    main()

