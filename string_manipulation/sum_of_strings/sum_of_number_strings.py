def sum_of_number_strings(nums):
    total = 0
    for i in nums:
        i = int(i)
        total += i
    return total

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
