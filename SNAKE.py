import pygame
import random
import os
pygame.mixer.init()
pygame.init()
screen_width=900
screen_height=500
gameWindow=pygame.display.set_mode((screen_width,screen_height))
bgimg=pygame.image.load(r'C:\Users\Adarsh C. Shetty\snake\pic3.jpg')
bgimg=pygame.transform.scale(bgimg,[screen_width,screen_height]).convert_alpha()
bgimg1=pygame.image.load(r'C:\Users\Adarsh C. Shetty\snake\pic2.jpg')
bgimg1=pygame.transform.scale(bgimg1,[screen_width,screen_height]).convert_alpha()
pygame.display.set_caption("SNAKES WITH ADARSH")
pygame.display.update()
Clock=pygame.time.Clock() 
font=pygame.font.SysFont(None,40)
def homepage():
    exit_game=False
    while not exit_game:
        gameWindow.fill((225,220,150))
        gameWindow.blit(bgimg1,(0,0))
        display1("Welcome To Snake Game",(255,250,250),275,200)
        display1("Press Enter To Play",(255,250,250),295,245)
        for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:  
                            gamecontrol()
        pygame.display.update()
        Clock.tick(60)                
def display1(text,color,x,y):
    sc_text=font.render(text,True,color)
    gameWindow.blit(sc_text,(x,y))
def plot_snake(gameWindow,color,snake_list,s_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,(0,0,0),[x,y,s_size,s_size])    
def gamecontrol():
        exit_game=False
        game_over=False
        co_x=50
        co_y=50
        speed_x=0
        speed_y=0
        apple_x=random.randint(20,screen_width/2)
        apple_y=random.randint(20,screen_height/2)
        s_size=25
        init_speed=5
        score=0
        fps=30
        snake_list=[]
        snake_len=1
        if(not os.path.exists("highscore.txt")):
            with open("highscore.txt","w") as f:
                f.write("0")
        with open("highscore.txt","r") as f:
            highscore=f.read()
        while not exit_game:
            if game_over:
                with open("highscore.txt","w") as f:
                    f.write(str(highscore))
                gameWindow.fill((255,255,255))
                gameWindow.blit(bgimg1,(0,0))
                display1("GAME OVER! PRESS ENTER TO CONTINUE",(255,255,255),200,200)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            gamecontrol()    
            else:    
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            speed_x=init_speed
                            speed_y=0
                        if event.key==pygame.K_LEFT:
                            speed_x=-init_speed
                            speed_y=0
                        if event.key==pygame.K_UP:
                            speed_y=-init_speed
                            speed_x=0
                        if event.key==pygame.K_DOWN:
                            speed_y=init_speed
                            speed_x=0 
                co_x+=speed_x
                co_y+=speed_y      
                if abs(co_x-apple_x)<8 and abs(co_y-apple_y)<8:
                    score+=5
                    snake_len+=5
                    apple_x=random.randint(20,screen_width/2)
                    apple_y=random.randint(20,screen_height/2)  
                    pygame.mixer.music.load(r'C:\Users\Adarsh C. Shetty\snake\beep.mp3')
                    pygame.mixer.music.play()      
                    if score>int(highscore):
                        highscore=score
                gameWindow.fill((255,255,255)) 
                gameWindow.blit(bgimg,(0,0))
                display1("Current Score :  "+ str(score)+"  Highscore :  "+ str(highscore),(0,0,139),5,5)
            # pygame.draw.rect(gameWindow,black,[co_x,co_y,s_size,s_size]) 
                pygame.draw.rect(gameWindow,(255,0,0),[apple_x,apple_y,15,15])
                head=[]
                head.append(co_x)
                head.append(co_y)
                snake_list.append(head)
                if len(snake_list)>snake_len:
                    del snake_list[0]
                if head in snake_list[:-1]:
                    game_over=True
                    pygame.mixer.music.load(r'C:\Users\Adarsh C. Shetty\snake\home.mpeg')
                    pygame.mixer.music.play()        
                if co_x<0 or co_x>screen_width or co_y<0 or co_y>screen_height:
                    game_over=True 
                    pygame.mixer.music.load(r'C:\Users\Adarsh C. Shetty\snake\home.mpeg')
                    pygame.mixer.music.play()      
                plot_snake(gameWindow,(0,0,0),snake_list,s_size)
            pygame.display.update() 
            Clock.tick(fps) 
        pygame.quit()
        quit()  
pygame.mixer.music.load(r'C:\Users\Adarsh C. Shetty\snake\INTRO.mpeg')
pygame.mixer.music.play()            
homepage()