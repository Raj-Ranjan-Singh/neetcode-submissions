class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in nums:
        #     c=0
        #     for j in nums:
        #         if i==j:
        #             c+=1
        #             if c==2:
        #                 return True
        # return False
        d = set()
        for num in nums:
            if num in d:
                return True
            d.add(num)
        return False
        
        