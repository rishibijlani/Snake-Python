from turtle import *
from random import randrange, randint
from shit import square, vector
import easygui

food = vector(0,0)
snake = [vector(10,0)]
dir = vector(0,-10)

def change(x, y):
	dir.x = x
	dir.y = y

def drawCirc(x, y):
	up()
	goto(x,y)
	down()
	fillcolor("chartreuse")
	begin_fill()
	circle(5)
	end_fill()

def wRite():
	color("pale turquoise")
	x = randrange(22,52)
	cOlour = ["pale turquoise", "olive drab", "snow", "seashell4", "lime green", "yellow"]
	z=randint(0,5)
	color(cOlour[z])
	write("SNACKS.lmaIO", move = False, align="center", font=("Comic Sans MS", x, "normal"))

def BG():
	backgrnd = ["black", "dark gray", "gold", "light yellow"]
	x = randint(0,3)
	bgcolor(backgrnd[x])


def inside(head):
	#write code for portal level jazz across screen here
	return True

def moveSnake():
	head = snake[-1].copy()
	head.move(dir)

	if not inside(head) or head in snake:
		square(head.x, head.y, 9, 'red')
		update()
		easygui.msgbox("Get reKt n00b!", title=":(")
		return

	snake.append(head)

	if head == food:
		print('current score: ',len(snake))
		food.x = randrange(-20, 20) * 10
		food.y = randrange(-20, 20) *10
	else:
		snake.pop(0)

	clear()

	for body in snake:
		square(body.x, body.y, 9, 'dark violet')

	drawCirc(food.x, food.y)
	#square(food.x,food.y, 9, 'green')
	update()
	wRite()
	#BG()
	#write("SNACKS.lmaIO", move = False, align="center", font=("Comic Sans MS", 52, "normal"))
	ontimer(moveSnake, 35)

title("slither.io 18th century")
#backgrnd = ["black", "dark gray", "gold", "light yellow"]
#bg=randint(0,3)
bgcolor("dark gray")
bgcolor("yellow")
#bgcolor(backgrnd[bg])
wRite()
color("pale turquoise")
setup(560.0, 560.0, 370, 150)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10,0), 'Left')
onkey(lambda: change(0,10), 'Up')
onkey(lambda: change(0,-10), 'Down')
moveSnake()
done()
