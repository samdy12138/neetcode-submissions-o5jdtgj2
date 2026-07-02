class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

"""
I solve this problem using prefix and postfix products.

In the first pass, I calculate the product of all elements to the 
left of each position and store it in the result array.

In the second pass, I traverse from right to left while 
maintaining a postfix product, which is the product of all elements to the right. 
I multiply this postfix product with the value already stored in the result array.

After these two passes, each position contains 
the product of all elements except itself.

This approach runs in O(n) time and uses O(1) extra space, 
excluding the output array.
"""
        