# Total number of stairs = n
# Number of steps one can do = a list = x
# # Find:
# 'all ways of stairs-'
# 'Total ways to climb'
# 'Unique steps to climb'

steps = []
unique = []

def unique_steps():
    for st in steps:
        st1 = st.strip('-').split('-')
        st2 = list(set(st.strip('-').split('-')))
        if sorted(st1) == sorted(st2):
            unique.append(st)

def count_stairs(a, curr_sum, sum, st):
    for i in range(len(a)):
        curr_sum = curr_sum + a[i]
        st1=st
        st = st + str(a[i]) + '-'
        if curr_sum == sum:
            print st
            steps.append(st)
            return

        elif curr_sum > sum:
            curr_sum = curr_sum - a[i]
            continue

        # call count again
        count_stairs(a, curr_sum, sum, st)
        curr_sum=curr_sum-a[i]
        st=st1

n=10
x = [1,2,3,5]

print 'all ways of stairs-'
count_stairs(x, 0, n, '-')
print 'Total ways to climb'
print len(steps)
print 'Unique steps to climb'
unique_steps()
print unique
