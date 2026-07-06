class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k=set()
        for num in nums:
            if num in k:
                return True
            else:
                k.add(num)
        return False
        ''' I use the set to store numbers, I iterate the array and 
        check if the current number in the set , if so, return true. if 
        not, add the current number in the set.Finally if there are no 
        duplicates, return false.
        '''