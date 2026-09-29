"""
Write an algorithm to find the number of occurrences of needle in a given positive number haystack.

Input
The first line of the input consists of an integer needle, representing a digit.
The second line consists of an integer haystack, representing the positive number.

Output
Print an integer representing the number of occurrences of needle in haystack.

Constraints
0 ≤ needle ≤ 9
0 ≤ haystack ≤ 99999999

Example
Input:
2
123228

Output:
3
"""

# 最佳答案
needle = input()
haystack = input()

result = 0

for digit in haystack:
    if digit == needle:
        result += 1

print(result)