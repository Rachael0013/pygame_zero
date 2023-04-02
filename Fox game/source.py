import pgzrun
from random import randint 

WIDTH = 400
HEIGHT = 400

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200,200
hedgehog = Actor("hedgehog")
hedgehog.pos = 200,200


def draw():
    screen.fill("green")        #배경색깔 칠하는것

    fox.draw()
    coin.draw()
    hedgehog.draw()

    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
    

def place_coin():       #코인을 랜덤 장소로 옴기는 것
    coin.x = randint(20, (WIDTH + 20))
    coin.y = randint(20, (HEIGHT + 20))


def place_hedgehog():
    hedgehog.x = randint(10, 400)
    hedgehog.y = randint(10, 400)


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2

    if keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2 

    coin_collected = fox.colliderect(coin)          #여우그림이 코인에 부디쳤을떄 혹은 겹쳤을떄
    touch_hedgehog = fox.colliderect(hedgehog)
    overlap_together = coin.colliderect(hedgehog)

    if coin_collected:
        score = score + 10      #score = score + 10 이랑 score += 10이랑 똑같은것
        place_coin()
        place_hedgehog()
    elif touch_hedgehog:
        score = score - 10
        place_hedgehog()
        place_coin()
    elif overlap_together:
        time_up()               #끝내는것       
        

clock.schedule(time_up, 20.0)        #시간 예약해주는 것
place_coin()
place_hedgehog()

pgzrun.go()

#장애물을 설치하고 장애물을 건드렸을때 점수 10만큼 줄어들음