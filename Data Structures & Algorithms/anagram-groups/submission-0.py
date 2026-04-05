class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            word1=sorted(word)
            key=""
            for ch in word1:
                key+=ch
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]
                
        return list(hashmap.values())