class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals based on the start of each interval
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        #iterate starting from 1th one
        for start, end in intervals[1:] :
            #need to check if the intervals are overlapping
            #so check the start and end with the previous interval
            previousEnd = output[-1][1]

            if start <= previousEnd :
                #then overlapping, so merge them
                output[-1][1] = max(previousEnd, end)
            else :
                #not ovelapping
                output.append([start, end])

        return output
