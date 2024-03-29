# subset_sum
# a = [3, 1, 4, 12, 5, 2, 7]
# sum=9

import copy

def check_unique(st):
    st2 = list(set(st))
    if st == st2:
        return True
    return False

import pdb
def find_sum_all_sub_set(a, sum, curr_sum, st):
    for i in range(len(a)):
        curr_sum = curr_sum+a[i]
        st1 = copy.deepcopy(st)
        st.append(a[i])
        if curr_sum > sum:
            curr_sum = curr_sum - a[i]
            st = copy.deepcopy(st1)
            continue

        elif curr_sum == sum:
            if check_unique(st) and len(st) == 3:
                print st
                return

        find_sum_all_sub_set(a, sum, curr_sum, st)
        curr_sum = curr_sum-a[i]
        st = copy.deepcopy(st1)

def find_sum_all_sub_set2(a, s):
    # This is much faster solution than earlier solution.
    def util(cur, pos, target):
        if target == 0:
            arr.append(cur[:])
            return

        for i in range(pos, l):
            if a[i] > target:
                break
            cur.append(a[i])
            util(cur, i, target-a[i])
            cur.pop()

    l = len(a)
    a.sort()
    arr=[]
    util([], 0, s)
    return arr

a = [3, 1, 4, 12, 5, 2, 7, 6, 8]
sum = 9
find_sum_all_sub_set(a, sum, 0, [])
