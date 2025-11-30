# Longest Substring Without Repeating Characters Problem
# Given a string s = "abcabcbb"
# Find the length of the longest substring without repeating characters.
# A substring must contain unique characters and be continuous.
# In this example, the longest substring is "abc" → length = 3.

str = input("Enter string :- ")

def lengthOfLongestSubstring(str):
    frq={}
    left=0
    max_len=0

    for right in range(len(str)):
        curr=str[right]

        if curr in frq and frq[curr]>=left:
            left=frq[curr]+1
        
        frq[curr]=right
        max_len=max(max_len,right-left+1)

    return max_len

print(lengthOfLongestSubstring(str))

