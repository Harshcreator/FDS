def partition(per, start, end):
    pivot = per[start]
    low = start+1
    high = end-1

    while True:
        while low <= high and per[high] >= pivot :
            high = high - 1
        while low <= high and per[low] <= pivot :
            low = low + 1
        if low <= high :
            per[low], per[high] = per[high], per[low]
        else:
            break
    per[start], per[high] = per[high], per[start]

    return high

def quick_sort(per, start, end):
    if start >= end :
        return
    p = partition(per, start, end)
    quick_sort(per, start, p)
    quick_sort(per, p+1, end)

per = []
n = int(input("Enter total number of students:"))
for i in range(n):
    value = float(input("Enter the percentage"))
    per.append(value)
quick_sort(per, 0, len(per))
print(per)
print("Top 5 scores are:", per)
minimum = len(per)-6
maximum = len(per)-1
index = 1
for i in range(maximum, minimum, -1):
    if i>=0 :
        print(f"{index} Top Scorer:", per[i])
        index+=1







