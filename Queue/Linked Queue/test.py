# -*- coding: utf-8 -*-

class Node:

    def __init__(self, d = None, n = None):

        self.data = d
        self.next = n # 指向下一個節點

    def print_data(self):
        print("Node value: " + str(self.data))

class LinkedQueue:

    def __init__(self):
        """
        沒有首指標的linked list，因此沒有建立任何class node
        """
        self.first = None # head pointer 指向第一個節點
        self.last = None # tail pointer 指向最後一個節點
        self.size = 0

    def is_empty(self):
        return self.first is None

    def enqueue(self, user_data):
        """
        從尾巴新增一個節點
        :param user_data:
        :return:
        """
        old_last = self.last # 之前的最後一個節點
        self.last = Node(user_data)
        if self.is_empty(): # 第一次新增節點...
            self.first = self.last # 因為只有一個節點，兩個指標指向同一個節點
        else:
            old_last.next = self.last # 之前的最後一個節點指向現在的最後一個節點
        self.size += 1

    def dequeue(self):
        delete = self.first
        self.first = self.first.next # dequeue的話，第二個節點變成第一個節點
        if self.is_empty():
            self.last = None
        self.size -= 1
        return delete

    def __str__(self):
        s = ''
        curr_node = self.first
        while curr_node is not None:
            s += str(curr_node.data) + ' '
            curr_node = curr_node.next
        return s

def main():
    myQueue = LinkedQueue()
    myQueue.enqueue('1')
    myQueue.enqueue('2')
    myQueue.enqueue('3')
    myQueue.enqueue('4')
    print(myQueue)

    myQueue.dequeue()
    myQueue.enqueue('5')
    myQueue.dequeue()
    print(myQueue)

if __name__ == '__main__':
    main()