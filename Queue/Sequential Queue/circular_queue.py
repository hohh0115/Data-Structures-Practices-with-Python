# -*- coding: utf-8 -*-

"""
Circular Queue: 如果queue滿了，就再重頭開始
改進linear_queue.py中，tail pointer超出index範圍的問題(IndexError)，而且queue前面的位置是空的狀況
"""

import sys

class CircularQueue:
    """
    empty queue: head pointer = tail pointer
    full queue: (tail pointer + 1) % max_size = head pointer => (the index of the last element + 2) % = head pointer
    所以，queue能放的最多元素數量是max_size-1個
    """
    def __init__(self):
        self.max_size = 5
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, user_data):
        next_tail_pos = (self.tail+1) % self.max_size
        if next_tail_pos == self.head:
            print('Queue Full! Data: %s can\'t enqueue' % str(user_data))
        else:
            self.queue[self.tail] = user_data
            self.tail = next_tail_pos
            self.size += 1

    def dequeue(self):
        if self.head == self.tail:
            print('Queue Empty')
        else:
            delete = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1

            return delete

    def get_queue_length(self):
        return (self.tail - self.head + self.max_size) % self.max_size

    def print_queue(self):
        print('#=========#')
        print(self.queue)
        print('Queue Size: %d / %d' % (self.get_queue_length(), self.size))
        print('#=========#\n')

def main():
    myQueue = CircularQueue()
    myQueue.print_queue()

    myQueue.enqueue('1')
    myQueue.enqueue('2')
    myQueue.enqueue('3')
    myQueue.enqueue('4')
    myQueue.enqueue('5')
    myQueue.print_queue()

    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.print_queue()

    myQueue.enqueue('1')
    myQueue.enqueue('2')
    # myQueue.enqueue('3')
    myQueue.print_queue()

if __name__ == '__main__':
    main()





