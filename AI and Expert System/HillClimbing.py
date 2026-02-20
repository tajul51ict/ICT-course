import copy

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Precompute goal positions for Manhattan distance calculation
goal_pos = {}
for i in range(3):
    for j in range(3):
        goal_pos[GOAL[i][j]] = (i, j)

def calculate_manhattan(board):
    """Calculate Manhattan distance from current board to goal."""
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                goal_i, goal_j = goal_pos[val]
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def find_blank(board):
    """Find the position of the blank tile (0)."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1  # Should never happen

def solve_8puzzle_hill_climbing(start):
    """Solve 8-puzzle using Hill Climbing algorithm."""
    current = copy.deepcopy(start)
    current_h = calculate_manhattan(current)
    
    # Directions: down, up, right, left
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while True:
        # Check if goal is reached
        if current == GOAL:
            print("Goal reached using Hill Climbing.")
            return
        
        x, y = find_blank(current)
        best_neighbor = current
        best_h = current_h
        
        # Explore all possible moves
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Create new board by swapping blank with neighbor
                next_board = copy.deepcopy(current)
                next_board[x][y], next_board[nx][ny] = next_board[nx][ny], next_board[x][y]
                
                h = calculate_manhattan(next_board)
                
                if h < best_h:
                    best_h = h
                    best_neighbor = next_board
        
        # If no better neighbor found, we're stuck
        if best_h >= current_h:
            print("Stopped at local minimum. Goal not reached.")
            return
        
        # Move to the best neighbor
        current = best_neighbor
        current_h = best_h

def main():
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    print("Starting 8-Puzzle Solver using Hill Climbing...")
    solve_8puzzle_hill_climbing(start)

if __name__ == "__main__":
    main()Output
