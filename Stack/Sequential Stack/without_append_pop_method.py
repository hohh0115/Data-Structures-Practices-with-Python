# -*- coding: utf-8 -*-

"""
Implementing a stack with only list data type(array only)
"""

class Stack():

    maxSize = 100 # stack max size, top: 0~99

    def __init__(self):
        """
        init an empty stack
        """
        self.stack = [None] * self.maxSize # init list/array with fixed size
        self.top = -1 # 堆疊頂端元素在陣列中的index值, -1 = empty stack

    def push(self, user_data):
        """
        進堆疊push
        if self.top > self.maxSize - 1: 只是為了符合「陣列須預先宣告大小」這件事而做檢查
        在python中，即使self.stack是一個list with fixed size，用append()多加一個資料元素也是可以的
        :param user_data:
        :return:
        """
        if self.top > self.maxSize - 1:
            print('Stack Full')
        else:
            self.top += 1
            self.stack[self.top] = user_data

    def pop(self):
        if self.top == -1:
            print('Empty Stack')
        else:
            del_element = self.stack[self.top]
            self.top -= 1
            return del_element

    def print_stack(self):
        print('Stack:', self.stack)

def main():
    myStack = Stack()
    myStack.push('1')
    myStack.push('2')
    myStack.push('3')
    myStack.push('4')
    myStack.print_stack()

    print('Pop one element:', myStack.pop())

if __name__ == '__main__':
    main()