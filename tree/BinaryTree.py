
class BinaryTree:
    def __init__(self,value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insertLeft(self,value):
        '''
        如果存在不存在左子树，即添加左子树的空树
        如果存在左子树，将原先的值给下一个子树的左子树，t的左子树
        :param value:
        :return:
        '''

        if not self.left_child:
            self.left_child = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self,value):
        if not self.right_child:
            self.right_child = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t.right_child = self.right_child
            self.right_child = t

