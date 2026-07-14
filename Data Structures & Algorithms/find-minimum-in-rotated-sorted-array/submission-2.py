class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
"""
 I use binary search.

I compare the middle number with the right number.

If the middle number is bigger, the minimum is on the right.

Otherwise, the minimum is on the left, including the middle.

When the two pointers meet, I return that number.

The time complexity is O(log n).

"""
        