def b_search(l1,key):
    start = 0
    end = len(l1)
    while start<end:
        mid = (start+end)//2
        if l1[mid] > key :
            end = mid
        elif l1[mid] < key :
            start = mid-1
        else:
            return mid
    return -1

def main():

    dict1 = {}
    print("Enter exit to display phone numbers")
    while True:
        data = input("Enter name and mobile number, seperated by comma: ")
        if 'Exit' == data or 'exit' == data:
            break
        name, num = data.split(",")
        num = int(num)
        dict1[num] = name

    print(dict1)
    l1 = dict1.keys()
    l1 = list(l1)
    l1.sort()
    print(l1)

    key = int(input("The number to search for: "))

    index = b_search(l1, key)
    if index < 0:
        print("{} was not found.".format(key))
    else:
        print("{} was found at index {}.".format(key, index))
        print("Details of numbers found: ")
        print(dict1[key])

main()