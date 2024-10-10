def mergeIntervals(intervals):
    intervals.sort()
    output = [intervals[0]]
    for i in [k+1 for k in range(len(intervals)-1)]:
        current = intervals[i]
        if current[0] == output[-1][0]:
            output[-1][1] = current[1]
        elif current[0] <= output[-1][1]:
            if current[1] > output[-1][1]:
                output[-1][1] = current[1]
        else:
            output.append(current)
    return output


intervals = [[]]
print(mergeIntervals(intervals))

intervals = [[1,3]]
print(mergeIntervals(intervals))

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))