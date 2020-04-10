n = int(input())
year2id = {}
keyword2id = {}
publisher2id = {}
author2id = {}
title2id = {}
for i in range(n):
    id_ = input()
    title = input()
    author = input()
    keyword = input()
    publisher = input()
    year = input()
    if year in year2id:
        year2id[year].append(id_)
    else:
        year2id[year] = [id_]
    if author in author2id:
        author2id[author].append(id_)
    else:
        author2id[author] = [id_]
    if keyword in keyword2id:
        keyword2id[keyword].append(id_)
    else:
        keyword2id[keyword] = [id_]
    if publisher in publisher2id:
        publisher2id[publisher].append(id_)
    else:
        publisher2id[publisher]=[id_]
    if title in title2id:
        title2id[title].append(id_)
    else:
        title2id[title] = [id_]
type2dict = {'1':title2id,'2':author2id,'3':keyword2id,'4':publisher2id,'5':year2id}
query = []
for i in range(int(input())):
    type_,context = input().split(':')
    query.append([type_,context.strip()])
for type_,context in query:
    print('{}: {}'.format(type_,context))
    if type_ == '3':
        saver = []
        for k,v in keyword2id.items():
            if context in k:
                saver += v
        if not saver:
            print('Not Found')
        else:
            print('\n'.join(sorted(saver)))
    else:
        try:
            print('\n'.join(sorted(type2dict[type_][context])))
        except KeyError:
            print('Not Found')