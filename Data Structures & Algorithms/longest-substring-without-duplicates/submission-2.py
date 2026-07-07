class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res, r-l+1)
        return res

"""
I use a sliding window and a set.

The set stores the characters in the current window.

I move the right pointer one by one.

If I see a duplicate character,
 I move the left pointer and remove characters until there is no duplicate.

Then I update the max length.

Finally, I return the max length.

Time complexity is O(n), and space complexity is O(n).

"""
        