# -*- coding: utf-8 -*-

"""
implementation of an undirected graph with Adjacency List, using Python dictionary

    1. 先對圖形建立頂點才可以加上邊(先add_vertex()再add_edge())
    2. 因為是無向圖形沒有方向，所以(A,B)這條邊，會分別存在於Vertex A的connected_to跟Vertex B的connected_to，因此add_edge()的部分會對兩個頂點各自加上
    3. 承上，所以edges = ['AB', 'AC', 'AD', 'BC', 'CD']的部分，一條無向邊只需要一種表達就好，例如'AB'有了那'BA'就不用了
"""

class Vertex:
    """
    頂點
    """
    def __init__(self, n):
        self.name = n # 頂點名稱
        self.connected_to = dict() # 該頂點的邊

    def add_neighbor(self, neighbor, weight = 0):
        if neighbor not in self.connected_to:
            self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.name) + ' connect to: ' + str([x.name for x in self.connected_to])

class Graph:
    """
    圖形
    """
    def __init__(self):
        self.vertex_list = dict() # 該圖形擁有的頂點
        self.num_of_vertices = 0 # 該圖形擁有的頂點個數

    def add_vertex(self, vertex):
        """
        對該圖形增加頂點
        :param vertex:
        :return:
        """
        if isinstance(vertex, Vertex) and vertex.name not in self.vertex_list:
            self.num_of_vertices += 1
            self.vertex_list[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex_name_1, vertex_name_2, weight = 0):
        """
        對該圖形的頂點加上邊
        :param vertex_name_1: 其中一個頂點名稱
        :param vertex_name_2: 另外一個頂點名稱
        :param weight: 權值
        :return:
        """
        if vertex_name_1 in self.vertex_list and vertex_name_2 in self.vertex_list:
            self.vertex_list[vertex_name_1].add_neighbor(self.vertex_list[vertex_name_2], weight)
            self.vertex_list[vertex_name_2].add_neighbor(self.vertex_list[vertex_name_1], weight)
            return True
        else:
            return False

    def print_vertices_edges(self):
        for vertex in self.vertex_list:
            print(self.vertex_list[vertex])

def main():

    myGraph = Graph()
    for i in range(ord('A'), ord('E')): # 建立有A,B,C,D四個頂點的圖形
        myGraph.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AC', 'AD', 'BC', 'CD'] # 無向圖形的邊
    for edge in edges:
        myGraph.add_edge(edge[:1], edge[1:])

    myGraph.print_vertices_edges()

if __name__ == '__main__':
    main()