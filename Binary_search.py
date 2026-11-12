# binary search 

# binary search is a method to find an elemnt in a sorted array by 
# repeatedly dividing the search space into half .
# divide -> check -> eliminate half -> repeat 
# """array must be sorted >>>"""
# left → starting index
# right → ending index
# mid → middle index

"""formula  for mid = left + right //2""" 
""" If arr[mid] == target → return index
    If target > arr[mid] → search right side
    If target < arr[mid] → search left side """

"""if we use len(arr)-1 , the the lenght will be 5 but there will be no 
index 5 so len(arr)-1"""
""" // 2 it gives the whole number not decimal """

#binary search
"""
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1  # this len=5-1

    while left <= right:
        mid = (left + right) // 2    # // this gives int value instead of 3.0

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    return -1

#  MAIN FUNCTION (Driver Code)
def main():
    n = int(input("Enter number of elements: "))
    
    arr = []
    print("Enter elements in sorted order:")
    for i in range(n):
        x = int(input())
        arr.append(x)
    
    target = int(input("Enter element to search: "))

    result = binary_search(arr, target)

    if result == -1:
        print("Element not found")
    else:
        print("Element found at index:", result)


# Run the program
main()
"""

"""def search(arr,x):
    left = 0
    right = len(arr)-1
    while left <= right :
        mid = (left+right) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid +1
        else:
            right = mid -1

def main():
    n=int(input("enter the size of array"))
    arr=[]
    print("enter the elemnt of array ")
    for i in range(n):
        tar=int(input())
        arr.append(tar)
    x=int(input("enter the elemnt ot search  "))
    result=search(arr,x)
    if result == -1:
        print("elemnet not found ")
    else:
        print("element found at ", result)
main()"""

#NORMAL BINARY SEARCH

"""def search(arr,x):
    left = 0
    right = len(arr)-1   #if len is 5 then index is 4 so= 5-1=4
    while left <= right:
        mid= (left+right)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            left = mid +1
        else:
            right = mid -1
arr=list(map(int,input("enter the array eleements ").split()))
arr.sort()
x=int(input("enter the lement to search"))
result=search(arr,x)
if result == -1:
    print("element not found ")
else:
    print("elment found at ", result )"""


"""def search(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1
arr=[1,2,3,2]
x=int(input("enter the element"))
result=search(arr,x)
if result == -1:
    print("element not found ")
else:
    print("element found ",result )
"""

#first to last occurenece value 

"""def first(arr,x):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid] == x:
            result= mid
            right=mid-1
        elif arr[mid]< x:
            left= mid +1           
        else:
            right=mid-1
    return result 

def last(arr,x):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid =(left+right)//2
        if arr[mid] == x:
            result= mid
            left=mid+1
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return result 
arr=list(map(int,input("enter number").split()))
arr.sort()
print(arr)
x=int(input("enter elements "))
one=first(arr,x)
two=last(arr,x)
if one == -1:
    print("element not found ")
else:
    print("all occurenece indices ", list(range(one,two+1)))"""

#finding how many duplicated values are there

def first(arr,x):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid][0] == x:     #(value, original_index)
            result=mid
            right=mid-1
        elif arr[mid][0]<x:
            left = mid+1
        else:
            right =mid-1
    return result 

def last(arr,x):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid][0]==x:
            result=mid
            left = mid+1
        elif arr[mid][0]<x:
            left = mid + 1
        else:
            right = mid-1
    return result 
arr=list(map(int,input("enter the eleemnts ").split()))
x=int(input("enter the element to search"))
arr_index=[(arr[i],i)for i in range(len(arr))]     #creates (value,original index)
arr_index.sort()
one=first(arr_index,x)
two=last(arr_index,x)
if one  == -1:
    print("element not found ")
else:
    original_indices = [arr_index[i][1] for i in range(one, two + 1)]  #(1,3+1), itcreates list 
    print("Original indices:", original_indices)





