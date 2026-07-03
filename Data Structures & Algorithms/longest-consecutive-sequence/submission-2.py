class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for n in nums:
            if (n-1) not in numset:
                length=1
                while (n+length) in numset:
                    length+=1
                longest=max(length,longest)
        return longest

"""
I first put all numbers into a hash set so I can check 
whether a number exists in O(1) time.

Then I iterate through the numbers. I only start counting when the 
current number is the beginning of a sequence, which means n - 1 is not in the set.

From that starting point, I keep checking the next consecutive numbers 
until the sequence ends, and update the maximum length.

This way, every sequence is counted only once, so the overall time complexity is O(n).
"""
        

        