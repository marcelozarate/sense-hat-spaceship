from time import sleep
from random import randint
from sense_hat import SenseHat
sense = SenseHat()

sense.clear(0, 0, 0)

x = 4
#ratio 1 (hard) ++ (easier)
ratio=8
loops=0
score=0
asteroids=[]
rematch=True

O = (0,0,0)
R = (255,0,0)
G = (0,255,0)

big_V = [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,G,O,
    O,O,O,O,O,G,O,O,
    O,O,O,O,G,O,O,O,
    O,G,O,G,O,O,O,O,
    O,O,G,O,O,O,O,O,
    O,O,O,O,O,O,O,O
]

big_X = [
    O,O,O,O,O,O,O,O,
    O,R,O,O,O,O,R,O,
    O,O,R,O,O,R,O,O,
    O,O,O,R,R,O,O,O,
    O,O,O,R,R,O,O,O,
    O,O,R,O,O,R,O,O,
    O,R,O,O,O,O,R,O,
    O,O,O,O,O,O,O,O
]

def draw_ship():
    sense.set_pixel(x, 7, 255, 255, 255)
        
def asteroids_fall():
    global loops
    global score
    global ratio
    
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
          if (ratio>1):
            if(score % 5 == 0):
              ratio -= 1
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

def show_rematch():
    middlepressed=False
    option=1
    sense.show_message("Play again?", text_colour=(0, 255, 0))
    sense.set_pixels(big_V)
    event = sense.stick.wait_for_event()
    if(event.direction == "middle"):
            middlepressed=True
    while(middlepressed==False):
        if((event.direction == "left") and (event.action == "pressed")) or ((event.direction == "right") and (event.action == "pressed")):
            if (option == 1):
                option = 0
                sense.set_pixels(big_X)
            else:
                option = 1
                sense.set_pixels(big_V)
        if(event.direction == "middle"):
            middlepressed=True
        else:
            event = sense.stick.wait_for_event()
        print (event.action)
        print(event.direction)
    if (option == 1):
        return True
    else:
        return False

while rematch==True:
    score=0
    ratio=8
    asteroids = []
    while asteroids_fall():
        draw_ship()
        sleep(0.5)
        sense.clear(0, 0, 0)
    sense.show_message("Game Over - Score: "+str(score), text_colour=(255, 99, 71))
    rematch = show_rematch()
sense.show_message("Bye!", text_colour=(0,0,255))
sense.clear(0, 0, 0)
