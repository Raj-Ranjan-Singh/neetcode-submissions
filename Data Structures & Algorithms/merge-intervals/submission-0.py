class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        if len(intervals)==1:
            return intervals
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            last=res[-1]
            last_ed=last[1]
            last_st=last[0]
            curr_st=intervals[i][0]
            curr_ed=intervals[i][1]
            if last_ed>=curr_st:
                res.pop()
                res.append([last_st,max(curr_ed,last_ed)])
            else:
                res.append(intervals[i])
        return res