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
        