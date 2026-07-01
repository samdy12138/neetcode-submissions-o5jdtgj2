class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        freq=[[] for _ in range(len(nums)+1)]
        for num,c in count.items():
            freq[c].append(num)
        res=[]
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

'''
I solve this using a bucket sort approach.

First, I count the frequency of each number using a hashmap.

Then, I create buckets where the index represents the frequency, 
and each bucket stores numbers with that frequency.

After that, I iterate through the hashmap and put each number 
into its corresponding bucket.

Finally, I iterate from the highest frequency to the lowest, 
and collect elements until I get k results.

This approach runs in O(n) time and avoids sorting.
'''