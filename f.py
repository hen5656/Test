intervals = [2,1, 1, 1, 1, 4,4,4, 3,4,1,1,1]
const = intervals[0]
index_start = 0
index_end = 1
i = 1
count = 1
flag=0
j=len(intervals)-2
d = {}
for interval in intervals[1:len(intervals)]:
    if const == interval:
        if flag == 0:
            index_start = i
            flag = 1
        count = count + 1
        index_end = i

    else:
        if (index_start, index_end) not in d and count > 1:
            d[(index_start, index_end + 1)] = count
        const = interval
        count = 1
        flag = 0

    if i==j: #last iteration
        if (index_start, index_end) not in d and count > 1:
            d[(index_start, index_end + 1)] = count

    i = i + 1

print("done")