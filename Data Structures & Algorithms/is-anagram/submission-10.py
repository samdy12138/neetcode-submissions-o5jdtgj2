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
        I use two hashmaps.

The first hashmap counts each character in string s.

The second hashmap counts each character in string t.

For each character, if it is already in the hashmap, I increase the count by 1.

If it is not in the hashmap, I add it and set the count to 1.

At the end, I compare the two hashmaps.

If they are the same, it means the two strings have the same characters with the same counts, so I return true.

Otherwise, I return false.

        '''