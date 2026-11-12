#gfg
# arrays 
#1.linear traversal

"""arr=[10,20,30,40,50]
for i in (arr):
    print(i,end=" ")
print()"""       # just next line prints 

#2.reverse traversal

"""arr=[10,22,30,40,50]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")          #for value arr[i] , fo rindex i """

#traverse using while loop

"""arr=[10,20,30]
i=0
n=len(arr)
while i<n:
    print(arr[i],end=" ")
    i+=1                        #it will run infinite 
print()"""

#searching elemnt in arr

"""arr=[10,20,30]
tar=30
found=False
val=0
for i in range(len(arr)):
    if arr[i] == tar:
        val=i
        found=True
        break
if found==True:
    print('the value found at ',val)
else:
    print("not found ")
"""

#  inserting element 

"""arr=[10,20,30]
val=50
print("arr before insertion ",arr)
arr.insert(0,val)
print("arr after insertion ",arr)"""

# liner search 

"""def search(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i] == x:
            return i 
    return -1
arr=[10,20,30]
x=10
result=search(arr,x)
if result == -1:
    print("element not found")
else:
    print("eleemnt found at ", result )"""

# binary search

"""def search(arr,x):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid]<x:
            left+=1
        else:
            right-=1
    return -1                           # T C o(log)n
arr=[10,20,30]
x=20
result=search(arr,x)
if result == -1:
    print("elemnt not found ")
else:
    print("elemnt found at index ", result )"""


def first(arr,x):
    left=0
    right=len(arr)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            ans=mid
            right=mid-1
        elif arr[mid]<x:
            left =mid+1
        else:
            right =mid-1
    return ans 

def last(arr,x):
    left=0
    right=len(arr)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            ans=mid
            left = mid +1
        elif arr[mid]<x:
            left= mid+1
        else:
            right = mid-1
    return ans 

arr=[10,20,30,40,30]    # not sorted doesnt work 
x=30

print("first occured at ,", first(arr,x))
print("second t occured at ,",last(arr,x))