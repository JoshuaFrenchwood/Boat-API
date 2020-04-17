# -*- coding: utf-8 -*-
"""
Instructions:
1. Press the green Run button above
2. Wait for blue screen to appear
3. When Blue Screen Appears, click mouse on the blue Screen
4. Use arrow keys to change directions and speed

Press Up: Increase speed
Press Down: Reduce speed
Press S: To send data to data base
Press R: Retrieve data from data base
Press esc: End The Game
Hold Left: Turn left
Hold Right: Turn Right

OS: Linux/Windows , Mac?

@author: Joshua Frenchwood
"""
import BoatApi as api
import random 
import pygame
from os import path

#Linux and Windows image finder
img_dir = path.join(path.dirname(__file__), 'img')

#Window Settings
WIDTH = 600
HEIGHT = 500
FPS = 30

#usefull colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Initialize Pygame and create Window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boat Simulator")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial',bold=1)

def draw_text(surf, text, size, x , y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
    
def convert_angle(angle):
    if angle > 180 and angle< 360:
        return angle - 360
    return angle

def rudder_angle_convert(converted):
    return -1* converted
        
class Rudder(pygame.sprite.Sprite):
    #Sprite for Boat
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.transform.scale(rudder_img,(100,250))
        self.original_image.set_colorkey(BLACK)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.rot = 0
        self.rot_speed = 1
        self.boat_speed = 0
        self.last_update = pygame.time.get_ticks()
    def rotate(self, left, right):
        if convert_angle(self.rot) == 35:
            self.rot = self.rot -1
            print('Cannot Go Past 35 Degree Range')
            return self.rot
        if convert_angle(self.rot) == -35:
            self.rot = self.rot + 1
            print('Cannot Go Past 35 Degree Range')
            return self.rot
        if left == True:
            self.rot = (self.rot + self.rot_speed) % 360
        if right == True:
            self.rot = (self.rot - self.rot_speed) % 360
        new_img = pygame.transform.rotate(self.original_image, self.rot)
        old_center = self.rect.center
        self.image = new_img
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        return self.rot
            
    def update(self):
        keyState = pygame.key.get_pressed()
        num = self.rot
        if keyState[pygame.K_RIGHT]:
            num = self.rotate(False, True)
        if keyState[pygame.K_LEFT]:
            num = self.rotate(True, False)
        return num
    
#Load All game graphics
rudder_img = pygame.image.load(path.join(img_dir, 'rudder3.PNG')).convert()

#Sprites
all_sprites = pygame.sprite.Group()
rudder= Rudder()
all_sprites.add(rudder)


# Game Loop 
running = True # Set to false to end game

speed = 0
anlge = 0

apiData = {'speed':0 , 'direction':0}

while running:
        #Keep running at Right Speed, Keep FPS
        clock.tick(FPS)
        #********************process input (events)****************************
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                running = False
                    
        #**********************Update******************************************
        all_sprites.update()
        
        #********************Draw / render************************************
        screen.fill(BLUE)
        all_sprites.draw(screen)
        
        #Doulbe Buffering display to increase RT game speed *AFTER DRAWINGS*
        pygame.display.flip()
        
pygame.quit()

