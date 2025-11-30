# Majority Element Problem
# Given an array nums = [2, 2, 1, 1, 1, 2, 2]
# The majority element is the element that appears more than n/2 times.
# In this example, 2 appears 4 times out of 7 → which is more than 7/2.
# Therefore, the majority element is 2.

arr = list(map(int,input("enter array elements :- ").split(",")))

class Sol():

    def majorityElementByBoyerMoore(self,arr):
        count=0
        candidate=None

        for num in arr:
            if count==0:
                candidate=num

            count+=(1 if candidate==num else -1)
        
        return candidate


    def majorityByHashmap(self,arr):
        seen={}

        for i in range(len(arr)):
            seen[arr[i]]=seen.get(arr[i],0)+1
            if seen[arr[i]]>len(arr)//2:
                return arr[i]



ans = Sol()
ansByMoore=ans.majorityElementByBoyerMoore(arr.copy())
ansByHashmap=ans.majorityByHashmap(arr.copy())
print(ansByMoore)
print(ansByHashmap)