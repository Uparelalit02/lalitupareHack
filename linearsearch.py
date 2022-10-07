def search(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
    return -1
arr=[1,2,3,4,5]
ele=5
print(search(arr, ele))
