class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return[hashmap[complement],i]
            else:
                hashmap[num]=i
'''first I use the hashmap to store the numbers and their indices, 
then I iterate through the list with index and number, 
for each number, I calculate complement as target minus number, 
and check if the complement is in the hashmap,if it exists, 
then return the indices, if not exist,store the current number in the hashmap'''
'''The time complexity is O(n).'''
        