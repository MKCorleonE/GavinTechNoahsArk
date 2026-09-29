"""
You are given an array A of N positive integers.

Consider the following operation: remove one element from A and compute the product of all the remaining array elements. If there is only one element remaining in the array, the product is equal to that element.

For example, if A = [9, 16, 4], we can:
- remove 9 and get a product equal to (16 x 4) = 64;
- remove 16 and get a product of 36;
- remove 4 and get a product of 144.

As seen in the example above, the product might change depending on which element we remove.

Write a function:
def solution(A)

that, given an array A of N integers, returns the number of different products that can be obtained by removing exactly one element from A.

Examples:
1. Given A = [9, 16, 4], the function should return 3. As explained above, the achievable products are 64, 36 and 144.
2. Given A = [3, 4, 2, 3, 1], the function should return 4.
3. Given A = [1000000000, 1000000000], the function should return 1.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [2..100,000];
- each element of array A is an integer within the range [1..1,000,000,000].
"""

# 最佳答案
def solution(A):
    return len(set(A))

# 复杂度分析：
# 时间复杂度：O(N)，其中 N 是数组 A 的长度。我们需要遍历数组 A 一次，将每个元素添加到集合中。集合的插入操作平均时间复杂度为 O(1)，
# 因此总的时间复杂度为 O(N)。
# 空间复杂度：O(N)，在最坏情况下，数组 A 中的所有元素都是不同的，我们需要存储所有这些不同的元素在集合中。因此，空间复杂度为 O(N)。

# 如果包含0的情况，代码可以修改如下：
def solution(A):
    zero_count = A.count(0)

    if zero_count == 0:
        return len(set(A))
    elif zero_count == 1:
        return 2
    else:
        return 1