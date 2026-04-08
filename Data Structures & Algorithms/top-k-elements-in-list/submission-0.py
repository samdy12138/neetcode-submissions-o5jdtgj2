class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        arr=[]
        for num in count:
            times=count[num]
            arr.append((num,times))
        
        arr.sort(key=lambda x:x[1],reverse=True)

        res=[]
        i=0
        while i<k:
            res.append(arr[i][0])
            i+=1
        return res


        '''
        先统计 再转成列表 再排序 再取前k个
        '''