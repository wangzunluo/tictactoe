def checkHorizontal(board, user, x, y):
  if user == 'X':
    for cell in board[x]:
      if not cell == 'X':
        return False
    return True
  else:
    for cell in board[x]:
      if not cell == 'O':
        return False
    return True
def checkVertical(board, user, x, y):
  if user == 'X':
    for row in board:
      if not row[y] == 'X':
        return False
    return True
  else:
    for row in board:
      if not row[y] == 'O':
        return False
    return True

def checkDiagonal(board, user, x, y):
  if (board[0][0] == user) and (board[1][1] == user) and (board[2][2] == user):
    return True
  if (board[0][2] == user) and (board[1][1] == user) and (board[2][0] == user):
    return True
  return False
def checkFull(board):
  for row in board:
    for cell in row:
      if not cell:
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

def checkStatus(board, user):
  x = [0,1,2]
  y = [0,1,2]
  for i in range(2):
    if checkHorizontal(board, user, x[i], y[i]):
      return True
    elif checkVertical(board, user, x[i], y[i]):
      return True
    elif checkDiagonal(board, user, x[i], y[i]):
      return True
  return False

def fullCheck(board):
  if checkStatus(board,"X"):
    return [True, False, False]
  elif checkStatus(board, "O"):
    return [False, True, False]
  elif checkFull(board):
    return [False, False, True]
  else:
    return [False, False, False]
  # isEdge = checkEdge(board, x, y)
  # result = [False,False,False]
  # if(user == 'X'):
  #   tuser = 0
  # else:
  #   tuser = 1
  # if not isEdge:
  #   if checkDiagonal(board, user, x, y):
  #     result[tuser] = True
  #     return result
  # if checkHorizontal(board, user, x, y):
  #   result[tuser] = True
  #   return result
  # if checkVertical(board, user, x, y):
  #   result[tuser] = True
  #   return result
  # if checkFull(board):
  #   result[2] = True
  #   return result
  # return result