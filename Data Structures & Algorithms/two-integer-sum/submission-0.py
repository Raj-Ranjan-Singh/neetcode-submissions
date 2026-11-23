class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        res=[]
        for i in range(len(nums)):
            if(target-nums[i]) in map:
                res.extend([map.get(target-nums[i]),i])
                return res
            map[nums[i]] = i
        return res