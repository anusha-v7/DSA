# kadane alg : used to find sum of contigues subarray , means the elemnets 
# must be next to each other 
# arr=[1,2,3]    = [1] [1,2] [1,2,3] [2,3]
#now sum is 1, 3, 6, 5 ===> now max sum is 6

# why we need ==> easiets way to think prolem we could generate every possible subarray and calculate 
# its sum 

# For an array of size n, there can be approximately:  n sqr
# brute force takes o(n sqr) but kadane solves in o(n)


def max_subarray(arr):
    current_sum = arr[0]
    maximum_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum + arr[i])
        maximum_sum = max(maximum_sum,current_sum)
    return maximum_sum

arr=[1,2,4,5,6,2,5]

print(max_subarray(arr))
