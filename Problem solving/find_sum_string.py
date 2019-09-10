# Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we can form a number 'N' using the sum of the given three numbers.
# (allowing repetitions and different arrangements).
# Total number of ways to form 6 is: 8
# 1 + 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 3
# 1 + 1 + 3 + 1
# 1 + 3 + 1 + 1
# 3 + 1 + 1 + 1
# 3 + 3
# 1 + 5
# 5 + 1

a = [1,2,3,5,7]
n=len(a)
num = 20
all_arrangements = []

def find_sum_string(curr_sum, st):
    if curr_sum == num:
        all_arrangements.append(st)
        return

    for i in range(n):
        curr_sum+=a[i]
        if curr_sum > num:
            continue

        st=st+str(a[i])
        find_sum_string(curr_sum, st)
        st=st[:-1]
        curr_sum-=a[i]

find_sum_string(0, '')
for x in all_arrangements:
    print x