# PREFIX SUM 
# to find the sum of the given arr, and specifi index like (1,3)

"""arr=[2,6,1,4,3]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("original arr  ", arr)
print("prefix arr  ", prefix)

left=1
right=3
if left==0:
    answer=prefix[right]
else:
    answer= prefix[right]-prefix[left-1]
print("the sum is  ", answer)"""


# TWO POINTERS
# BEGIN WITH TWO POINTERS OF GIVEN ARRAYS USES TWO VARIABLES LEFT & RIGHT

# TWO SUM : check two sum == target 

"""def  sum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum == target:
            t=arr[left],arr[right]
        elif sum < target:
            left+=1
        else:
            right -=1
arr=[10,20,30,40,60]
target=30
s=sum(arr,target)
print(s)"""


# reverse array using two pointers

"""def reverse(arr):
    left=0
    right=len(arr)-1
    print("arr before reverse ",arr )
    while left < right:
        arr[left], arr[right]= arr[right], arr[left]
        left+=1
        right-=1
    return arr

arr=[10,20,30,40]
s=reverse(arr)
print("array after reverse>>>>",s)"""


# SLIDING WINDOW : MAXIMUM SUM OF SUBARRAY fixed size

"""def max_sum(arr,k):
    wind_sum=0
    for i in range(k):
        wind_sum+=arr[i]
    maximum=wind_sum
    for right in range(k,len(arr)):
        wind_sum+=arr[right]
        wind_sum-=arr[right-k]
        maximum=max(maximum,wind_sum)
    return maximum
arr=[1,2,3,4,5]
k=3
print(max_sum(arr,k))"""


# SLIDING WINDOW : LENGTH OF LONGEST SUBARRAY WHOSE SUM IS LESS THAN 7 <=7

"""def var(arr):
    left=0
    wind=0
    maximum=0
    for right in range(len(arr)):
        wind+=arr[right]
        while wind>7:
            wind-=arr[left]
            left +=1
        maximum=max(maximum , right-left+1)
    return maximum
arr=[1,2,3,4,5,6,2]
print(var(arr))"""


# SLIDING WINDOW : LENGTH OF LONGEST SUBARRAY WHOSE SUM IS LESS THAN 7 <=7 with elemnts 

"""def var(arr):
    left=0
    maximum=0
    wind=0
    max_wind=0
    for right in range(len(arr)):
        wind+=arr[right]
        while wind>7:
            wind -=arr[left]
            left+=1

        curent=right - left+1  #length of curr window 
        if wind == 7 and curent>maximum:
            maximum=curent
            max_wind=arr[left:right+1]    # windwo elements 
    return maximum,max_wind
arr=[1,2,3,4,5,2,3]
max,window=var(arr)
print("maximum length", max)
print("window",window)"""

def min(arr,target):
    left=0
    wind_sum=0
    minimum=float('inf')
    for right in range(len(arr)):
        wind_sum+=arr[right]
        while wind_sum>=target:
            current=right-left+1
            minimum=min(minimum,current )
            wind_sum-=arr[left]
            left+=1
    if minimum==float('inf'):
        return 0

    return minimum