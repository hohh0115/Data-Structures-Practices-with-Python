# -*- coding: utf-8 -*-

import sys
from random import randint

class Node():
    def __init__(self, initdata = 0):
        self.data = initdata
        self.next = None

def do_list_traverse():
    ptr = head.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next

def refresh_to_end_node(head):
    ptr = head
    while ptr.next != None:
        ptr = ptr.next

    return ptr

def insert_at_end(begin_node, insert_count, loop_count):

    for i in range(1, insert_count + 1):
        new_data = Node(str(randint(1, 500)) + '-尾插法No.' + str(loop_count) + '-' + str(i))
        begin_node.next = new_data  # 前一次迴圈做的節點的指標欄位指向這次迴圈做的新節點
        new_data.next = None  # 最後一個節點指標為空
        begin_node = begin_node.next  # ptr為最後節點，供下一次迴圈使用

def insert_at_head(head, insert_count, loop_count):
    for i in range(1, insert_count + 1):
        new_data = Node(str(randint(1, 500)) + '-頭插法No.' + str(loop_count) + '-' + str(i))
        new_data.next = head.next
        head.next = new_data

def insert_at_point(head, insert_count, insert_point):
    pass

make_list = False
select = 0
count = 0
head = Node() # linked list的首指標
insert_point = 0
loop_count = 1

while make_list is not True:
    print('使用尾插法:1，使用頭插法：2，任意插入：3，離開：-1')
    try:
        select = int(input('輸入一個選項:'))
        if select > 0:
            count = int(input('要有幾個節點?'))
    except ValueError:
        print('輸入錯誤')
        print('請重新輸入\n')
        continue

    if select == 1:
        begin_node = refresh_to_end_node(head)
        insert_at_end(begin_node, count, loop_count)
    elif select == 2:
        insert_at_head(head, count, loop_count)
    elif select == 3:
        insert_index = int(input('從第幾個位置開始插入?'))
        j = 1
        point = head
        while j < insert_index:
            point = point.next
            j += 1

        if not point:
            print('該位置不存在')
            continue
        else:
            pass
            # print(point.data)
            # print(point.next.data)
            # sys.exit(1)

        for i in range(1, count + 1):
            new_data = Node(str(randint(1, 500)) + '-插入第' + str(insert_index) + '位置No.' + str(loop_count) + '-' + str(i))
            new_data.next = point.next
            point.next = new_data

    elif select == -1:
        make_list = True
    else:
        print('看不懂')
        continue

    loop_count += 1
    do_list_traverse()





