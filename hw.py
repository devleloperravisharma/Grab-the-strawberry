import pgzrun

import random


TITLE = "Grab the Strawberries"

WIDTH = 600

HEIGHT = 500

score = 0

game_over = False

'--------------------------------------------------------------------------------------------------------------------------------------------------'

strawberry = Actor("strawberr")
basket = Actor('baske')

strawberry.pos = (100,100)

basket.pos = (30,30)

def draw():
    screen.blit("pink", (0,0))
    strawberry.draw()
    basket.draw()
    screen.draw.text("Score: "+str(score), color = (255, 255, 255), topleft = (10,10))

    if game_over:
        screen.fill("#ffffff")
        screen.draw.text("Game Over!", color = "pink", midtop = (WIDTH/2, HEIGHT/2-50), fontsize = 40)
        if score<10:
                screen.draw.text("loser!", color = "pink", midtop = (WIDTH/2, HEIGHT/2), fontsize = 30)
        else:
            screen.draw.text("winner", color = "pink", midtop = (WIDTH/2, HEIGHT/2), fontsize = 30)

def time_up():
    global game_over
    game_over = True





def movest():
    strawberry.x = random.randint(50, WIDTH-50)
    strawberry.y = random.randint(50, WIDTH-50)

'--------------------------------------------------------------------------------------------------------------------------------------------------'
def update():
    global score
    if keyboard.up:
        basket.y -= 5
    if keyboard.down:
        basket.y += 5
    if keyboard.left:
        basket.x -= 5
    if keyboard.right:
        basket.x += 5
    if basket.colliderect(strawberry):
        score += 1
        movest()

clock.schedule(time_up, 60.0)
'--------------------------------------------------------------------------------------------------------------------------------------------------'



pgzrun.go()