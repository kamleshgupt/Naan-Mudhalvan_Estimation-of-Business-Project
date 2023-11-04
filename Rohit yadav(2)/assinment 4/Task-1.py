# create two list and join those two list

l=[[1,2,3],[4,5,6]]
l2=[[11,12,13],[12,12,12]]
for i in range(2):
    for j in   range(3):
        l[i][j]+=l2[i][j]
print(l)
