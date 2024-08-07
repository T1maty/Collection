Binary Search
Binary search is an algorithm used to find the position of a target value within a sorted array. It works on the principle of divide and conquer.

Key Steps of Binary Search:
Initialization:

Set the initial values for the left (start) and right (end) boundaries of the array.
Search Loop:

Calculate the middle index between the left and right boundaries.
If the value at the middle index is equal to the target value, return the index.
If the target value is less than the value at the middle index, narrow the search to the left half of the array (update the right boundary).
If the target value is greater than the value at the middle index, narrow the search to the right half of the array (update the left boundary).
Completion:

If the boundaries converge and the target value has not been found, return an indicator that the value is not present in the array (e.g., -1).
