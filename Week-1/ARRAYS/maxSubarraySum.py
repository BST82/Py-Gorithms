# Problem: Find the maximum sum of any continuous subarray within the array.
# Problem: Find the maximum sum of any continuous subarray within the array.
# Example input: nums = [3, 4, 7, 2, -3, 1, 4, 2]


arr = list(map(int,input("Enter array elements :- ").split(",")))

def maxSubarraySum(arr):
    currSum=arr[0]
    maxSum=arr[0]

    for num in arr[1:]:
        currSum=max(num,currSum+num)
        maxSum=max(maxSum,currSum)

    return maxSum

print(maxSubarraySum(arr))