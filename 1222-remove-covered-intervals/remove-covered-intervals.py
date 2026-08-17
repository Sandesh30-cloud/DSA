class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cnt = 0
        m_end = 0
        for start, end in intervals:
            if end > m_end:
                cnt +=1
                m_end = end
        return cnt
        