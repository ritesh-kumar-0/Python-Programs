def find_unique(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR each number
    return result


nums = [4, 1, 2, 1, 2]
print("Unique number is:", find_unique(nums))