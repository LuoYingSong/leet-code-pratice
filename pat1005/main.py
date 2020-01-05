num_english = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
               6:'six',7:'seven',8:'eight',9:'nine'}

num_str = input()
total = 0
for num in num_str:
    total += int(num)
total_str = []
for num in str(total):
    total_str.append(num_english[int(num)])
print(' '.join(total_str),end='')