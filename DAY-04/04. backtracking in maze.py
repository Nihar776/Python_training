m=n=3
def backtrack(i:int,j:int):
    # Dead End
    if i==m or j==n:
        return 0
    # Destination Reached
    if i==m-1 and j==n-1:
        return 1
    # Move to Right
    right=backtrack(i,j+1)
    # Move Down
    down=backtrack(i+1,j)
    return right+down

print(backtrack(0,0))