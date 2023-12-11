def sel_sort():
    marks = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        r = float(input("Enter marks inserted"))
        marks.append(r)
    print(marks)

    for i in range(len(marks)):
        min_m = i
        for j in range(i+1, len(marks)):
            if(marks[min_m] > marks[j]):
                temp = marks[min_m]
                marks[min_m] = marks[j]
                marks[j] = temp
    print("sorrted list")
    print(marks)
    if(n >= 5):
        a = marks[::-1]
        print("top 5 marks")
        for i in range(5):
            print(a[i])

def bubble_sort():
    marks = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        r = float(input("Enter marks inserted"))
        marks.append(r)
    print(marks)
    for i in range(n-1):
        for j in range(n-i-1):
            if(marks[j] > marks[j+1]):
                temp = marks[j]
                marks[j] = marks[j+1]
                marks[j+1] = temp
    print("The sorted list is :")
    print(marks)
    if(n >= 5):
        a = marks[::-1]
        print("The top 5 members are:")
        for i in range(5):
            print(a[i])

while(True):
    print("press 1: selection sort\n press 2 : bubble sort")
    d= int(input("Enter your choice"))
    if(d==1):
        sel_sort()
    elif(d==2):
        bubble_sort()
    else:
        print("Invalid entry")

