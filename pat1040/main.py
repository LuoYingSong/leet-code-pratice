string = input()
max_length = 0
for i in range(1, len(string)-1):
    if string[i - 1] == string[i + 1]:
        length = 3
        find_index = 2
        while i - find_index >= 0 and i + find_index < len(string):
            if string[i-find_index] == string[i+find_index]:
                length += 2
                find_index += 1
            else:
                break
        if length > max_length:
            max_length = length
    if string[i] == string[i + 1]:
        length = 2
        find_index = 2
        while i - find_index + 1 >= 0 and i + find_index < len(string):
            if string[i - find_index+1] == string[i + find_index]:
                length += 2
                find_index += 1
            else:
                break
        if length > max_length:
            max_length = length
print(max_length)
