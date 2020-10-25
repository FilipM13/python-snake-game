import pygame
import os
import random
import time
#variables
width = 800       #window width
height = 800      #window height
x_min = 100       #game area starting x point
y_min = 100        #game area starting y point
x_max = x_min+600 #game area width
y_max = y_min+600 #game area height

#pygame window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('snake')

#prepering fonts
pygame.font.init()

#snake bodypart class and array
snake = [[400, 200]]

#food object
food = {'x_position':400, 'y_position':350}

#bg image
bg1 = pygame.transform.scale(pygame.image.load(os.path.join('images', 'background1.png')), (x_max-x_min, y_max-y_min))
bg2 = pygame.transform.scale(pygame.image.load(os.path.join('images', 'background2.png')), (width, height))

#main loop
def main():
  run = True
  end = False
  fps = 6
  clock = pygame.time.Clock()
  font = pygame.font.SysFont('comicsans', 40)

  v_speed = 1
  h_speed = 0
  vector = 10
  #loosing the game
  def lost():
    #you lost label and lenght of snake label
    lost_label = font.render(f'You lost! Your score is {len(snake)-1}!', 1, (240, 0, 20))
    window.blit(lost_label, (width/2-lost_label.get_width()/2, height/2-lost_label.get_height()/2))
    pygame.display.update()
    #again btn
    #quit btn
    return None
  def win():
    #you won label and lenght of snake label
    lost_label = font.render(f'You won! Your score is {len(snake)-1}!', 1, (240, 0, 20))
    window.blit(lost_label, (width/2-lost_label.get_width()/2, height/2-lost_label.get_height()/2))
    pygame.display.update()
    #again btn
    #quit btn
    return None
  #extending body after getting food
  def extend_body():
    l = len(snake)
    s = snake[l-1]
    snake.append([s[0], s[1]])
    return None
  #generate random food
  def new_food():
    food['x_position'] = random.choice([i for i in range(x_min, x_max, 10)])
    food['y_position'] = random.choice([i for i in range(y_min, y_max, 10)])
    for i in range(len(snake)):
      if snake[i][0] == food['x_position'] and snake[i][1] == food['y_position']:
        new_food()
    return None
  #updating view
  def draw():
    #drawing background
    window.blit(bg2, (0,0))
    window.blit(bg1, (x_min,y_min))
    #drawing food
    pygame.draw.rect(window, (200,20,0), (food['x_position'], food['y_position'], 10, 10))
    #drawing snake
    for i in range(len(snake)):
      if i == 0:
        pygame.draw.rect(window, (0,220,0), (snake[i][0], snake[i][1], 10, 10))
      elif i == len(snake)-1:
        pygame.draw.rect(window, (130,180,0), (snake[i][0], snake[i][1], 10, 10))
      else:
        pygame.draw.rect(window, (130,150,0), (snake[i][0], snake[i][1], 10, 10))
    #updating display
    pygame.display.update()
    return None

  while run:
    clock.tick(fps)

    #stop game
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #check for collision
    if snake[0][0] == food['x_position'] and snake[0][1] == food['y_position']:
      #extend snake
      extend_body()
      #generate new food
      new_food()
    
    #turning a snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and h_speed == 0:  #left
      h_speed = -1
      v_speed = 0
    if keys[pygame.K_d] and h_speed == 0:  #right
      h_speed = 1
      v_speed = 0
    if keys[pygame.K_w] and v_speed == 0: #up
      h_speed = 0
      v_speed = -1
    if keys[pygame.K_s] and v_speed == 0: #down
      h_speed = 0
      v_speed = 1

    
    draw()
    #dead check
    if snake[0][0]+h_speed*vector > x_max-10: #border right
      v_speed, h_speed = 0, 0
      lost()
    elif snake[0][0]+h_speed*vector < x_min: #border left
      v_speed, h_speed = 0, 0
      lost()
    elif snake[0][1]+v_speed*vector > y_max-10: #border top
      v_speed, h_speed = 0, 0
      lost()
    elif snake[0][1]+v_speed*vector < y_min: #border btm
      v_speed, h_speed = 0, 0
      lost()
    for i in range(len(snake)):
      for ii in range(i+2,len(snake)):
        if snake[i][0]==snake[ii][0] and snake[i][1]==snake[ii][1]:  
          v_speed, h_speed = 0, 0
          lost()
    if v_speed==0 and h_speed==0:
      lost()
    if len(snake) == 3600:
      v_speed, h_speed = 0, 0
      win()

    
    
    #update body field memory
    for i in range(len(snake)-1, 0, -1):
      snake[i][0] = snake[i-1][0]
      snake[i][1] = snake[i-1][1]
    #moving snake head
    snake[0][0] += h_speed*vector
    snake[0][1] += v_speed*vector

#run game
main()

#ToDo:
#lost label
#win label
#quit and again btn