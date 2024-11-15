# Function to implement binary search

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid                 # Target found, return index
        elif sorted_list[mid] < target:
            left = mid + 1             # Search in the right half
        else:
            right = mid - 1            # Search in the left half

    return -1                          # Target not found

# Example for understanding
numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 5))  # Output: 2
print(binary_search(numbers, 8))  # Output: -1
