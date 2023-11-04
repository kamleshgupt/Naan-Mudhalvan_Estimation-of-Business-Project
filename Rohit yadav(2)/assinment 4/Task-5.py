'''
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0,7)
'''
def sum_of_all(list1):
    return sum(list1)
res=sum_of_all([8,2,3,0,7])
print(res)

#2bs ways with logic
def  sum_of_list(*list1):
    ans=0
    for i in list1:
        ans+=i
    return ans
res2=sum_of_list(8,2,3,0,7)
print(res2)
