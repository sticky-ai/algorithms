# 178 chars
import collections
c, u = eval(dir()[0])
d = collections.defaultdict(list)
for i in c:
    d[i[0]] = i[1:]
for j in u:
    if j[1] not in d[j[0]]:
        d[j[0]].append(j[1])
return sorted([k] + sorted(v) for k, v in d.items())

# 208 chars
# import collections
# def catalogUpdate(catalog, updates):
#     d = collections.defaultdict(list)
#     for c in catalog:
#         d[c[0]] = c[1:]
    
#     for u in updates:
#         if u[1] not in d[u[0]]:
#             d[u[0]].append(u[1])
    
#     return sorted([[k] + sorted(v) for k, v in d.items()])
