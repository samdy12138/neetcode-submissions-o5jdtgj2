class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k=set()
        for num in nums:
            if num in k:
                return True
            else:
                k.add(num)
        return False
''' first, I use the set to store the numbers, 
Then I iterate through the array and check if the current number 
is already in the set. if so, return true, 
if not, add the number to the set, 
Finally, if no duplicates are found, I return false.
'''
        
        