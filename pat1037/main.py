input()
ticket_list = list(map(int, input().split(' ')))
input()
item_list = list(map(int, input().split(' ')))
ticket_positive_list = list(sorted([ticket for ticket in ticket_list if ticket > 0],reverse=True))
ticket_negative_list = list(sorted([ticket for ticket in ticket_list if ticket < 0]))
item_positive_list = list(sorted([item for item in item_list if item >= 0],reverse=True))
item_negative_list = list(sorted([item for item in item_list if item < 0]))
count = 0
posi_length = min(len(ticket_positive_list),len(item_positive_list))
for ticket, item in zip(ticket_positive_list[:posi_length],item_positive_list[:posi_length]):
    count += item * ticket
neg_length = min(len(ticket_negative_list),len(item_negative_list))
for ticket, item in zip(ticket_negative_list[:neg_length],item_negative_list[:neg_length]):
    count += item * ticket
print(count)