#http://codeforces.com/problemset/problem/144/A
import sys
n = int(raw_input())
nums = map(int, raw_input().split())

def min_max(n, nums):
    mini = sys.maxint
    mini_index = 0
    maxi = -sys.maxint
    maxi_index = 0
    for i in xrange(n):
        if (nums[i] <= mini):
            mini_index = i
            mini = nums[i]
        if (nums[i] >= maxi_index):
            maxi_index = i
            maxi = nums[i]
    return maxi_index, mini_index

mini, maxi = min_max(n, nums)

if (mini < maxi):
    result = (n - mini) + maxi - 1
