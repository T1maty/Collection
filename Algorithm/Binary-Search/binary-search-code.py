def binary_search(arr, target):
    left,right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle -1
    return -1 #Goals not having
 

 #example of usage

sorted_array = [1,2,5,6,7,9,21,345]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"{target_value} found in index {result}")
else:
    print(f"{target_value} not found in array")

#This code efficiently finds the target value in a sorted array in logarithmic time,  O(log n).






