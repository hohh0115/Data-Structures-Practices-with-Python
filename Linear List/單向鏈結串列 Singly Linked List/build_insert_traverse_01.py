# -*- coding: utf-8 -*-

import sys
from random import randint

class Node():
    def __init__(self, initdata = 0):
        self.data = initdata
        self.next = None

def do_list_traverse(node_head):
    ptr = node_head.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next

def refresh_to_end_node(head):
    ptr = head
    while ptr.next != None:
        ptr = ptr.next

    return ptr

def insert_at_end(begin_node, insert_count, loop_count):
    """
    尾插法
    :param begin_node: linked list的最後一個節點
    :param insert_count: 插入多少節點
    :param loop_count:  使用者操作次數
    :return:
    """
    for i in range(1, insert_count + 1):
        new_data = Node(str(randint(1, 500)) + '-尾插法No.' + str(loop_count) + '-' + str(i))
        begin_node.next = new_data  # 前一次迴圈做的節點的指標欄位指向這次迴圈做的新節點
        new_data.next = None  # 最後一個節點指標為空
        begin_node = begin_node.next  # ptr為最後節點，供下一次迴圈使用

def insert_at_head(head, insert_count, loop_count):
    """
    頭插法
    :param head: linked list的首指標
    :param insert_count: 插入多少節點
    :param loop_count: 使用者操作次數
    :return:
    """
    for i in range(1, insert_count + 1):
        new_data = Node(str(randint(1, 500)) + '-頭插法No.' + str(loop_count) + '-' + str(i))
        new_data.next = head.next
        head.next = new_data

def insert_at_point(begin_node, insert_count, insert_at, loop_count):
    """
    插入任意位置
    :param begin_node: linked list第幾個位置的前一個節點
    :param insert_count: 插入多少節點
    :param insert_at: 插入第幾個位置
    :param loop_count: 使用者操作次數
    :return:
    """
    for i in range(1, insert_count + 1):
        new_data = Node(str(randint(1, 500)) + '-插入第' + str(insert_at) + '位置No.' + str(loop_count) + '-' + str(i))
        new_data.next = begin_node.next
        begin_node.next = new_data

if __name__ == "__main__":

    make_list = True
    select = 0 # 使用者選擇哪個方法
    count = 0 # 使用者選擇產生幾個節點
    head = Node() # linked list的首指標
    insert_point = 0 # 第幾個位置做插入
    loop_count = 1 # 使用者操作幾次

    while make_list is not False:
        print('使用尾插法:1\n使用頭插法：2\n任意插入：3\n離開：-1')
        try:
            select = int(input('輸入一個選項:'))
            if select > 0:
                count = int(input('要有幾個節點?'))
        except ValueError:
            print('輸入錯誤，請重新輸入！')
            continue

        if select == 1:
            begin_node = refresh_to_end_node(head)
            insert_at_end(begin_node, count, loop_count)
        elif select == 2:
            insert_at_head(head, count, loop_count)
        elif select == 3:

            insert_at = int(input('從第幾個位置開始插入?'))
            j = 1
            point = head
            try:
                while j < insert_at: # 第insert_at位置的前一個節點就可以，第insert_at位置的節點用其前一個節點的指標做指向
                    point = point.next
                    j += 1
            except AttributeError:
                print('該位置不存在')
                continue

            else:
                if point is None: # 當 insert_at = 2 時候...
                    print('該位置不存在')
                    continue

            insert_at_point(point, count, insert_at, loop_count)
        elif select == -1:
            make_list = False
        else:
            print('看不懂')
            continue

        loop_count += 1
        do_list_traverse(head)
        print('========================')





