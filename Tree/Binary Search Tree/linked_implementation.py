# -*- coding: utf-8 -*-

from random import randint

class TreeNode:

    def __init__(self, user_data):
        self.data = user_data
        self.leftchild = None
        self.rightchild = None

    def insert(self, user_data):
        if self.data == user_data:
            return False
        elif self.data > user_data: # 節點資料大於新資料，新資料往左邊子樹節點走
            if self.leftchild:
                return self.leftchild.insert(user_data)
            else:
                self.leftchild = TreeNode(user_data)
                return True
        elif self.data < user_data: # 節點資料小於新資料，新資料往右邊子樹節點走
            if self.rightchild:
                return self.rightchild.insert(user_data)
            else:
                self.rightchild = TreeNode(user_data)
                return True

    def find(self, find_data):
        if self.data == find_data:
            return True
        elif self.data > find_data: # 節點資料大於被搜尋資料，被搜尋資料往左邊子樹節點走
            if self.leftchild:
                return self.leftchild.find(find_data)
            else:
                return False
        elif self.data < find_data: # 節點資料小於被搜尋資料，被搜尋資料往右邊子樹節點走
            if self.rightchild:
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
        print('Pre-Order')
        self.root.preorder()

    def inorder(self):
        print('In-Order')
        self.root.inorder()

    def postorder(self):
        print('Post-Order')
        self.root.postorder()

def main():
    number_list = []
    myTree = BinarySearchTree()
    for i in range(0, 100):
        rand_number = randint(1, 500)
        number_list.append(rand_number)
        myTree.insert(rand_number)

    print(myTree.insert(40))
    print(number_list)
    print(myTree.find(number_list[3]))
    # myTree.preorder()
    # myTree.inorder()
    # myTree.postorder()

if __name__ == '__main__':
    main()
