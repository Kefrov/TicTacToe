import pygame
import sys

pygame.init()

pygame.display.set_icon(pygame.image.load('icon.png'))
screen = pygame.display.set_mode((500, 500))

result_font = pygame.font.Font('font.ttf', 84)
restart_font = pygame.font.Font('font.ttf', 26)
init_grid = [['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
             ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']]
init_turn = 'x'
init_score = {'x' : 0, 'o' : 0}
init_marks = []


def update(grid, x, y, score, turn, marks):
    grid[y][x] = turn

    counter = 0
    for i in range(10):
        if grid[y][i][0] == turn and 'horizontal' not in grid[y][i]:
            counter += 1
            if counter == 5:
                marks.append((i, y, i - 4, y))
                for j in range(5):
                    grid[y][i - j] = (turn, 'horizontal')
                score[turn] += 1
                screen = pygame.display.set_caption(f"TicTacToe (X : {score['x']} || O : {score['o']})")
        else:
            counter = 0

    counter = 0
    for i in range(10):
        if grid[i][x][0] == turn and 'vertical' not in grid[i][x]:
            counter += 1
            if counter == 5:
                marks.append((x, i, x, i - 4))
                for j in range(5):
                    grid[i - j][x] = (turn, 'vertical')
                score[turn] += 1
                pygame.display.set_caption(f"TicTacToe (X : {score['x']} || O : {score['o']})")
        else:
            counter = 0

    diagonal_bounds = {'diag_up' : [], 'diag_down' : []}
    x1, y1 = x, y
    x2, y2 = x, y
    while x1 > 0 and y1 > 0:
        x1 -= 1
        y1 -= 1
    while x2 < 9 and y2 < 9:
        x2 += 1
        y2 += 1
    diagonal_bounds['diag_down'] = [x1, y1, x2, y2]
    x1, y1 = x, y
    x2, y2 = x, y
    while x1 > 0 and y1 < 9:
        x1 -= 1
        y1 += 1
    while x2 < 9 and y2 > 0:
        x2 += 1
        y2 -= 1
    diagonal_bounds['diag_up'] = [x1, y1, x2, y2]

    counter = 0
    x1, y1, x2, y2 = diagonal_bounds['diag_down']
    while (x1, y1) != (x2 + 1, y2 + 1):
        if grid[y1][x1][0] == turn and 'diag_down' not in grid[y1][x1]:
            counter += 1
            if counter == 5:
                marks.append((x1, y1, x1 - 4, y1 - 4))
                for j in range(0, 5):
                    grid[y1 - j][x1 - j] = (turn, 'diag_down')
                score[turn] += 1
                screen = pygame.display.set_caption(f"TicTacToe (X : {score['x']} || O : {score['o']})")
        else:
            counter = 0
        x1 += 1
        y1 += 1
    x1, y1, x2, y2 = diagonal_bounds['diag_up']
    counter = 0
    while (x1, y1) != (x2 + 1, y2 - 1):
        if grid[y1][x1][0] == turn and 'diag_up' not in grid[y1][x1]:
            counter += 1
            if counter == 5:
                marks.append((x1, y1, x1 - 4, y1 + 4))
                for j in range(0, 5):
                    grid[y1 + j][x1 - j] = (turn, 'diag_up')
                score[turn] += 1
                screen = pygame.display.set_caption(f"TicTacToe (X : {score['x']} || O : {score['o']})")
        else:
            counter = 0
        x1 += 1
        y1 -= 1

    return 'x' if turn == 'o' else 'o'


def create_grid():
    position = 50
    for i in range(9):
        pygame.draw.line(screen, color=(0, 0, 0), start_pos=(5, position), end_pos=(495, position), width=2)
        pygame.draw.line(screen, color=(0, 0, 0), start_pos=(position, 5), end_pos=(position, 495), width=2)
        position += 50


def fill_grid(grid, turn, marks):
    for i in range(10):
        for j in range(10):
            if grid[i][j][0] == 'o':
                pygame.draw.circle(screen, (220, 0, 0), (j * 50 + 26, i * 50 + 26), 16, 4)
            if grid[i][j][0] == 'x':
                pygame.draw.line(screen, color=(0, 220, 0), start_pos=(j * 50 + 12, i * 50 + 12), end_pos=((j + 1) * 50 - 12, (i + 1) * 50 - 12), width=6)
                pygame.draw.line(screen, color=(0, 220, 0), start_pos=(j * 50 + 12, (i + 1) * 50 - 12), end_pos=((j + 1) * 50 - 12, i * 50 + 12), width=6)
    for mark in marks:
        color = (0, 255, 0) if grid[mark[1]][mark[0]][0] == 'x' else (255, 0, 0)
        pygame.draw.line(screen, color=color, start_pos=(mark[0] * 50 + 25, mark[1] * 50 + 25), end_pos=(mark[2] * 50 + 25, mark[3] * 50 + 25), width=3)


def end_screen(result):
    result_text = result_font.render(result, 1, (0, 0, 0))
    result_text_rect = result_text.get_rect(center=(250, 125))
    restart_text = restart_font.render('press Space to restart', 1, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=(250, 375))
    screen.blit(result_text, result_text_rect)
    screen.blit(restart_text, restart_text_rect)


def game(turn, score, grid, marks):
    pygame.display.set_caption('TicTacToe (X : 0 || O : 0)')
    while True:
        screen.fill((255, 255, 255))
        create_grid()
        fill_grid(grid, turn, marks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()
                x = mouse_xy[0] // 50
                y = mouse_xy[1] // 50
                if grid[y][x][0] == 'e':
                    turn = update(grid, x, y, score, turn, marks)
        
        for row in grid:
            grid_full = True
            if 'e' in row:
                grid_full = False
                break
        if grid_full:
            game_over(score)

        pygame.display.update()
        pygame.time.Clock().tick(60)


def game_over(score):
    if score['x'] == score['o']:
        result = 'Draw.'
    elif score['x'] > score['o']:
        result = 'X wins!'
    else:
        result = 'O wins!'
    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game(init_turn, init_score.copy(), [row[:] for row in init_grid], init_marks.copy())

        end_screen(result)

        pygame.display.update()
        pygame.time.Clock().tick(60)


game(init_turn, init_score.copy(), [row[:] for row in init_grid], init_marks.copy())
