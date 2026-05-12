def matri(matrix,row,col,n):

        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m - 1

        while row < n and col >= 0:

            if matrix[row][col] == n:
                return (row, col)

            elif matrix[row][col] < n:
                row += 1

            else:
                col -= 1

            return (-1, -1)

def main():
    matrix=[]
    row=int(input("enter the number of rows"))
    col=int(input("enter the number of cols"))
    n=int(input("enter the number to search"))
    for i in range (row):
        r=[]
        for j in range(col):
            val=int(input(""))
            r.append(val)
        matrix.append(r)
    print(matri(matrix,row,col,n))

if __name__=="__main__":
    main()