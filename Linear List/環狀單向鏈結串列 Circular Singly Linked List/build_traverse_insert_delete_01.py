# -*- coding: utf-8 -*-

import sys

class Node():

    def __init__(self, d, n):
        """
        建立節點
        :param data:
        """
        self.data = d # 資料欄位
        self.next_node = n # 指標欄位

    def print_data(self):
        print("Node value: " + str(self.data))

class CircularLinkedList():
    """
    所有的position都是從1開始，而非0開始，因為語言上比較直觀
    """
    def __init__(self):
        """
        初始化一個有首節點(dummy node)的環狀鍊結串列
        """
        self.head = Node(None, None) # dummy node, will point to the first node of the list
        self.head.next_node = self.head # make it circular
        self.size = 0

    def print_list_size(self):
        """
        印出當前串列長度
        :return:
        """
        print('List Size:', self.size)

    def size_count(self):
        """
        和size屬性一樣，只是這裡重頭開始數
        :return:
        """
        count = 0
        curr_node = self.head.next_node
        while curr_node != self.head:
            count += 1
            curr_node = curr_node.next_node

        return count

    def insert_last(self, user_data):
        """
        尾插法
        :param user_data:
        :return:
        """
        curr_node = self.head.next_node
        while curr_node.next_node != self.head: # 代表不是最後一個節點，所以需要走訪到最後一個節點
            curr_node = curr_node.next_node

        # 這裡可以確定curr_node是最後一個節點了
        new_node = Node(user_data, curr_node.next_node) # new_node為要新增的節點，這時curr_node.next_node依然指向self.head
        curr_node.next_node = new_node # 連接

        self.size += 1

    def insert_front(self, user_data):
        """
        頭插法
        :param user_data:
        :return:
        """
        new_node =  Node(user_data, self.head.next_node)
        self.head.next_node = new_node

        self.size += 1

    def insert(self, user_data, position):
        """
        插入任意position，這裡position是從1開始，而非0
        插入第position=3的位置，則原本position=3的位置(index=position-1=2)的元素向後移動
        :param user_data:
        :param position:
        :return:
        """
        if 0 < position <= self.size:
            curr_node = self.head # trick
            curr_position = 1

            while curr_position < position: # 找到第position位置前一個位置的節點
                curr_node = curr_node.next_node
                curr_position += 1

            new_node = Node(user_data, curr_node.next_node)
            curr_node.next_node = new_node
            self.size += 1
        else:
            print('Position not exist')

    def remove_first(self):
        """
        移除第一個Node
        :return:
        """
        delete_node = self.head.next_node
        self.head.next_node = delete_node.next_node
        delete_node.next_node = None

        self.size -= 1

    def remove_last(self):
        """
        移除最後一個Node
        :return:
        """
        curr_node = self.head.next_node

        while curr_node.next_node.next_node != self.head: # curr_node = 最後一個節點的前一個節點
            curr_node = curr_node.next_node

        delete_node = curr_node.next_node
        curr_node.next_node = self.head
        delete_node.next_node = None

        self.size -= 1

    def remove(self, position):
        """
        移除第position的Node
        :param position:
        :return:
        """
        if 0 < position <= self.size:
            curr_node = self.head # trick
            curr_position = 1
            while curr_position < position: # curr_node = 最後一個節點的前一個節點
                curr_node = curr_node.next_node
                curr_position += 1

            delete_node = curr_node.next_node
            curr_node.next_node = delete_node.next_node
            delete_node.next_node = None

            self.size -= 1
        else:
            print('Position not exist')

    def fetch_position_data(self, position):
        """
        找出第position位置的資料
        :param position:
        :return:
        """
        if 0 < position <= self.size:
            curr_node = self.head.next_node # trick
            curr_position = 1
            while curr_position < position: # trick
                curr_node = curr_node.next_node
                curr_position += 1

            print('Position', position, 'data:', curr_node.data)
        else:
            print('Position not exist')

    def print_list(self):
        """
        印出當前串列
        :return:
        """
        print('Printing List...')
        curr_node = self.head.next_node

        while curr_node != self.head:
            print(curr_node.data)
            # curr_node.print_data()
            curr_node = curr_node.next_node

def main():
    myList = CircularLinkedList()
    myList.insert_last('1')
    myList.insert_last('2')
    myList.insert_front('3')
    myList.insert_last('4')
    myList.insert_last('5')
    myList.insert_last('6')
    myList.insert('7', 2)
    myList.print_list_size()
    myList.print_list()

    myList.fetch_position_data(4)
    print('==================')
    print('Begin to remove...')

    myList.remove_first()
    myList.remove_last()
    myList.remove(3)
    myList.print_list_size()
    myList.print_list()
    myList.fetch_position_data(3)

if __name__ == '__main__':
    main()