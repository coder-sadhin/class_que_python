from operator import index


lists=[0,1,2,3,4,5,6,7]
b = reversed(lists)
b=list(b)
c = b.index(4)
# print(b,c)

delwork=[True,1,0,'x',None,False,2,True]
delwork.pop(4)
# print(delwork)

list_a=[33,44,55,66,77,88]
indx=list(range(1,len(list_a),2))
indx.reverse()
for k in indx:
    list_a.pop(k)
print(list_a)