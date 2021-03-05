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

def middle(arr):
    m = len(arr)//2
    if len(arr)%2==0:
        print(arr[m-1])
    else:
        print(arr[m])

def most_freq(arr):
    already_counted = []
    num=[]
    n_c={}
    for i in arr:
        if i in already_counted:
            continue
        else:
            num.append(arr.count(i))
            already_counted.append(i)
    for i in range(len(num)):
        n_c[already_counted[i]] = num[i]
    sorted_num = quickSort(num)
    cnt_num = sorted_num[-1]
    pp=[]
    for i in n_c.keys():
        if n_c.get(i)==cnt_num:
            pp.append(i)
    t = quickSort(pp)
    if len(t)==1:
        print(t[0])
    else:
        print(t[1])

def sansul_mean(arr):
    mean = sum(arr)/n
    print(f"{mean:.0f}")

def rang(arr):
    print(max(arr)-min(arr))

if __name__=="__main__":
    import sys
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append((int(sys.stdin.readline())))
    sansul_mean(arr)
    p = quickSort(arr)
    middle(p)
    most_freq(arr)
    rang(arr)

    