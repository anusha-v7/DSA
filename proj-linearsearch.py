def find_student(marks, target):
    for i in range(len(marks)):
        if marks[i] == target:
            return i
    return -1


def count_occurrences(marks, target):
    count = 0
    for m in marks:
        if m == target:
            count += 1
    return count


def find_max(marks):
    max_val = marks[0]   #this assumes that index value is greter first and then it compares 
    for m in marks:
        if m > max_val:
            max_val = m
    return max_val


def find_min(marks):
    min_val = marks[0]
    for m in marks:
        if m < min_val:
            min_val = m
    return min_val


def first_occurrence(marks, target):
    for i in range(len(marks)):
        if marks[i] == target:
            return i
    return -1


def last_occurrence(marks, target):
    for i in range(len(marks)-1, -1, -1): # start from last index move backword and stop at index 0
        if marks[i] == target:
            return i
    return -1


def count_greater(marks, x):
    count = 0
    for m in marks:
        if m > x:
            count += 1
    return count


def sum_marks(marks):
    total = 0
    for m in marks:
        total += m
    return total


def even_odd_count(marks):
    even = odd = 0
    for m in marks:
        if m % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def reverse_marks(marks):
    rev = []
    for i in range(len(marks)-1, -1, -1):
        rev.append(marks[i])
    return rev


def second_largest(marks):
    first = second = float('-inf')  # -ve infinite value  1st 2nd smallest possible value 
    for m in marks:
        if m > first:  #the value m is holding it beccomes old and stores in 2nd , and the new comapre big value become first  
            second = first
            first = m
        elif m > second and m != first:
            second = m
    return second


# ---------------- MAIN PROGRAM ----------------

marks = list(map(int, input("Enter student marks (space separated): ").split()))

while True:
    print("\n--- Student Data Analyzer ---")
    print("1. Search mark")
    print("2. Count occurrences")
    print("3. Find maximum mark")
    print("4. Find minimum mark")
    print("5. First occurrence")
    print("6. Last occurrence")
    print("7. Count marks greater than X")
    print("8. Sum and Average")
    print("9. Even and Odd count")
    print("10. Reverse marks")
    print("11. Second largest mark")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter mark to search: "))
        result = find_student(marks, x)
        if result == -1:
            print("Mark not found")
        else:
            print("Mark found at index:", result)

    elif choice == 2:
        x = int(input("Enter mark: "))
        print("Count:", count_occurrences(marks, x))

    elif choice == 3:
        print("Maximum mark:", find_max(marks))

    elif choice == 4:
        print("Minimum mark:", find_min(marks))

    elif choice == 5:
        x = int(input("Enter mark: "))
        print("First occurrence index:", first_occurrence(marks, x))

    elif choice == 6:
        x = int(input("Enter mark: "))
        print("Last occurrence index:", last_occurrence(marks, x))

    elif choice == 7:
        x = int(input("Enter value: "))
        print("Count greater than", x, ":", count_greater(marks, x))

    elif choice == 8:
        total = sum_marks(marks)
        avg = total / len(marks)
        print("Sum:", total)
        print("Average:", avg)

    elif choice == 9:
        even, odd = even_odd_count(marks)
        print("Even count:", even)
        print("Odd count:", odd)

    elif choice == 10:
        print("Reversed marks:", reverse_marks(marks))

    elif choice == 11:
        print("Second largest mark:", second_largest(marks))

    elif choice == 12:
        print("Exiting...")
        break

    else:
        print("Invalid choice")