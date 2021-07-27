import pygame
import time
WIN_WIDTH =800;WIN_HEIGHT =600   #視窗大小
ENEMY_WIDTH=100;ENEMY_HEIGHT=100 #Enemy大小
BTN_WIDTH = 50;BTN_HEIGHT = 50   #按鈕大小
HP_WIDTH = 40;HP_HEIGHT = 40     #HP icon大小
FPS=30
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
'''主視窗大小設定'''
pygame.display.set_caption("My First Game")
background=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/Map.png')
background=pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
'''導入Background圖片，並調整大小'''
enemy=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/enemy.png')
enemy=pygame.transform.scale(enemy,(ENEMY_WIDTH,ENEMY_HEIGHT))
'''導入Enemy圖片，並調整大小'''
hp=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/hp.png')
hp=pygame.transform.scale(hp,(HP_WIDTH,HP_HEIGHT))
'''導入hp圖片，並調整大小'''
hp_gray=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/hp_gray.png')
hp_gray=pygame.transform.scale(hp_gray,(HP_WIDTH,HP_HEIGHT))
'''導入hp_gray圖片，並調整大小'''
muse=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/muse.png')
muse=pygame.transform.scale(muse,(BTN_WIDTH,BTN_HEIGHT))
'''導入muse圖片，並調整大小'''
sound=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/sound.png')
sound=pygame.transform.scale(sound,(BTN_WIDTH,BTN_HEIGHT))
'''導入sound圖片，並調整大小'''
go=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/continue.png')
go=pygame.transform.scale(go,(BTN_WIDTH,BTN_HEIGHT))
'''導入run圖片，並調整大小'''
pause=pygame.image.load('/Users/antony/Desktop/NCKU/lab02/images/pause.png')
pause=pygame.transform.scale(pause,(BTN_WIDTH,BTN_HEIGHT))
'''導入pause圖片，並調整大小'''
clock = pygame.time.Clock()
run = True
while run:
    window.fill((0,0,0))    #底色
    window.blit(background,(0,0))
    window.blit(enemy,(8,235))
    pygame.draw.rect(window, (150, 23, 100), [0, 0, 800, 100])  #粉紫色工具列
    pygame.draw.rect(window,(255,0,0),[19,240,70,5])
    window.blit(hp_gray,(400,50));window.blit(hp_gray,(450,50));window.blit(hp_gray,(500,50))
    window.blit(hp,(350,50));window.blit(hp,(300,50))
    window.blit(hp, (300,20));window.blit(hp, (350,20));window.blit(hp,(400,20))
    window.blit(hp,(450,20));window.blit(hp,(500,20))
    window.blit(muse,(550,30));window.blit(sound,(600,30))
    window.blit(go,(650,30));window.blit(pause,(700,30))
    '''詳細icon'''
    text=pygame.font.SysFont('simhei', 40)
    time_text=text.render('0:00',True,(0,0,0),(255,255,255))
    window.blit(time_text,(20,550))
    '''Bonus題目'''
    clock.tick(FPS)
    # event loop (user action)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
