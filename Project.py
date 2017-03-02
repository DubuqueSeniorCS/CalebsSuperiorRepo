from sense_hat import SenseHat
import time
import random
import pygame

from pygame.locals import *

pygame.init()
pygame.display.set_mode((640,480))
s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

direction = 0;
head = 0;
length = 1;
food = random.randint(1,63);

Field = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    ]

def Dead():
    G = green
    Y = yellow
    B = blue
    O = nothing
    R = red
    logo = [
    R, R, O, O, O, O, O, O,
    R, O, R, O, O, O, O, O,
    R, O, R, G, G, O, O, O,
    R, R, O, G, O, O, O, O,
    O, O, O, G, G, B, B, O,
    O, O, O, G, O, B, O, B,
    O, O, O, G, G, B, O, B,
    O, O, O, O, O, B, B, O
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo


running = True

while running: 

  if head == food:
    food = random.randint(1,63)
    length = length + 1
  
  G = green
  Y = yellow
  B = blue
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]

  for event in pygame.event.get():
      #print(event)
      if event.type == KEYDOWN:
          if event.key == K_RIGHT:
              direction = 0
          if event.key == K_UP:
              direction = 1
          if event.key == K_LEFT:
              direction = 2
          if event.key == K_DOWN:
              direction = 3
      if event.type == QUIT:
          running = False
          print("BYE")
  if direction == 0:
    if head%8==7:
      #head = head-8;
      running = False
    head+=1;
  if direction == 1:
    if head/8==0:
      #head +=56
      running = False
    else:
      head-=8;
  if direction == 2:
    if head%8==0:
      #head+=8;
      running = False
    head-=1;
  if direction == 3:
    if head/8==7:
      #head = 0;
      running = False
    else:
      head+=8;
  
  #direction = random.randint(0, 3);
  
  for x in range(0, 64):
    if Field[x] > 0:
      Field[x] = Field[x] - 1
  if Field[head] > 0:
      running = False
  else:
      Field[head] = length
  
  
  
  for x in range(0, 64):
    if Field[x]==0:
      logo[x]=O;
    else:
      logo[x]=(0,255/length*Field[x], 255/length*(length-Field[x]));
  s.set_pixels(logo)
  s.set_pixel(food%8,food/8,255,0,0)
  
  
    
  
    
  time.sleep(.25)



#s.set_pixels(Dead())
while True:
  logo = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O
  ]
  for x in range(0,64):
      logo[x] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
  s.set_pixels(logo)
  time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
