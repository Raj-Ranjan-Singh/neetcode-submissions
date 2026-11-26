class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0;j=0;curr=0;max_=float('-inf');n=len(nums)
        while(i<=j and j<n):
            if curr<0:
                i=j
                curr=0
            if j==n and i!=n-1:
                i+=1
                j=i
                curr=0
            curr+=nums[j]
            max_=max(curr,max_)
            j+=1
        return max_