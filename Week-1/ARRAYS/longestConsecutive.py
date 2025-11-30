# Longest Consecutive Sequence Problem
# Given an unsorted array nums = [100, 4, 200, 1, 3, 2]
# Find the length of the longest consecutive elements sequence.
# For this example, the longest sequence is [1, 2, 3, 4] → length = 4

arr = list(map(int,input("enter array elements :- ").split(",")))

def longestConsecutive(arr):
    num_set=set(arr)
    longest=0

    for num in arr:
        curr=num
        streak=1

        if num-1 not in num_set:
            curr=num
            streak=1

            while curr+1 in num_set:
                curr+=1;
                streak+=1
            
            longest=max(longest,streak)

    return longest

print(longestConsecutive(arr))