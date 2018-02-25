def checkHorizontal(board, user, x, y):
  if user == 'X':
    for cell in board[x]:
      if not board[x][cell] == 'X':
        return False
    return True
  else:
    for cell in board[x]:
      if not board[x][cell] == 'Y':
        return False
    return True
def checkVertical(board, user, x, y):
  if user == 'X':
    for row in board:
      if not board[row][y] == 'X':
        return False
    return True
  else:
    for row in board:
      if not board[row][y] == 'Y':
        return False
    return True
def checkDiagonal(board, user, x, y):
  if x == 0:
    if y == 0:
      for i in range(1):
        if not board[i][i] == board[i+1][i+1]:
          return False
      return True
    else:
      if not board[0][2] == board[1][1]:
        return False
      elif not board[2][0] == board[1][1]:
        return False
      return True
  elif x == 2:
    if y == 0:
      if not board[0][2] == board[1][1]:
        return False
      elif not board[2][0] == board[1][1]:
        return False
      return True
    else:
      for i in range(1):
        if not board[i][i] == board[i+1][i+1]:
          return False
      return True
  else:
    for i in range(1):
      if not board[i][i] == board[i+1][i+1]:
        return False
    return True

def checkFull(board):
  for row in board:
    for cell in row:
      if not board[row][cell]:
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
  isEdge = checkEdge(board, x, y)
  result = [False,False,False]
  if(user == 'X'):
    user = 0
  else:
    user = 1
  
  if not isEdge:
    if checkDiagonal(board, user, x, y):
      result[user] = True
      return result
  if checkHorizontal(board, user, x, y):
    result[user] = True
    return result
  if checkVertical(board, user, x, y):
    result[user] = True
    return result
  if checkFull(board):
    result[2] = True
    return result
  return result