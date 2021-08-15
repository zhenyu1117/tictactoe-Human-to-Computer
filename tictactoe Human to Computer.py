
 
import pygame
from pygame import *
import random as ra
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
points = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
x = 0
y = 0
flag = 1
lst = []
lst_mine = []
lst_android = []
count = 0
text = pygame.font.SysFont('tic', 50)
Play_score = 0
AI_score = 0
 
 
def draw_restart():
    steps = [(400, 450), (400, 500), (550, 500), (550, 450)]
    pygame.draw.polygon(screen, black, steps, 1)
    text_x = text.render("AGAIN?", 1, black)
    screen.blit(text_x, (410, 460))
 
 
def draw_img(player, x, y):
    if player == 1:
        pygame.draw.circle(screen, black, (x, y), 40, 1)
    # ����
    else:
        pygame.draw.rect(screen, black, ((x - 20, y - 20), (50, 50)), 1)
 
 
def draw_score():
    text_1 = pygame.font.SysFont('����', 30)
    text_player_score = text_1.render('PLAYER ' + str(Play_score), 1, black)
    text_AI_score = text_1.render('AI   ' + str(AI_score), 1, black)
    screen.blit(text_player_score, (410, 10))
    screen.blit(text_AI_score, (410, 40))
 
 
def draw_back():
    screen.fill(white)
    steps = [(100, 100), (100, 400), (400, 400), (400, 100)]
    pygame.draw.polygon(screen, black, steps, 1)
    pygame.draw.lines(screen, black, False, [(100, 200), (400, 200)])
    pygame.draw.lines(screen, black, False, [(100, 300), (400, 300)])
    pygame.draw.lines(screen, black, False, [(200, 100), (200, 400)])
    pygame.draw.lines(screen, black, False, [(300, 100), (300, 400)])
 
 
def check_win(tab):
    return ((points[0][0] == tab and points[0][1] == tab and points[0][2] == tab) or
            (points[1][0] == tab and points[1][1] == tab and points[1][2] == tab) or
            (points[2][0] == tab and points[2][1] == tab and points[2][2] == tab) or
            (points[0][0] == tab and points[1][0] == tab and points[2][0] == tab) or
            (points[0][1] == tab and points[1][1] == tab and points[2][1] == tab) or
            (points[0][2] == tab and points[1][2] == tab and points[2][2] == tab) or
            (points[0][0] == tab and points[1][1] == tab and points[2][2] == tab) or
            (points[0][2] == tab and points[1][1] == tab and points[2][0] == tab)
            )
 
 
def winner():
    # AI
    if check_win(100):
        return 100
    elif check_win(1):
        return -100
 
 
def is_full():
    fl = 0
    for i in range(3):
        for j in range(3):
            if points[i][j] != 0:
                fl += 1
 
    return fl
 
 
def AI_move():

    for i in range(3):
        for j in range(3):
            if points[i][j] == 0:
                points[i][j] = 100
                if check_win(100):
                    return (i, j)
                else:
                    points[i][j] = 0

    for i in range(3):
        for j in range(3):
            if points[i][j] == 0:
                points[i][j] = 1
                if check_win(1):
                    return (i, j)
                else:
                    points[i][j] = 0
 

    if points[1][1] == 0:
        return (1, 1)
 

    temp = []
    for i in (0, 2):
        for j in (0, 2):
            if points[i][j] == 0:
                temp.append((i, j))
    if len(temp) != 0:
        return ra.choice(temp)
 
    # ռ�ı�
    for i in ((0, 1), (1, 0), (1, 2), (2, 1)):
        if points[i[0]][i[1]] == 0:
            temp.append((i[0], i[1]))
    if len(temp) != 0:
        return ra.choice(temp)
 
 
def draw_all():
    draw_back()
    draw_score()
    for i in lst:
        draw_img(i[0], i[1], i[2])
    if flag == 100:
        text_conent = text.render("AI win", 1, black)
        screen.blit(text_conent, (220, 50))
    elif flag == -100:
        text_conent = text.render("You win", 1, black)
        screen.blit(text_conent, (220, 50))
    elif flag == 123:
        text_conent = text.render("TIE", 1, black)
        screen.blit(text_conent, (220, 50))
    if flag == 123 or flag == 100 or flag == -100:
        draw_restart()
 
 
def play():
    global flag, AI_score, Play_score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 400 < x < 550 and 450 < y < 500:
                    lst.clear()
                    for i in range(3):
                        for j in range(3):
                            points[i][j] = 0
                    flag = 1
                if 100 <= x <= 400 and 100 <= y <= 400:
                    x = (x - 100) // 100
                    y = (y - 100) // 100
                    l_x = x * 100 + 150
                    l_y = y * 100 + 150
                    # player
                    if flag == 1:
                        if is_full() != 9:
                            if points[x][y] == 0:
                                points[x][y] = 1
                                lst.append((1, l_x, l_y))
                                if winner() == -100:
                                    flag = -100
                                    Play_score += 1
                                    print('player win')
                                else:
                                    flag = -1
                        else:
                            flag = 123
 
            if flag == -1:
                if is_full() != 9:
                    # �˻���
                    xx, yy = AI_move()
                    l_x = xx * 100 + 150
                    l_y = yy * 100 + 150
                    points[xx][yy] = 100
                    lst.append((2, l_x, l_y))
                    if winner() == 100:
                        flag = 100
                        AI_score += 1
                        print('AI win')
                    else:
                        flag = 1
                else:
                    flag = 123
 
        draw_all()
        pygame.display.flip()
 
 
if __name__ == '__main__':
    play()