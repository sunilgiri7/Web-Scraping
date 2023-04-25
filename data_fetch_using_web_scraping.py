def next_move(human, bot, board):
    # Check if current cell is dirty
    if board[human][bot] == 'd':
        print('CLEAN')
        return
    
    # Find closest dirty cell using Manhattan distance 
    min_dist = float('inf')
    min_cell = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dist = abs(i - human) + abs(j - bot)
                if dist<min_dist:
                    min_dist = dist
                    min_cell = (i, j)

    # Move to the closest dirty cell
    if human - min_cell[0] < 0:
        next_move = 'DOWN'
    elif human - min_cell[0] > 0:
        next_move = 'UP'
    elif bot - min_cell[1] < 0:
        next_move = 'RIGHT'
    elif bot - min_cell[1] > 0:
        next_move = 'LEFT'
    print(next_move)
    return None

if __name__=='__main__':
    human, bot = [int(i) for i in input().strip().split()]
    board = []
    for i in range(5):
        board.append(input().strip())
    next_move(human, bot, board)

# if __name__=='__main__':
#     human = [int(i) for i in input().strip().split()]
#     bot = int(input())  
#     board = [[j for j in input().strip()]for i in range(5)]
#     next_move(human[0], bot[0], board)