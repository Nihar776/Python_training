def spiralMatrix(l:list,i:int,j:int,m:int,n:int,visited):
    if i==m or j==n or i<0 or j<0 or (i,j) in visited :
        return
    # Print element
    print(l[i][j])
    #Append index of element 
    visited.append((i,j))
    # Move Right
    spiralMatrix(l,i,j+1,m,n,visited)
    # Move Down
    spiralMatrix(l,i+1,j,m,n,visited)
    # Move Left
    spiralMatrix(l,i,j-1,m,n,visited)
    # Move Up
    spiralMatrix(l,i-1,j,m,n,visited)

arr = [
    [1, 2, 3, 4],
    [12,13,14,5],
    [11,16,15,6],
    [10, 9, 8,7]
]
spiralMatrix(arr,0,0,4,4,[])
