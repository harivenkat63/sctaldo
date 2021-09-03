arr=list(map(int,input().split()))
sum=int(input())
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j])==sum:
            print(arr[i],arr[j])
else:
    print("No Pairs found")
