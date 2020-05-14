class Node():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


total = []


def create_tree(node, data_list):
    length = len(data_list)
    if length == 1:
        node.value = data_list[0]
        return
    if length == 0:
        return
    n2 = len(bin(length).split('b')[-1]) - 2
    n2 = 0 if n2 <= 0 else n2
    if length - 2 ** n2 >= 2 ** (n2+1):
        rage = length - 2 ** n2 - (2 ** (n2+1)-1)
        mid = length - 2 ** n2 - (rage)
    else:
        mid = length - 2 ** n2
    node.value = data_list[mid]
    node.left = Node()
    node.right = Node()
    create_tree(node.left, data_list[:mid])
    create_tree(node.right, data_list[mid + 1:])


def bfs(node):
    queue = [node]
    while queue:
        node = queue.pop(0)
        total.append(node.value)
        if node.left is not None and node.left.value is not None:
            queue.append(node.left)
        if node.right is not None and node.right.value is not None:
            queue.append(node.right)


if __name__ == '__main__':
    input()
    datas = list(map(int, input().split()))
    root = Node()
    create_tree(root,sorted(datas))
    bfs(root)
    print(' '.join(map(str,total)))
