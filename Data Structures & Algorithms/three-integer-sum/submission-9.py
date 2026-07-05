class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res

"""
I first sort the array.

Then I fix one number and use two pointers to find the other two numbers.

If the sum is too small, I move the left pointer to get a bigger number.

If the sum is too large, I move the right pointer to get a smaller number.

If the sum is zero, I add the three numbers to the result.

I also skip duplicate numbers, so the result will not have repeated triplets.

The time complexity is O(n squared), and the extra space complexity is O(1).

"""
        