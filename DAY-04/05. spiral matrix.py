def spiralMatrix(mat:list,top:int,bottom:int,left:int,right:int):
    if top>bottom or left>right:
        return
    # From Left Move Right →
    for i in range(left,right+1):
        LR=mat[top][i]
        print(mat[top][i])
    # From Top Move down ↓
    for i in range(top+1,bottom+1):
        TB=mat[i][right]
        print(mat[i][right])
    # From Right Move Left ←
    for i in range(right-1,left-1,-1):
        RL=mat[bottom][i]
        print(mat[bottom][i])
    # From Bottom Move Up ↑
    for i in range(bottom-1,top,-1):
        BT=mat[i][left]
        print(mat[i][left])
    spiralMatrix(mat,top+1,bottom-1,left+1,right-1)



arr = [
    [1 ,2 ,3 ,4 ,5],
    [16,17,18,19,6],
    [15,24,25,20,7],
    [14,23,22,21,8],
    [13,12,11,10,9]
    
]
# arr = [
#     [1, 2, 3, 4],
#     [12,13,14,5],
#     [11,16,15,6],
#     [10, 9, 8,7]
# ]
spiralMatrix(arr,0,len(arr)-1,0,len(arr[0])-1)
