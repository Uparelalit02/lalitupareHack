n=4
arr=[1,6,-2,4]
arr.sort()
diff=0
for i in range(len(arr)-1):
    diff=diff+abs(arr[i+1]-(arr[i]))
print(diff)

    
    