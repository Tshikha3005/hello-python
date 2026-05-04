import sys

def solve():
    # Reading input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        grid = []
        max_border = 0
        
        # Process Rows
        for i in range(n):
            row_str = input_data[idx]
            grid.append(row_str)
            idx += 1
            
            # Find max consecutive '#' in this row
            row_segments = row_str.split('.')
            for segment in row_segments:
                max_border = max(max_border, len(segment))
        
        # Process Columns
        for j in range(m):
            col_count = 0
            for i in range(n):
                if grid[i][j] == '#':
                    col_count += 1
                    max_border = max(max_border, col_count)
                else:
                    col_count = 0
                    
        print(max_border)

solve()