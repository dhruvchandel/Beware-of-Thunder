import sys
import time
import pygame
import pyautogui
from random import randint

pygame.init()


# Adding Music to the game
pygame.mixer.music.load('groovyhiphop.mp3')
pygame.mixer.music.play(-1)
# Resolution of the screen
res = pyautogui.size()
res= (res[0], res[1])

screen = pygame.display.set_mode(res)
pygame.display.set_caption("DC: Beware Of Thunder")

clock = pygame.time.Clock()

character_pos = [res[0]//2,res[1]-2*res[1]//10]
rain_drop_pos = [randint(0,res[0]),0]
cloud_pos = [ [res[0]-res[0]//10,0] , [res[0]-3*(res[0]//10),0] , [res[0]-(6*res[0]//10),0] , [res[0]-(8*res[0]//10),0] , [res[0]-(5*res[0]//10),0] , [0,0]]

background_image = pygame.image.load("rainy_toronto.jpg").convert()
background_image = pygame.transform.scale(background_image, res)

scale_factor_character = (res[1]//20, 2*(res[1]//20))
scale_factor_enemy = (3*(res[1]//40), 4*(res[1]//40))


# Importig the character Sprite
character = pygame.image.load("stand_man.png").convert_alpha()
character = pygame.transform.scale(character, scale_factor_character )


# Importing the Enemy Sprite
rain_drop = pygame.image.load("drop.png").convert_alpha()
rain_drop = pygame.transform.scale(rain_drop, scale_factor_enemy)

# Importig the character Sprite
scale_factor_cloud = (res[1]//6, res[1]//6)
cloud = pygame.image.load("cloud.png").convert_alpha()
cloud = pygame.transform.scale(cloud, scale_factor_cloud )

# Attributes Of Enemies
enemy_count = 15
max_enemy = 15
rain_drop_pos = []
drop_rate = 0.1*res[1]


for _ in range(0, max_enemy) :
	rain_drop_pos.append([randint(0,res[0]),randint(-res[1]/0.8,0)]) #0])

def DrawCharacter() :
	screen.blit(background_image, [0,0])
	screen.blit(character, character_pos)

def CreateEnemy(z) :
	global rain_drop_pos 
	rain_drop_pos[z] = [randint(0,res[0]),0]

def DrawEnemy(z) :
	screen.blit(rain_drop, rain_drop_pos[z])
	rain_drop_pos[z][1] += drop_rate

def DrawClouds(z) :
	screen.blit(cloud, cloud_pos[z])

def IncreaseDifficulty() :
	global drop_rate
	drop_rate += 5

Game_Score = 0

game_over = False

# The main game Loop
while not game_over:

	for event in pygame.event.get() :

		if event.type == pygame.QUIT :
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT :
				if character_pos[0] >0 :
					character_pos[0] -= res[0]//50
			elif event.key == pygame.K_RIGHT :
				if character_pos[0] < res[0]-res[1]//10 :
					character_pos[0] += res[0]//50

	DrawCharacter()
	for _ in range(0,enemy_count) :
		DrawEnemy(_)
		if rain_drop_pos[_][1] >= res[1] :
			Game_Score += 1
			print(Game_Score)
			CreateEnemy(_)

	for _ in range(0,6) :
		DrawClouds(_)

	for _ in range (0,enemy_count) :
		if rain_drop_pos[_][0]>character_pos[0] and rain_drop_pos[_][0] <character_pos[0]+scale_factor_character[0]:
			if rain_drop_pos[_][1]>character_pos[1] and rain_drop_pos[_][1] < character_pos[1]+scale_factor_character[1] :
				game_over = True
				pygame.mixer.music.load('thunder.mp3')
				pygame.mixer.music.play(-10)
			elif rain_drop_pos[_][1]+scale_factor_enemy[1]> character_pos[1] and rain_drop_pos[_][1]+scale_factor_enemy[1] < character_pos[1]+scale_factor_character[1] :
				game_over = True
				pygame.mixer.music.load('thunder.mp3')
				pygame.mixer.music.play(-10)
		elif rain_drop_pos[_][0]+scale_factor_enemy[0] >character_pos[0] and rain_drop_pos[_][0]+scale_factor_enemy[0] <character_pos[0]+scale_factor_character[0]:
			if rain_drop_pos[_][1]>character_pos[1] and rain_drop_pos[_][1] < character_pos[1]+scale_factor_character[1] :
				game_over = True
				pygame.mixer.music.load('thunder.mp3')
				pygame.mixer.music.play(-10)
			elif rain_drop_pos[_][1]+scale_factor_enemy[1]> character_pos[1] and rain_drop_pos[_][1]+scale_factor_enemy[1] < character_pos[1]+scale_factor_character[1] :
				game_over = True
				pygame.mixer.music.load('thunder.mp3')
				pygame.mixer.music.play()


	font = pygame.font.Font(None, 36)
	text = font.render("Score : "+str(Game_Score), 1,(255,255,255),(0,0,0))
	textpos = [0,0]
	screen.blit(text, textpos)

	clock.tick(60)
	pygame.display.update()

	if game_over== True :
		font = pygame.font.Font(None, res[0]//6)
		text = font.render("GAME OVER !!!\nYour Score : " + str(Game_Score), 1,(255,255,255),(0,0,0))
		textpos = [res[0]/5, res[1]/3]
		screen.blit(text, textpos)
		pygame.display.update()



time.sleep(3)
