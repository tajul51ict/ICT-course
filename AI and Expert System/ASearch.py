import heapq
GOAL = (
(1, 2, 3),
(4, 5, 6),
(7, 8, 0)
)
# Goal position map
goalPos = {}
  def goalMap():
  for i in range(3):
    for j in range(3):
goalPos[GOAL[i][j]] = (i, j)
  def calculateManhattan(board):
  dist = 0
  for i in range(3):
    for j in range(3):
  val = board[i][j]
    if val != 0:
  gx, gy = goalPos[val]
dist += abs(i - gx) + abs(j - gy)
  return dist
def findBlank(board):
  for i in range(3):
    for j in range(3):
  if board[i][j] == 0:
  return i, j
    return -1, -1
def solve8Puzzle(start):
  pq = []
  visited = {}
h = calculateManhattan(start)
  heapq.heappush(pq, (h, 0, start)) # (f, g, board)
  visited[start] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
while pq:
  f, g, currentBoard = heapq.heappop(pq)
  if currentBoard == GOAL:
  print("Goal reached with cost:", g)
return
x, y = findBlank(currentBoard)
  for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]
  if 0 <= nx < 3 and 0 <= ny < 3:
# Convert tuple to list to swap
  board_list = [list(row) for row in currentBoard]
    board_list[x][y], board_list[nx][ny] = board_list[nx][ny], board_list[x][y]
  nextBoard = tuple(tuple(row) for row in board_list)
  newG = g + 1
  if nextBoard not in visited or newG < visited[nextBoard]:
    visited[nextBoard] = newG
  newH = calculateManhattan(nextBoard)
    newF = newG + newH
  heapq.heappush(pq, (newF, newG, nextBoard))
  print("Unsolvable puzzle.")
  if __name__ == "__main__":
start = (
(1, 2, 3),
(4, 0, 6),
(7, 5, 8)
)
goalMap()
print("Starting 8-Puzzle Solver...")
  solve8Puzzle(start)
