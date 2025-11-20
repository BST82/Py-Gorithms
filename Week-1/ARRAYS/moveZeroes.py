# Given an array, move all zeros to the end without changing the order of other elements.
# Input:[0,1,0,3,12]
# Output: [1,3,12,0,0]

arr=list(map(int,input("enter array elements :- ").split(" ")))

class Sol():
    def moveZeros(self,arr):
        j=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr



ans=Sol()
hasAns=ans.moveZeros(arr)
print(hasAns)