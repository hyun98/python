def main():
    row = 2
    col = 3
    mat = [[0]*col for i in range(row)]
    print(mat)
    initlist = [1,9,-12,20,-5,7]
    k=0
    for i in range(row):
        for j in range(col):
            mat[i][j] = initlist[k]
            k+=1
    print(mat)
    m2 = filter_neg(mat)
    print(m2)

def filter_neg(mat):
    row = len(mat)
    col = len(mat[0])
    mat2 = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if mat[i][j] < 0:
                mat2[i][j] = 0
            else:
                mat2[i][j] = mat[i][j]
    return mat2

if __name__ == "__main__":
    main()