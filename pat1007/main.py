if __name__ == '__main__':
    input()
    history = {}
    data_history = {}
    data = list(map(lambda x:int(x),input().split(' ')))
    for i in range(len(data)):
        history[i] = []
        data_history[i] = []
        if i == len(data):
            continue
        for j in range(i,len(data)):
            history[i].append(sum(data[i:j]))
            data_history[i].append(data[i:j])
    data2 = dict(zip(history.keys(),list(map(lambda x:max(x),history.values()))))
    max_key,max_value = -1,-1
    for key in data2.keys():
        if data2[key] > max_value:
            max_key = key
            max_value = data2[key]
    seq=data_history[max_key][history[max_key].index(max_value)]
    if max_value < 0:
        is_negative = True
        for num in seq:
            if num>0:
                is_negative = False
        if is_negative:
            max_value=0
    print(max_value,seq[0],seq[-1],end='')