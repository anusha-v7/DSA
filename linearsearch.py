#linear search 

"""def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr=list(map(int, input("enter the elements").split()))
x=int(input("enter the element to search"))
result=search(arr,x)
print(result)
if result == -1:
    print("element not found")
else:
    print("element found at ", result)"""

#count occurence

"""def count(arr,x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count
arr=list(map(int,input("enter the array elements").split()))
print(arr)
x=int(input("enter the element ")) 
print(f"the element to be searched {x}")
total = count(arr,x)
print(f"the element occured {total} times")
if total == count:
    print(count)"""

#maximum value

"""def maxi(arr):
    max_val=arr[0]      #seting to 0 to compare eith one element 
    for num in arr:
        if num > max_val:
            max_val=num
    return max_val
arr=list(map(int, input("enter the array elements "). split()))
print(arr)
result = maxi(arr)
print("the maximum value is ", result)"""

#minimum value

"""def mini(arr):
    min_val=arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
            return min_val
arr=list(map(int, input("enter the elements"). split()))
print(arr)
result=mini(arr)
print("the minimum value is ", result)"""

#counting how many times it as occured and index

"""def count_first(arr,x):
    first=-1
    count=0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if first == -1:
                first=i
    return first, count 
arr=list(map(int,input("enter the elements "). split()))
x=int(input("enter the elemnt "))
result,count=count_first(arr,x)
if result == -1:
    print("element not found ")
else:
    print("element found at index", result)
    print("count", count)"""

# the elemnt in array where it is last occured 

"""def last(arr,x):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == x:
            return i
    return -1
arr=list(map(int,input("enter the element "). split()))
x=int(input("enter the element "))
result = last(arr, x)
if result == -1:
    print("element not found")
else:
    print("the element occured at ", result)"""
#checking if element exist or not

"""def check(arr,x):
    for i in arr:
        if i == x:
            return True
    return False
arr=list(map(int,input("enter element"). split()))
x=int(input("enter element"))
result=check(arr,x)
if result == True:
    print("the element exist ", result)
else:
    print("the element does not exist ")"""

#counting how amny elments are greter than x
"""def great(arr,x):
    count = 0
    for num in arr:
        if num > x:
            count +=1
    return count
arr=list(map(int,input("enter element"). split()))
x=int(input("enter element"))
result=great(arr,x)
print("the elements greater than x are ", result)"""

#checking how many elements are greater smaller equal than x
"""def count(arr,x):
    greater = 0
    small = 0
    equal = 0
    for num in arr:
        if num > x:
            greater += 1
        elif num < x:
            small +=1
        else:
            equal +=1
    return greater, small, equal
arr=list(map(int,input("enter element"). split()))
x=int(input("enter element"))
g,s,e=count(arr,x)
print("the elment greater the ", x, "are", g)
print("the elements smaller than ", x, "are",s)
print("the elements equal are", x,"are", e)
"""
#sum of the array
"""def sum(arr):
    total=0
    for num in arr:
        total+=num
    return total
arr=list(map(int,input("enter the element").split()))
result=sum(arr)
print("the sum of the array is", result)
"""
#counting even and odd numbers 
"""def count(arr):
    even = 0
    even_num=[]
    odd = 0
    odd_num=[]
    for num in arr:
        if num % 2 == 0:
            even +=1
            even_num.append(num)
        else:
            odd +=1
            odd_num.append(num)
    return even, odd,even_num,odd_num
arr=list(map(int,input("enter the element").split()))
result,con,vani,chinnu=count(arr)
print("the even numbers are ", result)
print("the odd num are ", con)
print("the even numbers count are ", vani)
print("the odd num are ",chinnu)
"""
#reversing array without complex
"""rev=[1,2,3,4,5]
print(rev)
rev.reverse()
print(rev)"""



