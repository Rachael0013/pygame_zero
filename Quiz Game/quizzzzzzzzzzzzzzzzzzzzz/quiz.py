import pgzrun

WIDTH =1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 8

q1 = ["What is second last dynasty in China?", "Song dynasty", "Tang dynasty", "Yuan dynasty", "Ming dynasty", 4]
q2 = ["Who had more power than emperor in Japan?", "Daimyo", "Oda Nobunaga", "Shogun", "TOkugawa leyasu", 3]
q3 = ["What period is 100 BCE - 600 BCE?", "Korea (Silla,Baekje,Geoyreo)", "Han Dynasty", "Mongol's invasion", "Islam", 1]
q4 = ["Who unified Japan?", "Toyotomi Hideyoshi", "Oda Nobunaga", "Mongol", "Tokugawa Leyasu", 4]
q5 = ["Who is Temujin?","son of Khan", "Vikings", "Son of ogedei", "Janpan samurai", 1]
q6 = ["What was similar period with Han dynasty", "Constinople", "Song dynasty", "Taizong", "Roman Empire", 4]
q7 = ["What is Urbanization", "people go out from the city", "old city", " people go to city", "City", 3]
q8 = ["What is Chang An?", "Capital of Song", "Capital of Tang", "Capital of Yuan", "Capital of Han", 2]
q9 = ["what is Archipelago mean?", "spread of island", "spread of city", "chain of city", "chain of island", 4]
q10 = ["Where did Japan bring ideas?", "Korea and China", "Korea and Rome", "China and Rome", "Korea and colombia", 1]
q11 = ["What country did not have Confucianism?","Japan","Korea","America","China",3]
q12 = ["What group united Korea?", "Goryo", "Baekjae", "Silla", "Choseon", 3]
q13 = ["What is not describing Korea's Geography?", "Temperate Climate", "Ideas from Japan", "Peninsula", "Mountainous", 2]
q14 = ["What was same period with korea(silla, baekjae...)?","islam", "Egypt","spain","Rome", 4]
q15 = ["What is this subject about?","Geography","History","Study","ancient",2]



questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12,q13,q14,q15]
question = questions.pop(0)



def draw():
    screen.fill("khaki")
    screen.draw.filled_rect(main_box, "medium turquoise")
    screen.draw.filled_rect(timer_box, "medium turquoise")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "pale turquoise")

    screen.draw.textbox(str(time_left), timer_box, color = ("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

def game_over():
    global question, time_left
    message = "GAME OVER. YOU GOT %s QUESTIONS CORRECT" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("CLicked on answer" + str(index))
            if index == question[5]:
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

def on_key_up(key):
    global score
    if key == keys.SPACE:
        score =  score - 1
        correct_answer()

clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()