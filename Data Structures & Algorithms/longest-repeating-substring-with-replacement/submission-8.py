class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        max1=0
        count={}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            max1=max(max1,count[s[r]])
            while (r-l+1)-max1>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
"""
I use a sliding window.

I use a hash map to count how many times each character appears 
in the window. I also keep the count of the most common character.

For each window, the number of characters I need to change is:

window size minus the most common character count.

If this number is greater than `k`, the window is not valid, 
so I move the left pointer.

If the window is valid, I update the answer.

The time complexity is O(n).


"""

        
        
        
        