# -*- coding: utf-8 -*-

"""
implementation of undirected graph with Adjacency Matrix(鄰接矩陣)
"""

import sys

class Vertex:
    def __init__(self, n):
        self.name = n # 頂點名稱

class Graph:
    vertex_list = {} # 該圖形的頂點集合
    edge_matrix = [] # 頂點的邊陣列，代表頂點的邊矩陣。邊矩陣的第0列(index=0)為邊陣列index=0的陣列元素
    edge_indices = {} # {頂點名稱:該頂點的邊陣列資訊位於edge_matrix的index值=邊矩陣的第幾列(跟頂點加入的順序而形成的矩陣有關)}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertex_list:
            self.vertex_list[vertex.name] = vertex
            for row in self.edge_matrix: # 對矩陣新增一行 = 對edge_matrix這個二維陣列裡面的陣列元素新增一個元素
                row.append(0)
            self.edge_matrix.append([0] * (len(self.edge_matrix) + 1)) # 對矩陣新增一列 = 對edge_matrix這個二維陣列新增一個陣列元素。+1是因為這是一個n*n矩陣，剛好可以這樣用
            self.edge_indices[vertex.name] = len(self.edge_indices) # 紀錄頂點在矩陣的第幾列 = 頂點位於edge_matrix的index值
            return True
        else:
            return False

    def add_edge(self, start_vertex_name, end_vertex_name, weight = 1):
        if start_vertex_name in self.vertex_list and end_vertex_name in self.vertex_list:
            self.edge_matrix[self.edge_indices[start_vertex_name]][self.edge_indices[end_vertex_name]] = weight
            self.edge_matrix[self.edge_indices[end_vertex_name]][self.edge_indices[start_vertex_name]] = weight
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
    # print(len(myGraph.edge_matrix))

if __name__ == '__main__':
    main()

