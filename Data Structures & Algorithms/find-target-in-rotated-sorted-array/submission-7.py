class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

"""
I use binary search.

First, I find the middle element. If it equals the target,
 I return the index.

Otherwise, I check which half is sorted. 
Then I check whether the target is inside that sorted half.

If it is, I search that half. Otherwise, I search the other half.

Each time, I remove half of the search range, 
so the time complexity is O(log n), and the space complexity is O(1).

"""

        
            
                
                
        