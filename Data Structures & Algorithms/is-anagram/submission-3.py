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
        I use two hashmap to store the character frequencies of strings,first, count the frequency of character in both strings.
        for s, check if the current character in the hashmap1, if so,
        increase its count by 1, if not, set the count to 1. and for t,do the same thing. finally, compare
        two hashmaps,if they are equal, return true, if not, return false.
        '''