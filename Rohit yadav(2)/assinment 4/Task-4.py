#create a function  to find a odd number

def find_odd(num):
    if num%2!=0:
        return "odd"
    return False
num=int(input("enter a number"))
res=find_odd(num)
print(res)
