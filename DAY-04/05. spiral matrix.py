def spiralMatrix(l:list,i:int,j:int,m:int,n:int,visited):
    if i==m or j==n or i<0 or j<0 or (i,j) in visited :
        return
    print(l[i][j])
    visited.append((i,j))
    spiralMatrix(l,i,j+1,m,n,visited)
    spiralMatrix(l,i+1,j,m,n,visited)
    spiralMatrix(l,i,j-1,m,n,visited)
    spiralMatrix(l,i-1,j,m,n,visited)

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
spiralMatrix(arr,0,0,3,3,[])
