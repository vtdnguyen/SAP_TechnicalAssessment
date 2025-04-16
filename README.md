# 1st Problem:

## Approaches:
 - Initialize an **unordered map** (string_count) to store character counts.
 - Iterate through the string to update character counts in the map.
 - Iterate through the map , return the first character with a count of 1 (because map will have the order of character in string)

    ## OR:

 - The **Counter** class is used to count the frequency of each character in the string s
 - The next() function retrieves the first character from the generator that satisfies the condition (string_count[n] == 1).

# 3rd Problem:

## Approaches:
 - Uses two pointers (i and j) to track positions in arr1 and arr2.
 - Compares elements at the pointers, appending the smaller one to merged. After one array is exhausted, appends any remaining elements from the other array.

   ## OR:

 - Just sort the concatenated array (longer to run but shorter)