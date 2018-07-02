# -*- coding: utf-8 -*-

from random import randint
import sys

class TreeNode:

    def __init__(self, user_data):
        self.data = user_data
        self.leftchild = None # 指向左子節點
        self.rightchild = None # 指向右子節點
        self.parent = None # 指向父母節點

    def insert(self, user_data):
        """
        新增節點
        :param user_data:
        :return:
        """
        if self.data == user_data: # 避免重複資料
            return False
        elif self.data > user_data: # 節點資料大於新資料，新資料往左邊子樹節點走
            if self.leftchild:
                return self.leftchild.insert(user_data)
            else:
                self.leftchild = TreeNode(user_data)
                self.leftchild.parent = self # 設定新節點的parent
                return True
        elif self.data < user_data: # 節點資料小於新資料，新資料往右邊子樹節點走
            if self.rightchild:
                return self.rightchild.insert(user_data)
            else:
                self.rightchild = TreeNode(user_data)
                self.rightchild.parent = self # 設定新節點的parent
                return True

    def find(self, find_data):
        """
        尋找節點
        有找到返回該節點
        沒找到返回False
        :param find_data:
        :return:
        """
        if self.data == find_data:
            return self
        elif self.data > find_data and self.leftchild: # 節點資料大於被搜尋資料，被搜尋資料往左邊子樹節點走
            return self.leftchild.find(find_data)
        elif self.data < find_data and self.rightchild: # 節點資料小於被搜尋資料，被搜尋資料往右邊子樹節點走
            return self.rightchild.find(find_data)
        else:
            return False

    def preorder(self):
        """
        前序走訪
        :return:
        """
        print(str(self.data))
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def inorder(self):
        """
        中序走訪
        :return:
        """
        if self.leftchild:
            self.leftchild.inorder()
        print(str(self.data))
        if self.rightchild:
            self.rightchild.inorder()

    def postorder(self):
        """
        後序走訪
        :return:
        """
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(str(self.data))

    def get_height(self):
        """
        計算樹的高度
        :return:
        """
        if self.leftchild and self.rightchild:
            return 1 + max(self.leftchild.get_height(), self.rightchild.get_height())
        elif self.leftchild:
            return 1 + self.leftchild.get_height()
        elif self.rightchild:
            return 1 + self.rightchild.get_height()
        else:
            return 1

    def get_height_second(self):
        l_height = 0
        r_height = 0
        # Compute the depth of each subtree
        if self.leftchild:
            l_height = self.leftchild.get_height()
        elif self.rightchild:
            r_height = self.rightchild.get_height()

        # Use the larger one
        if (l_height > r_height):
            return l_height + 1
        else:
            return r_height + 1

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, user_data):
        if self.root is None: # 第一次建立節點->成為根節點
            self.root = TreeNode(user_data)
            return True
        else:
            return self.root.insert(user_data)

    def find(self, find_data):
        if self.root is None: # 沒有任何節點
            return False
        else:
            return self.root.find(find_data)

    def preorder(self):

        if self.root:
            print('Pre-Order')
            self.root.preorder()
        else:
            return False

    def inorder(self):

        if self.root:
            print('In-Order')
            self.root.inorder()
        else:
            return False

    def postorder(self):

        if self.root:
            print('Post-Order')
            self.root.postorder()
        else:
            return False

    def get_height(self):
        if self.root:
            return self.root.get_height()
        else:
            return 0

    def get_height_second(self):
        if self.root:
            return self.root.get_height_second()
        else:
            return 0

    def get_num_of_child(self, begin_node):
        """
        返回begin_node有幾個子節點
        :param begin_node:
        :return:
        """
        num_of_child = 0
        if begin_node.leftchild:
            num_of_child += 1
        if begin_node.rightchild:
            num_of_child += 1

        return num_of_child

    def min_value_node(self, begin_node = None):
        """
        begin_node的子樹中，有最小值的節點(the leftmost leaf node)
        :param begin_node:
        :return:
        """
        if begin_node is None:
            curr_node = self.root
        else:
            curr_node = begin_node

        while curr_node.leftchild is not None:
            curr_node = curr_node.leftchild

        return curr_node

    def remove_value(self, del_data):
        """
        透過值找到該節點然後移除節點
        :param del_data:
        :return:
        """
        return self.remove_node(self.find(del_data))

    def remove_node(self, node_to_del):
        """
        移除節點
        :param node_to_del:
        :return:
        """
        if node_to_del is False:
            return 'Not Found'
        else:
            node_parent = node_to_del.parent
            num_of_child = self.get_num_of_child(node_to_del)

            # situation 1 : the node to be deleted has no child (leaf node)
            if num_of_child == 0:
                if node_parent is not None: # the node to be deleted has parent node
                    if node_parent.leftchild == node_to_del:
                        node_parent.leftchild = None
                    else:
                        node_parent.rightchild = None
                else: # the node to be deleted has no parent node == root node
                    self.root = None # the tree has only root node, delete root node means delete the tree

            # situation 2 : the node to be deleted has only one child
            if num_of_child == 1:
                if node_to_del.leftchild is not None:
                    child = node_to_del.leftchild
                else:
                    child = node_to_del.rightchild

                if node_parent is not None:
                    if node_parent.leftchild == node_to_del:
                        node_parent.leftchild = child
                    else:
                        node_parent.rightchild = child
                else: # root node
                    self.root = child

                child.parent = node_parent

            # situation 3 : the node to be deleted has both left child and right child
            if num_of_child == 2:
                # get the inorder successor node (smallest in the right subtree) of the node to be deleted
                successor_node = self.min_value_node(node_to_del.rightchild)
                node_to_del.data = successor_node.data
                self.remove_node(successor_node)

            return True

def main():
    myTree = BinarySearchTree()

    number_list = []
    for i in range(0, 10):
        rand_number = randint(1, 100)
        number_list.append(rand_number)
        myTree.insert(rand_number)

    # number_list = [88, 7, 30, 37, 26, 53, 18, 5, 77, 80]
    # for i in number_list:
    #     myTree.insert(i)

    print(number_list)
    myTree.preorder()
    myTree.inorder()
    myTree.postorder()
    print('Height:', myTree.get_height())
    # print('Height:', myTree.get_height_second())

    del_data = number_list[randint(0, 9)]
    # del_data = 30
    print('Find?', del_data, myTree.find(del_data))
    print('Delete:', del_data, myTree.remove_value(del_data))
    myTree.inorder()

if __name__ == '__main__':
    main()
