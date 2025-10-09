import random
import math
import pygame
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_ymin=50
enemy_start_ymax=150
enemy_speedx=4
enemy_speedy=40
bullet_speedy=10
collision_distance=27

pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo(1).png")
pygame.display.set_icon(icon)


# player
player_image=pygame.image.load("player(1).png")
playerx=player_start_x
playery=player_start_y
player_xchange=0


# enemy
enemy_image=[]
enemyx=[]
enemyy=[]
enemy_xchange=[]
enemy_ychange=[]
number_of_enemy=10
for _i in range(number_of_enemy):
    enemy_image.append(pygame.image.load("enemy(1).png"))
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_ymin,enemy_start_ymax))
    enemy_xchange.append(enemy_speedx)
    enemy_ychange.append(enemy_speedy)


# bullet
bullet_image=pygame.image.load("bullet(1).png")
bullet_x=0
bullet_y=player_start_y
bullet_xchange=0
bullet_ychange=bullet_speedy
bullet_state="ready"


# score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
text_x=10
text_y=10


# game over text
over_font=pygame.font.Font("freesansbold.ttf",64)
# functions
def show_score(x,y):
    score=font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))