# -*- coding: utf-8 -*-

import sys
from build_insert_traverse_01 import insert_at_end, Node, do_list_traverse

if __name__ == '__main__':
    count = 20
    head = Node() # the external reference of the list
    delete_node = True
    delete_at = 0
    insert_at_end(head, count, 1)

    while delete_node is not False:
        print('目前singly linked list內容：')
        do_list_traverse(head)
        try:
            delete_at = int(input('刪除第幾個位置的?'))
        except ValueError:
            print('輸入錯誤，請重新輸入！')
            continue

        j = 1
        point = head
        try:
            while j < delete_at:  # 第delete_at位置的前一個節點就可以，第delete_at位置的節點用其前一個節點的指標做指向
                point = point.next
                j += 1
        except AttributeError:
            print('該位置不存在')
            continue
        else:
            if point is None:  # 當 delete_at = 2 時候...
                print('該位置不存在')
                continue

        delete_at_node = point.next
        point.next = point.next.next # 第delete_at位置的前一個節點的指標欄位指向第delete_at位置的後一個節點
        print('刪除的節點內容：%s' %(delete_at_node.data))
        print('========================')

        delete_at_node.next = None
        # delete_at_node = None # still take up space in memory.
        # del delete_at_node
