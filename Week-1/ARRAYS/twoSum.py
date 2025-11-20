
# two sum 
# An array arr = [2, 7, 11, 15]
# A target sum target = 9
# 👉 Output: [0, 1] because 2 + 7 = 9

arr=list(map(int,input("enter array elements :- ").split(" ")))
target=int(input("enter target :- "))

class Sol():
    def checkShort(self,arr,target):
        if arr==sorted(arr) :
           return "Two pointer answer", self.twoSumTwoPointer(arr, target)
        else :
           return "Hashmap answer", self.twoSumUsignHashmap( arr, target)
        
    
    def twoSumUsignHashmap(self,arr,tar):
        seen={}
        for i in range(len(arr)):
            curr=target-arr[i]
            if curr in seen:
                return [seen[curr],i]
            seen[arr[i]]=i
        return []
        
    def twoSumTwoPointer(self, arr, target):
       left =0
       right = len(arr) - 1
       
       while left < right:
           ans = arr[left] + arr[right]
           if ans == target:
              return [left, right]
           elif ans > target:
              right -= 1
           else:
               left+=1
              
            
       return []



ans=Sol()
hasAns=ans.checkShort(arr,target)
print(hasAns)
# print(target)