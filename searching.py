#liner search 
"""
def search(arr,x):
    n=len(arr)
    for i in range(n):
        if (arr[i]==x):
            return i
    return -1
arr=[10,20,30,40,50]
print(arr)
x=int(input("enter the elemetn to search"))
result=search(arr,x)
if result == -1:
    print("element not found")
else:
    print("the element is found as index",result)
"""

#linear search 


"""def search(arr,x):
    n=len(arr)
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1
arr=[10,20,30,40,50]
x=int(input("enter the element to saearch"))
result=search(arr,x)
if result == -1:
    print("the element is not found ")
else:
    print("the element is found at index",result)"""


# to understand clearly what is i and n 
"""arr=[10,20,30]
for i in range(len(arr)):
    print(i,arr[i]) """

#print the index of the searching element 
"""def index(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[10,20,30]
print(index(arr,20))"""

# the element which we are searching, from where to where it is in arr
"""def first_last(arr, x):
    first = -1
    last = -1
    
    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
            
    return first, last

# Example
arr = [1, 2, 3, 2, 4, 2]
print(first_last(arr, 2))"""  


#search using classs

"""class solution:
    def search (self,arr,x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
n=int(input(" enter"))     #size no need
arr=list(map(int,input().split()))
x=int(input("enter to search "))
obj=solution()
print(obj.search(arr,x))"""

#linear search my code
"""def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[10,20,30,40,50]
x=int(input("enter the element"))
result=search(arr,x)
if result==-1:
    print("element not found")
else:
    print("element found at place",result)"""

#counting elemts in array
"""class Solution:
    def search (self,arr,x):
        count=0
        for num in arr:
            if num == x:
                 count+=1
        return count
arr=[10,20,30,20,50]
x=int(input("enter element"))
result=Solution()
print(result.search(arr,x))"""


"""def first(arr,x):
    for i, num in enumerate(arr):
        if num == x:
            return i
    return -1
arr=list(map(int,input().split()))
x=int(input())
result=first(arr,x)
if result == -1:
    print("no occurenece")
else:
    print("the occurence",result)"""
        
# linear search with eunmarate and enter elements down by down
#enumarate means it prints both index and value

def search(arr,x):
    for i,num in enumerate(arr):
        if arr[i]==x:
            print("index ",i, "value ", num)
            return i
    return -1
n=int(input("enter the size of the arr"))
arr=[]
for i in range(n):
    num=int(input("enter the array eleemnt"))
    arr.append(num)
x=int(input("enter the element to search"))
result=search(arr,x)
if result == -1:
    print("elememt not found")
else:
    print("elemnt found at ", result)