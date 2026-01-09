import random,time,turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
player = turtle.Turtle()
player.shape("triangle")
player.setheading(90)
player.color("red")
player.penup()
player.goto(0,-250)
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-200,260)
score_display.write("Score: 0", font=("Arial", 16, "normal"))
balloons = []
screen.setup(width=500, height=600)

running = True

def create_balloon():
    balloon = turtle.Turtle()
    balloon.shape("circle")
    balloon.color(random.choice(["red","blue","green","yellow","purple","orange"]))
    balloon.penup()
    x = random.randint(-400,400)
    y = random.randint(-350,350)
    balloon.goto(x,y)
    balloon.speed(random.uniform(1,5)) 
    if random.random() < 0.2:
        balloon.color("black")
        balloon.is_bomb = True
    balloons.append(balloon)

def update_score(points):
    global score
    score += points
    score_display.clear()
    score_display.write("Score: {}".format(score), font=("Arial", 16, "normal"))

def move_left():
    x = player.xcor() -30
    if x < -500:
        player.setx(x)

def move_right():
    x = player.xcor() +30
    if x > 500:
        player.setx(x)

def game_over():
 global running
 running = False
 game_over_display = turtle.Turtle()
 game_over_display.hideturtle()
 game_over_display.penup()
 game_over_display.color("red")
 game_over_display.write("Game Over!".format(score), align="center", font=("Arial", 24, "normal"))
 screen.update()
 time.sleep(3)
 screen.bye()

screen.tracer(0)
screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

game_speed = 0.02
difficulty_increase = 0.001
spawn_interval = 2
last_spawn_time = time.time()


while running:
    screen.update()
    current_time = time.time()

    if current_time - last_spawn_time > spawn_interval:
        create_balloon()
        last_spawn_time = current_time


    for balloon in balloons[:]:
        balloon.sety(balloon.ycor() - balloon.speed())
        if balloon.ycor() < -600:
            balloon.hideturtle()
            balloons.remove(balloon)


        if balloon.distance(player) < 30:
            if balloon.is_bomb:
                game_over()
            else:
                update_score(5)
                balloon.hideturtle()
                balloons.remove(balloon)        

game_speed = max(0.005, game_speed - difficulty_increase)
spawn_interval = max(0.5, spawn_interval - 0.0005)

turtle.done()
