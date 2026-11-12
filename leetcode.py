# TWo sum
class solution():
    def twosum(self,nums,target):
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                total=nums[i]+nums[j]
                if total == target:
                    return [i,j]
s=solution()
nums=[10,20,30,40,50]
target=70
print(s.twosum(nums,target))    # in lc not asked to print 


# VALID PALINDROME USING TWO POINTER TECHNIQUE 
class solution():
    def pal(self,s):
        left=0           
        right=len(s)-1
        while left<right:
            while left< right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right-=1
            if s[left].lower()!= s[right].lower():
                return False
            left +=1
            right-=1
        return True

s="m,a,d,a,m"
a=solution()
print(a.pal(s))