from time import sleep
from random import randint
from sense_hat import SenseHat
sense = SenseHat()

sense.clear(0, 0, 0)

x = 4
#ratio 1 (hard) ++ (easier)
ratio=3
loops=0
score=0
asteroids=[]

def draw_ship():
    sense.set_pixel(x, 7, 255, 255, 255)
        
def asteroids_fall():
    global loops
    global score
    
    for a in asteroids:
        sense.set_pixel(a[0], a[1], 0, 0, 0)

    # Adding new asteroid
    if (loops % ratio == 0):
        asteroids.insert(0,[randint(0,7),0])
    
    for a in asteroids:
        # Hitting an asteroid
        if ((a[0] ==x ) & (a[1]==7)):
          return False
        # Brown
        sense.set_pixel(a[0], a[1], 210, 105, 30)
    	# Asteroid out of screen
        if a[1]==7:
          asteroids.pop()
          score += 1
        # Asteroid moving down
        else:
          a[1] += 1

    loops += 1
    return True

def move_left(event):
    global x
    if x > 0 and event.action=='pressed':
        x -= 1

def move_right(event):
    global x
    if x < 7 and event.action=='pressed':
        x += 1

sense.stick.direction_left = move_left
sense.stick.direction_right = move_right

while asteroids_fall():
    draw_ship()
    sleep(0.5)
    sense.clear(0, 0, 0)
    
sense.show_message("Game Over - Score: "+str(score), text_colour=(255, 99, 71))
