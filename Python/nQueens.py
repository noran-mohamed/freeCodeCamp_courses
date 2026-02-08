def dfs_n_queens(n):
    if n < 1:
        return []
    
    #solution[row] = column
    solutions = []
    current = []

    def dfs(row):
        if row == n:
            solutions.append(list(current))
            return
        
        for col in range(n):
            safe = True
            for r in range(row):
                c = current[r]
                if c == col or abs(c-col)==abs(r-row):
                    safe=False
                    break
            
            if safe:
                current.append(col)
                dfs(row+1)
                current.pop()
    dfs(0)
    return solutions

print(dfs_n_queens(5))
