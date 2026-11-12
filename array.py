# An array is a collection of elements stored in a sequence 

"""arr=[1,2,3,4,5]   #array of 5 numbers 
print(arr)
ar=["anu","vani","chinnu"]     #array of strings 
print(ar)
an=[]        #array in empty list 
print(an)"""

# brute force : solve problem in the simplest direct way 

#largest num in arr

"""arr=[10,20,30]
largest=arr[0]          # Here len is 5 then loop runs 5times if it is 100 then it runs 100 times 
for num in arr:          # so here it depends on n so   the T,C is o(n)
    if num>largest:          # n.o(1) = o(n)    
        largest=num
print(largest)"""

#same question in different way 

"""arr=[10,20,30]
print(max(arr))"""

# T,C
# o(1) for 1 iteration
"""o(n) for n iteration , o(3) for 3 iteration like nested loops"""
#the loop travels all n elements once and each comparison takes constant time o(1) so total complexity is o(n)

# smallest element in arr

"""arr=[10,20,30]
smallest=arr[0]
for num in arr:
    if num <smallest:
        smallest= num
print(smallest)"""

# second largest element 

"""def large(arr):
    largest = arr[0]
    for num in arr:              # first & second loop runs n times o(n) 
        if num > largest:       # o(n)+o(n) = o(2n)= o(n)
            largest=num            # space complexoty large and second fixed variables (does not depend on array size)
    second =-1                          # so  S,C = o(1)  
    for num in arr:
        if num != largest and num> second :
            second = num
    return second
arr=[10,20,30,40,50]
print(large(arr))"""


# second smallest element in array 

"""def small(arr):
    smallest=arr[0]
    for num in arr:             
        if num <smallest:
            smallest=num             # time complexity us o(n)     space complexity o(1)
    second=float('inf')      # intially we set to largest posible value (innfinite value seting )
    for num in arr:          #goes through the loop onebyone and checsk 
        if num !=smallest and num<second:      #10!=5 and 10<infinityy 
            second=num                                 #second =10
    return second                         #supose if 20 was frist index than 10 was 2index the it would comapre 20 with
arr=[10,20,30,40,50]                   #10 and it wound beccome true 

print(small(arr))"""


# third largest value my code 

"""def large(arr):
    largest=arr[0]
    for num in arr:
        if num > largest:
            largest=num
    second=-1
    for num in arr:
        if num !=largest and num> arr[0]:
            second=num
    thrid=-1
    
    for num in arr:
        if num !=largest and num !=second:
            third=num
    return largest , second, third 
    

arr=[10,20,30,40]
largest , second, third = large(arr)        # here if we define only like ele=large(arr)then it will onlyreturn1value
print("the first largset value is ", largest)
print("the second  largset value is ",second)
print("the third  largset value is ", third)"""


# 1,2,3 smallest vlaue my code

"""def small(arr):
    smallest=arr[0]
    for num in arr:
        if num <smallest:
            smallest=num
    second=-1
    for num in arr:
        if num !=smallest and num <arr[0]:
            second=num
    third=-1
    for num in arr:
        if num !=smallest and num != second and num <arr[0]:
            third=num
    return smallest , second, third
arr=[10,2,5,3,46]
smallest, second,third=small(arr)
print("1st smallest value is ", smallest)
print("2st smallest value is ", second)
print("3st smallest value is ", third)"""


# chek if array is sorted my code 

"""def sorted(anu):
    for i in range(len(anu)-1):
        if anu[i]>anu[i+1]:
        
            return False
    return True
anu=[10,20,60,30,40]
vani=sorted(anu)
if vani == True:
    print("it is sorted")
else:
    print("it is not sorted ")"""


# reverse an array

"""def reverse_arr(arr):
    left=0
    right=len(arr)-1    # size-1 = index  
    while left<right:          #it keeps running unitl left crosses right because swapping is only needed until middle
        arr[left], arr[right]= arr[right],arr[left]
        left+=1        # move right pointer one step left  and right pointer -1 so that it swift to next value 
        right-=1
    return arr
arr=[10,20,30,40]
print(reverse_arr(arr))"""


#remove duplicaets from sorted array

"""def remove_duplicates(arr):
    if len(arr)==0:
        return []
    i=0                         # it points to 1st unique element =1
    for j in range(1,len(arr)):             # j starts from second element 
        if arr[i] != arr[j]:
            i+=1                                #j explores i stores
            arr[i] = arr[j]                       # copy vlaue of j into i 
    return arr[:i+1]
arr=[1,1,2,2,3,4,4]
print(remove_duplicates(arr))"""


# left rotate an array 

"""def lef_rotate(arr):
    temp=arr[0]                      #saves the first element becoz when shifting starts one would disappear 
    for i in range(len(arr)-1):         #size=5-1 = 4 the index is till 4  
        arr[i]= arr[i+1]                # index is stopped til 3 becoz we need to put 1st element in the 4 index 
    arr[len(arr)-1] = temp              # puts saved element at the end 
    return arr
arr=[1,2,3,4,5]                     # loop runs n-1 times so T,C is o(n)
print(lef_rotate(arr)) """              # temp extra variable so S,C is o(1)


# right rotate an array 

"""def right(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):        # 4,0,-1   elements are shifted from right becoz we cant shift from left 
        arr[i]=arr[i-1]                 #orelse it will be overritten 
    arr[0]=temp
    return arr                              # loop runs n-1 times so T,C is o(n)
arr=[1,2,3,4,5]                             # temp extra variable so S,C is o(1)
print(right(arr))"""

# move zeros to end 

# it moves all 0s to end and keeps non zeros in the same order  

"""def zeros(arr):
    i=0                     # i tells where next non zero should go 
    for j in range(len(arr)):           #j checks every elemnt 
        if arr[j]!=0:                   # is it non zero, is yes ->place it correclty , if zero -> skip 
            arr[i],arr[j]= arr[j], arr[i]           # swap non zeros into correct position 
            i+=1                            # move placement pointer forward 
    return arr              # j finds good numbers , i stores them 
arr=[1,0,2,0,3,0,4]                    # T,C is o(n)
print(zeros(arr))"""                # S,C is o(1)  


# union of two array -> take all unique elements from both arrays 

"""def union(arr1,arr2):
    return list(set(arr1)| set (arr2))        # converts arr to set 
arr1=[1,2,3,4]                           # | means union for sets 
arr2=[1,3,5,6]                  # set removes duplicates automatically 
print(union(arr1,arr2))
"""

# intersection of two array -> takes only common elments 

"""def inter(arr1,arr2):
    return list(set(arr1) & set(arr2))
arr1=[1,2,3,4]
arr2=[2,5,4]
print(inter(arr1,arr2))"""

# intersection brute force 

"""def search():
    arr1=[1,2,3,4]
    arr2=[2,3,4,5]
    for i in arr1:
        for j in arr2:
            if i == j:
                print(i)

search()"""


# missing number problem 

# first math-logic optimization array problem
# You are given numbers from 1 to n, But one number is missing , 
# Find that missing number.   
# T C 𝑂(n)2

"""def missing(arr,n):   # n-> largest num expected 
    expected = n*(n+1)//2     # find total sum if nothing missing
    actual = sum(arr)
    return expected - actual
arr=[1,2,4,5]
print(missing(arr,5))"""

