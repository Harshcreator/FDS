def binary_search_rec(phonebook, name, low, high):
    if(low<=high):
        mid = (low + high)//2
        if(phonebook[mid][0] == name):
            return mid
        elif(phonebook[mid][0] < name):
            return binary_search_rec(phonebook, name, mid + 1, high)
        else:
            return binary_search_rec(phonebook, name, low, mid - 1)
    else:
        return -1
    
def binary_search_itr(phonebook, name):
    low, high = 0, len(phonebook)-1
    
    while(low<=high):
        mid = (low + high)//2
        if(phonebook[mid][0] == name):
            return mid
        elif(phonebook[mid][0] < name):
            low = mid + 1
        else:
            high = mid - 1
    return -1

def fibonacci_search(phonebook, name):
    fib_m_minus_2, fib_m_minus_1 = 0, 1
    fib = fib_m_minus_2 + fib_m_minus_1

    n = len(phonebook)

    while fib < n:
        fib_m_minus_2, fib_m_minus_1 = fib_m_minus_1, fib
        fib = fib_m_minus_2 + fib_m_minus_1

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if phonebook[i][0] < name:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif phonebook[i][0] > name:
            fib = fib_m_minus_2
            fib_m_minus_1 -= fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and phonebook[offset + 1][0] == name:
        return offset + 1

    return -1
   
def insert(phonebook, name, number):
    index = binary_search_itr(phonebook, name)
    if index == -1:
        phonebook.append((name, number))
        phonebook.sort()
        
def display(phonebook):
    for name, number in phonebook:
        print(name, "\t: ", number)
    
phonebook = [("Alice", "123-456-7890"), ("Bob", "987-654-3210"), ("Charlie", "555-123-4567")]
phonebook.sort()  # Initial sorting
insert(phonebook, "David", "111-222-3333")
insert(phonebook, "Charlie", "555-999-8888")  # Existing entry, won't be added

print("Phonebook after insertion:")
display(phonebook)

# Searching
search_name = "Bob"
index_rec = binary_search_rec(phonebook, search_name, 0, len(phonebook) - 1)
index_itr = binary_search_itr(phonebook, search_name)
index_fib = fibonacci_search(phonebook, search_name)

print("Search result for ",search_name)
if index_rec != -1:
    print(f"\nFound at index {index_rec} (Recursive)")
else:
    print("Not found (Recursive)")

if index_itr != -1:
    print(f"\nFound at index {index_itr} (Non-Recursive)")
else:
    print("Not found (Non-Recursive)")
    
if index_fib != -1:
    print(f"\nFound at index {index_fib}")
else:
    print("Not found")