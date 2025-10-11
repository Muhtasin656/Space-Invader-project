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



# player
player_image=pygame.image.load("player (1).png")
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
    enemy_image.append(pygame.image.load("enemy (1).png"))
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_ymin,enemy_start_ymax))
    enemy_xchange.append(enemy_speedx)
    enemy_ychange.append(enemy_speedy)


# bullet
bullet_image=pygame.image.load("bullet (1).png")
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
def player(x,y):
    screen.blit(player_image,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_image,(x+16,y+10))
def is_collision(enemyx,enemyy,bullet_x,bullet_y):
    distance=math.sqrt((enemyx-bullet_x)**2+(enemyy-bullet_y)**2)
    return collision_distance>distance
#creating game loop
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(pygame.image.load("download (1).jpeg"),(0,0))
for event in pygame.event.get():
    if event.type==pygame.QUIT:
        running=False
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            player_xchange=-5
        if event.key==pygame.K_RIGHT:
            player_xchange=5
        if event.key==pygame.K_SPACE and bullet_state=="ready":
            bullet_x=playerx
            fire_bullet(bullet_x,bullet_y)
    if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
        player_xchange=0
# player movement
playerx=playerx+player_xchange
playerx=max(0,min(playerx,screen_width-64))
for i in range(number_of_enemy):
    if enemyy[i]>340:
        for j in range(number_of_enemy):
            enemyy[j]=2000
        game_over_text()
        break
    enemyx[i]+=enemy_xchange[i]
    if enemyx[i]<=0 or enemyx[i]>=screen_width-64:
        enemy_xchange[i]=enemy_xchange[i]*-1
        enemyy[i]=enemyy[i]+enemy_ychange[i]
if is_collision(enemyx[i],enemyy[i],bullet_x,bullet_y):
    bullety=player_start_y
    bullet_state="ready"
    score_value=score_value+1
    enemyx[i]=random.radint(0,screen_width-64)
    enemyy[i]=random.randint(enemy_start_ymin,enemy_start_ymax)
enemy(enemyx[i],enemyy[i],i)
if bullet_y<=0:
    bullet_y=player_start_y
    bullet_state="ready" 
elif bullet_state=="fire":
    fire_bullet(bullet_x,bullet_y)
    bullet_y=bullet_y-bullet_ychange
player(playerx,playery)
show_score(text_x,text_y)
pygame.display.uodate()