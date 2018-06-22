# -*- coding: utf-8 -*-

"""
By using python array method - append() and pop() and python list data type,
don't worry about the size of the stack since python can dynamically changes its stack size.
"""

class Stack():
    def __init__(self):
        """
        init an empty list
        """
        self.stack = list() # or self.stack = []

    def push(self, user_data):
        """
        進堆疊 stack push
        :param user_data:
        :return:
        """
        return self.stack.append(user_data)

    def pop(self):
        """
        出堆疊 stack pop
        :return:
        """
        if self.is_empty():
            print('Stack Empty')
        else:
            return self.stack.pop()

    def is_empty(self):
        # return self.stack == []
        return self.get_size() == 0

    def get_size(self):
        print(len(self.stack))

    def print_stack(self):
        print(self.stack)

def main():
    myStack = Stack()
    myStack.push('1')
    myStack.push('2')
    myStack.push('3')
    myStack.print_stack()
    myStack.pop()
    myStack.print_stack()
    myStack.get_size()

if __name__ == '__main__':
    main()