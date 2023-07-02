import pgzrun
from random import randint
import os

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(900, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(900, 1600), 460

tree =  Actor("tree")
tree.pos = randint(900, 1600), 450

bird_up = True
up = False
game_over = False
score = 1
number_of_updates = 0
level = .7
levelup_time = 0
pass_monster = 0

scores = []
         
def update_high_scores():
    global score, scores
    filename = "high-scores.txt"
    scores = []
    with open(filename, 'r') as file:
        line = file.readline()
        high_scores = line.split()
    for high_score in high_scores:
        if (score > int(high_score)):
            scores.append(str(score) + " ")
            score = int(high_score)
        else:
            scores.append(str(high_score) + " ")
    with open(filename, 'w') as file:
        for s in scores:
            file.write(s)

def display_high_scores():
    screen.draw.text("HIGH SCORES", (350, 150), color = "black")
    y = 175
    rank = 1
    for s in scores:
        screen.draw.text(str(rank) + ", " + s, (350, y), color = "black")
        y += 25
        rank += 1

def draw():
    screen.blit("background", (0,0))
    if not game_over:
        screen.draw.text("Level: " + str(level), (100, 5), color="black")
        balloon.draw()
        tree.draw()
        bird.draw()
        house.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_scores()

def on_key_down(key):
    if key == keys.SPACE:
        global up
        up = True
        balloon.y -= 50  
 
def on_key_up(key):
    if key == keys.SPACE:
        global up
        up = False     

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def update():
    global game_over, score, number_of_updates, level, pass_monster
    if not game_over:
        if not up:
            balloon.y += 1

        if bird.x > 0:

            bird.x -= 4 * level
            bird.y += (randint(0, 7) - 3)
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            pass_monster += 1
            if pass_monster == 3:
                level += 1
                pass_monster = 0
            bird.x = randint (900, 1600)
            bird.y - randint(10, 200)
            score += 1
            number_of_updates = 0

        if house.right > 0:
            house.x -= 2 * level
        else:
            pass_monster += 1
            if pass_monster == 3:
                level += 1
                pass_monster = 0
            house.x = randint(900, 1600)

        if tree.right > 0:
            tree.x -= 2 * level
        else:
            pass_monster += 1
            if pass_monster == 3:
                level += 1 
                pass_monster = 0
            tree.x = randint(800,1600)

        if balloon.top > 0 and balloon.bottom < 560:
            pass
        else:
            game_over = True
            update_high_scores()

        if balloon.collidepoint(bird.x, bird.y) or \
        balloon.collidepoint(house.x, house.y) or \
        balloon.collidepoint(tree.x, tree.y):
            game_over = True
            update_high_scores()







pgzrun.go()