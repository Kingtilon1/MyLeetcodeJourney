def remove_duplicates(nums):
    index = 0
    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            nums.pop(index)
        else:
            index += 1
    return nums

nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
nums = remove_duplicates(nums)
print(nums)
