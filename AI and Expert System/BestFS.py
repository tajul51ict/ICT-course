import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]


def manhattan_distance(current, goal):
    pos = {}

    for i in range(3):
        for j in range(3):
            pos[goal[i][j]] = (i, j)

    dist = 0
    for i in range(3):
        for j in range(3):
            val = current[i][j]
            if val != 0:
                x, y = pos[val]
                dist += abs(i - x) + abs(j - y)

    return dist


def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j


def board_to_tuple(board):
    return tuple(tuple(r) for r in board)


def best_first_search(start):
    pq = []
    visited = set()

    h = manhattan_distance(start, goal_state)
    heapq.heappush(pq, (h, start))

    while pq:
        h, current = heapq.heappop(pq)

        print("Heuristic =", h)
        for r in current:
            print(r)
        print()

        if current == goal_state:
            print("Goal Reached!")
            return

        visited.add(board_to_tuple(current))

        x, y = find_blank(current)

        for k in range(4):
            nx = x + row[k]
            ny = y + col[k]

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [r[:] for r in current]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                if board_to_tuple(new_board) not in visited:
                    h_new = manhattan_distance(new_board, goal_state)
                    heapq.heappush(pq, (h_new, new_board))


start_state = [
    [1, 2, 0],
    [4, 6, 3],
    [7, 5, 8]
]

best_first_search(start_state)
