def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        right=[]
        left=[]
        merged_arr=[]
        for i in range(1,len(arr)):
            if arr[i]>pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        a = quickSort(left)
        b = quickSort(right)

        merged_arr.extend(a)
        merged_arr.append(pivot)
        merged_arr.extend(b)
        return merged_arr
    
if __name__=="__main__":
    import sys
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    for i in quickSort(arr):
        print(i)