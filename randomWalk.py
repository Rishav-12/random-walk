import random
import turtle

def random_walk():
	x = y = 0
	while True:
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		
		step = random.choice(['n', 's', 'e', 'w']) # Choosing direction randomly
		if step == 'n':
			y += 1
		elif step == 's':
			y -= 1
		elif step == 'e':
			x += 1
		else:
			x -= 1

		walker.color((r, g, b))
		walker.goto(x*20, y*20)

# Set Up
win = turtle.Screen()
win.colormode(255)
walker = turtle.Turtle() # Our Turtle object
walker.pensize(5)
walker.speed(3)
walker.hideturtle()

random_walk()
turtle.mainloop()
