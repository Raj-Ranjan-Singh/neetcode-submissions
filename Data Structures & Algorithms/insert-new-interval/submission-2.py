class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return [newInterval]

        curr_st=newInterval[0]
        curr_ed=newInterval[1]
        if(len(intervals)==1):
            last_st=intervals[-1][0]
            last_ed=intervals[-1][1]
            if not (curr_st==curr_ed==0) and last_ed>=curr_st:
                return [[min(last_st,curr_st),max(last_ed,curr_ed)]]
            else:
                intervals.append(newInterval)
                intervals.sort()
                return intervals
        in_pt=0
        l=0;h=n-1
        while(l<=h):
            mid=l+(h-l)//2
            if mid==n-1 and newInterval[0]>=intervals[mid][0]:
                in_pt=n
                break
            if intervals[mid+1][0]>newInterval[0]>=intervals[mid][0]:
                in_pt=mid+1
                break
            else:
                if intervals[mid][0]>newInterval[0]:
                    h=mid-1
                else:
                    l=mid+1
        # print(in_pt)
        intervals.insert(in_pt, newInterval)
        # print(intervals)
        res=[intervals[0]]
        # print(res)
        for i in range(1,n+1):
            last_st=res[-1][0]
            last_ed=res[-1][1]
            curr_st=intervals[i][0]
            curr_ed=intervals[i][1]
            if(last_ed>=curr_st):
                res.pop()
                res.append([last_st,max(last_ed,curr_ed)])
                # print(res)
            else:
                res.append(intervals[i])
        return res
