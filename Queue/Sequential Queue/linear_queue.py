# -*- coding: utf-8 -*-

"""
在python中實作Queue的方法有三種：
    1. 使用python的list data type以及相關的built-in functions ( e.g., insert() and pop() )，並且寫法上會把list的頭(index=0)作為queue的尾巴(用insert(0, data)做enqueue)、list的尾巴作為queue的頭(用pop()做dequeue)
    2. 使用python的queue module
    3. 單純使用陣列的方式去實作，需要事先宣告陣列的大小，這個也是最基本且最需要顧慮Queue它的結構原理的方法，但是在python中，會因為語言限制而有下列情況：
        1. 宣告陣列大小的問題：在python中，array就是python的list data type，所以若使用python去實作Queue時候，還是會用list data type，但會多一個integer max_size去宣告陣列大小
        2. 因為單純使用陣列方式，因此在enqueue時候，需使用queue[index] = new data的方式去實作，然而在python中，無法單憑max_size大小就開出一個裡面沒有元素的陣列，因此得 [None] * max_size，開出一個裡面有max_size大小且元素為None的list (若在enqueue時候想要使用append()方式，就不用[None] * max_size，直接使用空陣列就可以)
        3. queue = [None] * max_size還是可以用append()方法去加上新元素，因而超過設定的max_size，所以Queue做enqueue時會去檢查是否元素數量超過max_size

這裡使用第3項去實作Queue
"""

import sys

class Queue:

    def __init__(self):
        """
        init an empty queue
        head pointer - Points to the front of the Queue. Or in other words, it points to the element to be removed if the dequeue operation is called.
        tail pointer - Points to the next empty spot in which the new element can be inserted
        """
        self.max_size = 5
        self.queue = [None] * self.max_size
        self.head = 0 # head pointer指向queue的第一個元素的index值
        self.tail = 0 # tail pointer指向queue的最後一個元素的下一個位置的index值
        self.size = 0

    def enqueue(self, user_data):
        """
        add one element to the tail of the queue
        :param user_data:
        :return:
        """
        if self.size >= self.max_size:
            print('Queue Full')
        else:
            try:
                self.queue[self.tail] = user_data
                self.tail += 1
                self.size += 1
            except IndexError:
                print('Queue Index Out of Range!')

    def dequeue(self):
        """
        remove one element to the head of the queue
        :return:
        """
        # if self.size <= 0:
        if self.head == self.tail:
            self.reset_queue()
            print('Queue Empty')
        else:
            delete = self.queue[self.head]
            self.queue[self.head] = None
            self.head +=1
            self.size -= 1
            return delete

    def reset_queue(self):
        """
        reset the head and the tail pointer to 0 and restart the queue
        :return:
        """
        self.tail = 0
        self.head = 0
        self.queue = [None] * self.max_size

    def print_queue(self):
        print('=========')
        print(self.queue)
        print('Queue Size:', self.size)
        print('=========')

def main():
    myQueue = Queue()
    myQueue.print_queue()

    myQueue.enqueue('1')
    myQueue.enqueue('2')
    myQueue.enqueue('3')
    myQueue.enqueue('4')
    myQueue.enqueue('5')
    myQueue.print_queue()

    myQueue.dequeue()
    myQueue.print_queue()

    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.print_queue()

    myQueue.enqueue('1')
    myQueue.enqueue('2')
    myQueue.print_queue()

if __name__ == '__main__':
    main()