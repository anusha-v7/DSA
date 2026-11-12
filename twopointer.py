#structure 
"""     left=0
right=len(arr)-1
while left<right:
    left+=1
    right-=1        """

# reverse an array using two pointer 

"""arr=[10,20,30,40,50]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)"""

# Two sum 
"""arr=[10,20,30,40,50]
target=70
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total == target:
        print(left,right)
        break
    elif total <target:
        left+=1
    else:
        right-=1
        """

"""class solution():
    def twosum(self,nums,target):
        num_hash={}
        for i in range(len(nums)):
            if target-nums[i] in num_hash:
                return [num_hash[target - nums[i]],i]
            num_hash[nums[i]]=i
s=solution()
nums=[10,20,30,40,50]
target=70
s.twosum(nums,target)"""

"""class solution():
    def twosum(self,nums,target):
        hash_map={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hash_map:
                print(hash_map[diff],i)
s=solution()
nums=[10,20,30,40,50]
target=70
s.twosum(nums,target)"""


