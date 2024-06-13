def pos_neg_sort(lst):
    if not lst:
        return []
    n=len(lst)
    for i in range(n):
        if lst[i]<0:
            continue
        else:
            for j in range(i+1,n):
                if lst[i]>0 and lst[j]<lst[i]:
                    lst[i],lst[j]=lst[j],lst[i]
    return lst
    # positives_sorted = sorted([x for x in lst if x > 0])

    # # this is using iterator methods
    # pos_iter = iter(positives_sorted)
    # result1 = [next(pos_iter) if x > 0 else x for x in lst]

    # # this is using loop 
    # pos_index = 0
    # for i in range(len(lst)):
    #     if lst[i] > 0:
    #         lst[i] = positives_sorted[pos_index]
    #         pos_index += 1
        
    # return lst



lst1=pos_neg_sort([6,3,-2,5,-8,2,-2])
lst2=pos_neg_sort([6,5,4,-1,3,2,-1,1])
lst3=pos_neg_sort([-5,-5,-5,-5, 7,-5])

print(lst1)
print(lst2)
print(lst3)