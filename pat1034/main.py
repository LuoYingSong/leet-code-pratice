relate, threshold = list(map(int,input().split(' ')))
clusters = []
cluster2time = {}
people2time = {}
for i in range(relate):
    a, b, time = input().split(' ')
    time = int(time)
    flag = 0
    for i,cluster in enumerate(clusters):
        if a in cluster:
            flag = 1
            people2time[a] += time
            cluster2time[i] += time
            if b not in cluster:
                cluster.append(b)
                people2time[b] = time
            else:
                people2time[b] += time
            break
        elif b in cluster:
            flag = 1
            cluster2time[i] += time
            people2time[b] += time
            if a not in cluster:
                cluster.append(a)
                people2time[a] = time
            else:
                people2time[a] += time
            break
    if not flag:
        clusters.append([a,b])
        cluster2time[len(clusters)-1] = time
        people2time[a] = time
        people2time[b] = time
clusters_dict = {}
saver = []
for i,cluster in enumerate(clusters):
    if len(cluster)>2 and cluster2time[i] >= threshold:
        sum_call_time = cluster2time[i]
        saver.append([max(sorted(cluster),key=lambda x:people2time[x]),len(cluster)])
print(len(saver))
for i in sorted(saver,key=lambda x:x[0]):
    print(" ".join(map(str,i)))