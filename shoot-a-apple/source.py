import pgzrun
from random import randint

score = 0

apple = Actor("apple")  # 이미지 가지고오는 것

# 화면에 그리는 것
def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


# 마우스 클릭 이벤트
def on_mouse_down(pos):
    global score                # 밖에서 변수를 가지고 오는 것

    if apple.collidepoint(pos): # 사과 클릭했을때
        score = score + 1
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        print("score :", score) 
        quit()                  # 게임 강제 종료

place_apple()
pgzrun.go()

# 사과를 클릭했을떄 점수가 1점식 올라감/ 마지막에 점수 계산해서 터미널화면에 보여줌
# 사과 클릭했을떄 소리남