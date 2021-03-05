#병합정렬 : 계속해서 반으로 나눈다(재귀함수를 사용)

def mergeSort(arr):
    #1단계 : 나눈다
    if len(arr)>1:
        # 중간지점 구하기
        mid = len(arr)//2

        # 중간 지점을 기준으로 좌우로 나눔
        left = arr[:mid]
        right = arr[mid:]

        # 나누어진 왼쪽, 오른쪽을 다시 정렬
        left2 = mergeSort(left)
        right2 = mergeSort(right)

        #merge 함수를 불러와서 병합
        return Merge(left2, right2)
    else:
        return arr

# 순서대로 병합하는 함수
def Merge(left, right):
    # 임의의 두 변수를 선언 하는데
    # 아래 두 값이 리스트 내 값을 비교하는 지표가 됨
    i=0
    j=0

    #결과값을 받을 리스트
    merge_arr=[]

    #좌 우를 비교하여 작은 값을 결과리스트에 추가
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            merge_arr.append(left[i])
            i+=1
        else:
            merge_arr.append(right[j])
            j+=1
    
    #나머지 값 들을 결과리스트에 추가
    while i<len(left):
        merge_arr.append(left[i])
        i+=1
    while j<len(right):
        merge_arr.append(right[j])
        j+=1
    
    return merge_arr

if __name__=="__main__":
    import sys
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    
    for i in mergeSort(arr):
        print(i)
    