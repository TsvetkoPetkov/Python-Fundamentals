def polindrome(nums):
    for i in nums:
        if i == i[::-1]:
            print("True")
        else:
            print("False")

numbers = [x for x in input().split(", ")]
polindrome(numbers)
