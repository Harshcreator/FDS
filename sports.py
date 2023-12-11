def main():
    Group_A = []
    Group_B = []
    Group_C = []
    Group_Main = []

    accept(Group_Main,"All roll numbers")
    accept(Group_A,"Cricket")
    accept(Group_B,"Badminton")
    accept(Group_C,"Football")
    
    flag = True

    while (flag==True) :
        print("Menu: ")
        print("""1 for list of students who play both cricket and badminton 
             2 for students who play either cricket or badminton but not both
             3 for students who play neither cricket nor badminton
             4 for students who play cricket and football but not badminton""")
        n=int(input("Enter your choice"))

        if (n==1):
            print("list of students who play both cricket and badminton", inter(Group_A,Group_B))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif(n==2):
            print("list of students who play either cricket or badminton but not both", union(difference(Group_A, Group_B), difference(Group_B, Group_A)))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif(n==3):
            print("List of students who play neither cricket nor badminton", difference(Group_Main,union(Group_A,Group_B)))
            a = input("\n\nDo you want to continue (yes/no) :")
            if a == "yes":
                flag = True
            else:
                flag = False
                print("Thanks for using this program!")

        elif(n==4):
            print("list of students who play cricket and football but not badminton", difference(inter(Group_A,Group_B),Group_C))
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

def accept(grp,str):

    n = int(input("Enter number of students %s" %str))
    for i in range(n):
        x = input("Roll number %d of students who play %s :" %((i+1),str))
        grp.append(x)
    print(grp)

def inter(a,b):

    result = []

    for i in a:
        if i in b:
            result.append(i)
    
    return result

def union(a,b):

    result = []

    result = a.copy()

    for i in b :
        if i not in result:
            result.append(i)
    
    return result

def difference(a,b):

    result = []

    for i in a:
        if i not in b:
            result.append(i)
    
    return result

main()


