def accept(Group,a):

    for i in range(a):
        x = int(input("""Enter the marks of students
                         Enter -1 absent students"""))
        Group.append(x)

    print(Group)

def average(Group,a):

    add=0

    for i in Group:
        if(i>0):
            add = add + i

    avg = add/a

    return avg

def High(Group):

    highest = Group[0]
    for i in range(len(Group)):
        if(i>=0):
            if (i > highest):
                highest = Group[i]

    return highest

def Low(Group):

    lowest = Group[0]
    for i in range(len(Group)):
        if(i>=0):
            if (i < lowest):
                lowest = Group[i]

    return lowest

def absent(Group,a):

    count = 0
    for i in range(a):
        if Group[i]==-1:
            count += 1

    return count

def large_freq(Group,a):
    freq=0
    count = 0


    for i in range(a):
        if(i != -1):
            for j in range(a):
                if Group[i] == (Group[j]):
                    count += 1

        if(freq<count):
            mark=Group[i]
            freq=count


    return mark

def main():
    Marks = []
    N = int(input("Enter number of students in the class"))
    accept(Marks,N)

    flag = True

    while flag == True:

        print("Main Page")
        print("""1 for average score of class
                 2 for Highest Score & Lowest Score of Class
                 3 for Count of students who were absent for the test
                 4 for mark with highest frequency""")

        n = int(input("Enter the option you want to calculate"))

        if (n == 1):
            print("Average score of class", average(Marks,N))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif (n == 2):
            print(" Highest score", High(Marks),
                   " Lowest score of class ", Low(Marks))

            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif (n == 3):
            print("Count of students who were absent for the test", absent(Marks,N))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif (n == 4):
            print("Frequency, Mark with highest frequency",large_freq(Marks,N))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        else:
            print("invalid Input")
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")


main()










