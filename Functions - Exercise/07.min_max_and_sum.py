def min_number(numbers):
    return min(numbers)

def max_number(numbers):
    return max(numbers)

def sum_numbers(numbers):
    return sum(numbers)

nums = [int(x) for x in input().split(" ")]

print(f"The minimum number is {min_number(nums)}")
print(f"The maximum number is {max_number(nums)}")
print(f"The sum number is: {sum_numbers(nums)}")
