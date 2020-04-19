node_num, n, goal = list(map(int, input().split(' ')))
weight_list = list(map(int, input().split(' ')))


class Node():
    def __init__(self, id_):
        self.id = id_
        self.weight = weight_list[id_]
        self.child_list = []

    def is_leaf_node(self):
        if self.child_list:
            return False
        else:
            return True

    def add_child(self, node):
        self.child_list.append(node)


node_dict = dict(zip(range(node_num), [Node(i) for i in range(node_num)]))
for i in range(n):
    node_id, _, *child_list = list(map(int, input().split(' ')))
    for child in child_list:
        node_dict[node_id].add_child(node_dict[child])
saver = []


def dfs(node, weight, path):
    path = list(path)
    weight += node.weight
    path.append(node.id)
    if node.is_leaf_node():
        if weight == goal:
            saver.append(path)
    else:
        path = tuple(path)
        for child in node.child_list:
            dfs(child, weight, path)


dfs(node_dict[0], 0, tuple())
saver2 = []
for item in saver:
    alist = []
    for node in item:
        alist.append(str(node_dict[node].weight))
    saver2.append(alist)


def list2str(x):
    str1 = ''
    for num in x:
        str1 += "{0:03d}".format(int(num))
    return str1


saver2 = sorted(saver2, key=list2str, reverse=True)
for item in saver2:
    print(' '.join(item))
