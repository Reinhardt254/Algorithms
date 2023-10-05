def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves.
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements in the left and right subarrays and merge them into result.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from both subarrays.
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
