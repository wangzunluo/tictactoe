def checkHorizontal(board, user, x, y):

def checkVertical(board, user, x, y):

def checkDiagonal(board, user, x, y):

def checkFull(board):
  for row in board:
    for cell in row:
      if not board[row][cell]
        return False
  return True

def checkEdge(board, x, y):
  if x == 0:
    if y == 1:
      return True
    else:
      return False
  elif x == 1:
    if y == 0 or y == 2:
      return True
    else:
      return False
  else:
    if y == 1:
      return True
    else:
      return False

def checkStatus(board, user, x, y):
  isEdge = checkEdge(board, x, y):
  if not isEdge:
    if checkDiagonal(board, user, x, y):
      return "game was won"
  if checkHorizontal(board, user, x, y):
    return "game was won"
  if checkVertical(board, user, x, y):
    return "game was won"
  full = checkFull(board)
    return "cat game"