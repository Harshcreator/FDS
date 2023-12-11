def accept(A):
     n=int(input("enter the no of elements"))
     for i in range(n):
        x=int(input("enter mobile no of %d students "%(i+1)))
        A.append(x)
     
def display(A):
    n=len(A)

    for i in range (0,n):
        print(A[i])
    
def linear_search(A,x):
    n=len(A)
    
    x=int(input("enter the element to search"))
    l=0
    for i in range (n):
        if(A[i]==x):
            l=1
            break
        else:
            l=0
    if(l==1):
        print("present")
    else:
        print("not present")
            
                        
def sentinal_search(A,x):
    x=int(input("enter the element to search"))
    n=len(A)
    last=A[n-1]
    A[n-1]=x
    i=0
    while(x!=A[i]):
        i=i+1
    A[n-1]=last
    if(i<(n-1) or x==A[i]):
        print("present")
    else:
        print("not present")

def binary_iterative(A,x):
    
    x=int(input("enter value to search"))
    n = len(A)
    print(n)
    print(len(A))
    lb=0
    ub=n-1
    while(lb<ub):
        mid=int((lb+ub)/2)
        if(A[mid]==x):
            print("yes")
            return 0
    print("not present")
    return 0
            
def fibonacci_search(A, x):
    n = len(A)
    # Initialize Fibonacci sequence
    a, b = 0, 1
    f = a + b
    offset = -1
    # Find the smallest Fibonacci number greater than or equal to n
    while f < n:
        a, b = b, a + b
        f = a + b
    # Perform Fibonacci search
    while f > 1 and offset + 1 < n:
        i = min(offset + b, n - 1)
        if A[i] < x:
            f = a
            a, b = b, f - a
            offset = i
        elif A[i] > x:
            f = b
            a, b = a - b, f
        else:
            return i
    # Check for the last element
    if a and A[offset + 1] == x:
        return offset + 1
        print("present")
    elif A[offset + 1] == x:
        return offset + 1
        print("present")
    else:
        return -1


def main():
    A=[]
    x=0
    n=len(A)
    accept(A)
    display(A)

    linear_search(A,x)
    sentinal_search(A,x)
    binary_iterative(A,x)
    fibonacci_search(A,x)

main()