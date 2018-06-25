# -*- coding: utf-8 -*-

import sys

class StackNode():
    def __init__(self, d = None, n = None):
        """
        建立節點
        :param d: 資料欄位
        :param n: 後繼節點指標
        """
        self.data = d
        self.next = n

    def print_data(self):
        print("Node value: " + str(self.data))

class LinkedStack(object):
    """
    init an empty linked stack
    """
    def __init__(self):
        self.size = 0
        self.top = None # 首指標，指向堆疊的頂端節點

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, user_data):

        new_node = StackNode(user_data)
        new_node.next = self.top # 新節點指向目前堆疊頂端的節點
        self.top = new_node # 把首指標指向新節點

        self.size += 1

    def pop(self):

        if self.is_empty():
            print('Empty Stack')
        else:
            pop_node = self.top
            self.top = self.top.next
            self.size -= 1

            return pop_node

    def print_stack(self):

        curr_node = self.top
        while curr_node.next is not None:
            curr_node.print_data()
            curr_node = curr_node.next

        curr_node.print_data() # 堆疊底端節點

    def get_top(self):
        return self.top.data

    def get_stack_length(self):
        return self.size


def main():
    myStack = LinkedStack()
    myStack.push('1')
    myStack.push('2')
    myStack.push('3')
    myStack.push('4')
    myStack.push('5')
    myStack.push('6')
    print('Top Data:', myStack.get_top())
    myStack.print_stack()

    print('Pop Data:', myStack.pop().data)
    myStack.print_stack()

    print('Stack Length:', myStack.get_stack_length())


if __name__ == '__main__':
    main()
