class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

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
''' I use two hash maps to store the character frequencies of strings s and t.
First, I check if the two strings have the same length. If not, they are not anagrams.
Then, I count the frequency of each character in both strings.
For s, if a character already exists in hashmap1, I increase its count by 1; 
otherwise, I set its count to 1. I do the same for t using hashmap2.
Finally, I compare the two hash maps. If they are equal, the strings are anagrams; otherwise, they are not.
'''



        