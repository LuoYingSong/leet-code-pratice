class Node():
    def __init__(self):
        self.value = None
        self.left_child = None
        self.right_child = None


def tree_maker(node,num_list):
    if not num_list:
        return
    node.value = num_list[0]
    bigger_index = len(num_list)
    for i,value in enumerate(num_list[1:]):
        if value >= num_list[0]:
            bigger_index = i+1
            break
    left_node = Node()
    node.left_child = left_node
    left_list = list(num_list)[1:bigger_index]
    tree_maker(left_node,tuple(left_list))
    right_node = Node()
    node.right_child = right_node
    right_list = list(num_list)[bigger_index:]
    for node in right_list:
        if node < num_list[0]:
            raise Exception('')
    tree_maker(right_node, tuple(right_list))

def tree_maker_mirror(node,num_list):
    if not num_list:
        return
    # print(num_list[0])
    node.value = num_list[0]
    bigger_index = len(num_list)
    for i,value in enumerate(num_list):
        if value < num_list[0]:
            bigger_index = i
            break
    left_node = Node()
    node.left_child = left_node
    left_list = list(num_list)[1:bigger_index]
    tree_maker_mirror(left_node,tuple(left_list))
    right_node = Node()
    node.right_child = right_node
    right_list = list(num_list)[bigger_index:]
    for node in right_list:
        if node >= num_list[0]:
            raise Exception('')
    tree_maker_mirror(right_node, tuple(right_list))

total = []
def post_order(node):
    if node is not None:
        post_order(node.left_child)
        post_order(node.right_child)
        if node.value:
            total.append(node.value)
if __name__ == '__main__':
    try:
        start_node = Node()
        input()
        data_list = list(map(lambda x: int(x) , input().split(' ')))
        if len(data_list)>=2 and data_list[0] >= data_list[1]:
            tree_maker(start_node,data_list)
        elif len(data_list)<2:
            print('Yes')
            print(data_list[0],end='')
            exit()
        else:
            tree_maker_mirror(start_node,data_list)
        print('YES')
        post_order(start_node)
        print(' '.join(map(str,total)),end='')
    except Exception as e:
        print('NO',end='')