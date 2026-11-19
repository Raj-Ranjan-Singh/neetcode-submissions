class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        map={}
        count=[[] for _ in range(len(nums))]
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1
        for key,val in map.items():
            if len(map)==1:
                res.append(key)
                return res
            count[val].append(key)
        for i in range(len(count)-1,-1,-1):
            if k==0:
                break
            if count[i]:
                for x in count[i]:
                    if k==0:
                        break
                    res.append(x)
                    k-=1

        return res