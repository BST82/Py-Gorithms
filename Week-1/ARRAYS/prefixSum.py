# nums = [3, 4, 7, 2, -3, 1, 4, 2]
# k = 7

# find the count of subarrays those sum is equal to 7

arr = list(map(int,input("Enter array elements :- ").split(",")))
k= int(input("Enter sum :- "))

def countOfSubArraySum(arr,k):
    prefix=0
    count=0
    fre={0:1}

    for i in range(len(arr)):
        prefix+=arr[i]
        if prefix-k in fre:
            count+=fre[prefix-k]
        
        fre[prefix]=fre.get(prefix,0)+1

    return count

print(countOfSubArraySum(arr,k))