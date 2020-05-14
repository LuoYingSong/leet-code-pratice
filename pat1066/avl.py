class Node():
    def __init__(self, value):
        self.value = value
        self.father = None
        self.left_child = None
        self.right_child = None
        self.balance_factor = 0
        self.is_left = True

    def add_child(self, node, is_left):
        node.father = self
        if is_left:
            self.left_child = node
            node.is_left = True
        else:
            self.right_child = node
            node.is_left = False


class Tree():
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        add_node = Node(value)
        node = self.root
        while True:
            if value > node.value:  # 可能有bug
                if node.right_child:
                    node = node.right_child
                else:
                    node.add_child(add_node, False)
                    break
            else:
                if node.left_child:
                    node = node.left_child
                else:
                    node.add_child(add_node, True)
        self.update_balance(node)

    def update_balance(self, node):
        while True:
            if node.is_left:
                factor = 1
            else:
                factor = -1
            if node == self.root:
                break
            father = node.father
            father.balance_factor += factor
            node = node.father
            if father.balance_factor == 0:
                break
            if father.balance_factor == 2:
                self.right_rotate(node)
                break
            if father.balance_factor == -2:
                self.left_rotate(node)
                break

    def right_rotate(self, node:Node):
        old_node = node #1
        old_node_left_child = node.left_child #2
        if old_node == self.root:
            self.root = old_node_left_child
        else:
            if old_node.is_left:
                flag = True
            else:
                flag = False
            old_node.father.add_child(old_node_left_child,flag)
###解决平衡因子过大的爹的问题结束
        if old_node_left_child.right_child:
            old_node.add_child(old_node_left_child.right_child,True)
###把原节点右节点挂过去
        old_node_left_child.add_child(old_node,False)
        old_node.balance_factor = old_node.balance_factor - 1 - max(old_node_left_child.balance_factor,0)
        old_node_left_child.balance_factor = old_node_left_child.balance_factor + 1 - min(old_node_left_child.balance_factor,0)


    def left_rotate(self, node:Node):
        old_node = node
        old_node_right_child = node.right_child
        if old_node == self.root:
            self.root = old_node_right_child
        else:
            if old_node.is_left:
                flag = True
            else:
                flag = False
            old_node.father.add_child(old_node_right_child,flag)
        if old_node_right_child.left_child:
            old_node.add_child(old_node_right_child.right_child,False)
        old_node_right_child.add_child(old_node, True)
        old_node.balance_factor = old_node.balance_factor - 1 - max(old_node_left_child.balance_factor,0)
        old_node_left_child.balance_factor = old_node_left_child.balance_factor + 1 - min(old_node_left_child.balance_factor,0)
