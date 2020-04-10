class Node():
    def __init__(self):
        self.val = None
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        self.left_child = Node()
        return self.left_child

    def get_right_child(self):
        self.right_child = Node()
        return self.right_child
input()
preorder = list(map(lambda x:int(x),input().split(' ')))
inorder = list(map(lambda x:int(x),input().split(' ')))

node = Node()
def get_tree(pre_order,in_order,node):
    if not pre_order:
        return
    node.val = pre_order[-1]
    index = in_order.index(node.val)
    if len(pre_order) == 1:
        return
    get_tree(pre_order[index:-1],in_order[index+1:],node.get_right_child())
    get_tree(pre_order[:index], in_order[:index], node.get_left_child())


def printPreorder(root):
    if root:
        printPreorder(root.left_child)
        print(root.val if root.val else '',end=' ')
        printPreorder(root.right_child)

def printPostorder(root):
    if root:
        printPostorder(root.left_child)
        printPostorder(root.right_child)
        print(root.val if root.val else '',end=' ')

def bfs(node_list,flag):
    alist = []
    if not node_list:
        return
    for node in node_list:
        if node.val:
            if flag:
                print(' '+str(node.val),end='')
            else:
                print(node.val,end='')
        if node.left_child:
            alist.append(node.left_child)
        if node.right_child:
            alist.append(node.right_child)
    bfs(alist,1)

if __name__ == '__main__':
    get_tree(preorder,inorder,node)
    # printPreorder(node)
    # print()
    # printPostorder(node)
    bfs([node],0)