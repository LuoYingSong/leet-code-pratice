# class Node():
#     def __init__(self,value):
#         self.value = int(value)
#         self.child = []
#
#     def add_child(self,child):
#         if child not in self.child:
#             self.child.append(child)
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#     def has_child(self):
#         if self.child:
#             return 0
#         return 1
#
# def main():
#     total_node,not_leaf_node = input().split(' ')
#     total_node_list = [Node('01')]
#     def check_in_node_list(node):
#         nonlocal total_node_list
#         if node in total_node_list:
#             father_node = total_node_list[total_node_list.index(node)]
#             return father_node
#         else:
#             total_node_list.append(node)
#             return node
#     for i in range(int(not_leaf_node)):
#         data = input().split(' ')
#         father_node = check_in_node_list(Node(data[0]))
#         for index in range(2,int(data[1])+2):
#             child_num = data[index]
#             father_node.add_child(check_in_node_list(Node(child_num)))
#     node_list = [total_node_list[0]]
#     total_count = []
#     while True:
#         next_level_node = []
#         count = 0
#         for node in node_list:
#             count += int(node.has_child())
#             next_level_node = next_level_node + node.child
#         total_count.append(count)
#         node_list = next_level_node
#         if not node_list:
#             break
#     print(' '.join(map(lambda x:str(x),list(total_count))),end='')
#
# if __name__ == '__main__':
data =  input().split(' ')
if len(data)!=2:
    exit()
total_node,not_leaf_node =data
num_dict = {}
child_dict = {}
for i in range(int(not_leaf_node)):
    father,child_num,*data = list(map(lambda x:int(x),input().split(' ')))
    num_dict[father] = child_num
    child_dict[father] = data
start_list = [1]
num_list = []
while True:
    child_list = []
    count = 0
    for num in start_list:
        if num not in num_dict:
            count+=1
        else:
            child_list += child_dict[num]
    num_list.append(count)
    start_list = child_list
    if not start_list:
        break
print(' '.join(map(lambda x:str(x),list(num_list))),end='')

