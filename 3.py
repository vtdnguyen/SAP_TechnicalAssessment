def merge_sorted_arrays_1(arr1, arr2):
    merged, i, j = [], 0, 0

    # Merge the two arrays until one is exhausted
    while i < len(arr1) and j < len(arr2):
        merged.append(arr1[i] if arr1[i] <= arr2[j] else arr2[j])
        # Increment the index of that smaller array element
        i, j = (i + 1, j) if arr1[i] <= arr2[j] else (i, j + 1)
    # Append any remaining elements from arr1 or arr2
    return merged + arr1[i:] + arr2[j:]

def merge_sorted_arrays_2(arr1, arr2):
    #Just sort the concatenated array
    return sorted(arr1 + arr2)

print(merge_sorted_arrays_1([1, 3, 5], [2, 4, 6]))    # [1, 2, 3, 4, 5, 6]
print(merge_sorted_arrays_2([1, 5], [2, 3, 4]))    # [1, 2, 3, 4, 5]