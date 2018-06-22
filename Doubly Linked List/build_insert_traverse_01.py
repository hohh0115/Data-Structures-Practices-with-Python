# -*- coding: utf-8 -*-

import sys

class Node():
    def __init__(self, d = None, n = None, p = None):
        """
        建立節點
        :param d: 資料欄位
        :param n: 後繼節點指標
        :param p: 前驅節點指標
        """
        self.data = d
        self.next = n
        self.prior = p

    def print_data(self):
        print("Node value: " + str(self.data))

class DoublyLinkedList():
    """
    初始化一個空的環狀的雙向鏈結串列 empty circular doubly linked list
    由於是雙向的，所以新增一個一個tail node，比較好操作
    因此，有資料的節點是位於head node跟tail node中間的節點們
    """
    def __init__(self):
        self.head = Node(d='head')
        self.tail = Node(d='tail')
        self.size = 0

        self.head.next = self.head.prior = self.tail
        self.tail.next = self.tail.prior = self.head

    def insert_at_front(self, user_data):
        """
        頭插法
        :param user_data:
        :return:
        """
        new_node = Node(user_data, self.head.next, self.head)
        # new_node.next = self.head.next
        # new_node.prior = self.head

        self.head.next.prior = new_node
        self.head.next = new_node

        self.size += 1

    def insert_at_end(self, user_data):
        """
        尾插法(插在tail node前面的位置)
        :param user_data:
        :return:
        """
        new_node = Node(user_data, self.tail, self.tail.prior)
        # new_node.next = self.tail
        # new_node.prior = self.tail.prior

        self.tail.prior.next = new_node
        self.tail.prior = new_node

        self.size += 1

    def insert(self, user_data, position):
        """
        插入第position位置，position從1開始，而非1，如此語言上比較直觀
        :param user_data:
        :param position:
        :return:
        """
        curr_node = self.head # trick
        curr_position = 1
        if 0 < position <= self.size:
            while curr_position < position: # curr_node = 第position位置前一個位置的node
                curr_node = curr_node.next
                curr_position += 1

            new_node = Node(user_data, curr_node.next, curr_node)
            # new_node.next = curr_node.next
            # new_node.prior = curr_node

            curr_node.next = new_node
            curr_node.next.prior = new_node

            self.size += 1
        else:
            print('Position not exist')

    def fetch_position_data(self, position):
        if 0 < position <= self.size:
            curr_node = self.head.next # trick
            curr_position = 1
            while curr_position < position: # trick, curr_node = 第position位置的node
                curr_node = curr_node.next
                curr_position += 1

            print('Position', position, 'data:', curr_node.data)
        else:
            print('Position not exist')

    def print_list(self):
        curr_node = self.head.next
        while curr_node.next != self.head: # 當curr_node.next是head，代表curr_node為tail node
            curr_node.print_data()
            curr_node = curr_node.next

def main():
    myList = DoublyLinkedList()
    myList.insert_at_end('1')
    myList.insert_at_end('2')
    myList.insert_at_front('0')
    myList.insert_at_end('3')
    myList.insert('4', 2)
    myList.insert_at_end('5')
    myList.insert_at_front('6')
    myList.insert('7', 5)
    myList.print_list()

    myList.fetch_position_data(7)
    myList.fetch_position_data(2)
    print('==================')
    print('Begin to remove...')


if __name__ == '__main__':
    main()