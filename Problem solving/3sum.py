# Write a function that takes a non-empty array and an integer representing a target sum.
# Testcases
# [1,-1,0] -1
# [3,7,1,2,8,4,5] 10
# [3,7,1,2,8,4,5] 21
# [-1,2,1,-4,5,-3] -8

a=[-1,0,1,2,-1,-4]
a.sort()
t=20

def find_sum_of_two(nums, target, f, l):
    while l > f:
        s = nums[l] + nums[f]
        if s > target:
            l = l - 1
        elif s < target:
            f = f + 1
        else:
            return nums[l], nums[f]

    return False


def find_sum_of_three(nums, target):
    nums.sort()
    f = 0
    l = len(nums) - 1
    while f <= l - 2:
        s1 = find_sum_of_two(nums, target-nums[f], f+1, l)
        if s1:
          s = nums[f]+sum(s1)
          if s < target:
              f = f + 1
          elif s > target:
              l = l - 1
          else:
              return True
        else:
          f = f + 1

    # Replace this placeholder return statement with your code
    return False

print(find_sum_of_three(a, t))
