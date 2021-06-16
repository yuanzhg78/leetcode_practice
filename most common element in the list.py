def most_common(seq):
    d = {}
    for i in seq:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
       #d[i] = d.get(i, 0) + 1
    ret = []
    for j in sorted(d.items(), reverse=True, key=lambda x:x[1]):
        if len(ret) == 0:
            ret.append(j[0])
            n = j[1]
        else:
            if j[1] == n:
                ret.append(j[0])
            else:
                break
    return ret
print('频次最高',most_common([1,2,3,4,5,1,1,2,2]))
