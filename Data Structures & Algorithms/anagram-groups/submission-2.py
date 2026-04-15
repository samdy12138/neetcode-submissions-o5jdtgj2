class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            key="".join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]
        return list(hashmap.values())
        
        '''
        I use a hashmap to group words.
        For each word, I sort it and use the sorted string as a key.
        If the key is already in the hashmap, I add the word to that group.
        If not, I create a new group.
        At the end, I return all the groups.
        '''