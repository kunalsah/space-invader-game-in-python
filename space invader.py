#space invaders

import turtle
import os
import math
import random
import winsound

#setup the screen
wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#drawing border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#registering shapes
shapes=["enemy.gif","player.gif"]
for shape in shapes:
	turtle.register_shape(shape)

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 20

#Choose a number of enemies
number_of_enemies = 10
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())
for enemy in enemies:
	enemy.shape("enemy.gif")
	enemy.color("cyan")
	enemy.penup()
	enemy.speed(0)
	enemy.setheading(-90)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 4

#creating player bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_wid=1,stretch_len=0.05)
bullet.hideturtle()

bulletspeed = 60

#define bullet state
# ready - ready to fire
#fire - bullet is firing
bulletstate ="ready"


#move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -290:
		x = -290
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 290:
		x = 290
	player.setx(x)

def fire_bullet():
	#declare bulletstate as global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		
		bulletstate = "fire"
		#move the bullet just above the player
		x = player.xcor() - 2
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()
		winsound.PlaySound("attack.wav",winsound.SND_ASYNC)

def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 24:
		return True
	else:
		return False
#keyboard binding
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space") 

#Main game loop
while True:
	
	#Move the enemy
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
			
		#Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			winsound.PlaySound("destroy.wav",winsound.SND_ASYNC)
			#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		
		if isCollision(player, enemy):
			winsound.PlaySound("player destroy.wav",winsound.SND_ASYNC)
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			exit()


	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"


delay = raw_input("Press enter to finsh.")