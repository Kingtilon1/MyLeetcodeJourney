# Remove Duplicates

## Problem Statement
Write a function `remove_duplicates()` that takes in a sorted list of integers `nums` as a parameter and removes all duplicates in the list. The function returns the modified list.

## Solution
The solution is implemented in the `remove_duplicates.py` file.

### Usage
```python
from remove_duplicates import remove_duplicates

nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
nums = remove_duplicates(nums)
print(nums)  # Output: [1, 2, 3, 4, 5, 6]
