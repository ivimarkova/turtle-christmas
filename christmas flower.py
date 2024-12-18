import turtle
import random
import time

#настройка на екрана и цветовете
s=turtle.Screen()
s.bgcolor("black")
s.tracer(0)  # Спира автоматичното обновяване на екрана за по-плавна анимация
turtle.color("green")

#поставяне на текста над цветето
turtle.penup()
turtle.goto(0,250)#позиция над цветето
turtle.write("Merry Christmas",align="center",font=("Times New Roman",25,"bold"))
turtle.hideturtle()#скрива костенурката, която пише текста

#рисуване на цветето
s.tracer(1) #вкл временно авт-то обновяване
t=turtle.Turtle()
t.pencolor("red")
t.speed(0)
for i in range (150):
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)
t.hideturtle()
s.tracer(0)#изкл авт обновяване

#snowflake
def create_snowflake():
    flake=turtle.Turtle()
    flake.shape("circle")
    flake.color("white")
    flake.penup()
    flake.speed(0)
    flake.goto(random.uniform(-300,300), random.uniform(200,400))#start position на върха
    flake.showturtle()  # Показване на снежинката след позиционирането
    return flake

def snow_fall(snowflakes):
    for flake in snowflakes:
        y=flake.ycor()-random.uniform(2,5)#по-бавно движение надолу
        if y<-300: #ако падне под екрана, започва отново от върха
            flake.goto(random.randint(-300,300),random.randint(200,400))
        else:
            flake.sety(y)
snowflakes=[create_snowflake()for _ in range(100)]# a lot of snowflakes
while True:
    snow_fall(snowflakes)
    time.sleep(0.03)#control fall speed
    s.update()#обновяване на екрана

#задържане на екрана отворен
turtle.done()