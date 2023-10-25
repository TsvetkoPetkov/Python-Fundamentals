words = input().split(" ")
palindrome = input()

palindrome_list = [pal for pal in words if pal == pal[::-1]]

occurrences = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {occurrences} times")
