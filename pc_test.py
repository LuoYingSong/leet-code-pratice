from string import ascii_lowercase,ascii_uppercase


def encode(string, step):
    saver = []
    for word in string:
        if word in ascii_lowercase:
            i = ascii_lowercase.index(word)
            i += step
            if i >= len(ascii_lowercase):
                i -= 24
            elif i < 0:
                i += 24
            saver.append(ascii_lowercase[i])
        else:
            i = ascii_uppercase.index(word)
            i += step
            if i >= len(ascii_lowercase):
                i -= 24
            elif i < 0:
                i += 24
            saver.append(ascii_uppercase[i])
    return ''.join(saver)

if __name__ == '__main__':
    print(encode('SOS',3))
