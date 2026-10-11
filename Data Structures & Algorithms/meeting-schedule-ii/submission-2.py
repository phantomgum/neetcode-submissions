"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #first sort the intervals by their start times
        #O(nlogn)
        intervals.sort(key = lambda i : i.start)

        #min heap to store the end times of current meetings
        minHeap = []

        for meeting in intervals :
            #check if heap is empty
            if minHeap :
                #check if start time is greater than current
                #meeting end time
                if meeting.start >= minHeap[0] :
                    #remove that old meeting
                    heapq.heappop(minHeap)
                    #add the current meeting
                    heapq.heappush(minHeap, meeting.end)
                elif meeting.start < minHeap[0] : 
                    #room isn't available
                    heapq.heappush(minHeap, meeting.end)    
            else :
                #no othe meetings in progress
                heapq.heappush(minHeap, meeting.end)
        return len(minHeap)


