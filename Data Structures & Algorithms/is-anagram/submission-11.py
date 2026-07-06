class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}

        for ch in s:
            if ch in hashmap1:
                hashmap1[ch]+=1
            else:
                hashmap1[ch]=1
        for ch in t:
            if ch in hashmap2:
                hashmap2[ch]+=1
            else:
                hashmap2[ch]=1
        return hashmap1==hashmap2
        '''
 I use two hashmaps to count characters.

One hashmap is for string s, and the other one is for string t.

I count how many times each character appears in both strings.

Then I compare the two hashmaps.

If they are the same, I return true.

If they are different, I return false.


        '''