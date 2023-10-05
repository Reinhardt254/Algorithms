def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Continue searching in the right half
        else:
            right = mid - 1  # Continue searching in the left half

    return -1  # Element not found in the list

# Example usage:
arr = [11, 12, 22, 25, 64]
target = 22
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
