import time
import board
import neopixel
import random

pixel_pin = board.A1
num_pixels = 60

 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=(0, 1, 2, 3))
#pixels.auto_write=False
 
UB = 0.4
LB = 10
rate = 0.01
jump = 3


RED = (255, 0, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (180, 0, 255, 0)
WHITE = (255,255,255, 0)

p1 = list(range(0, 8))
p2 = list(range(8, 16))
p3 = list(range(16, 24))

cycle = [RED, PURPLE, BLUE, GREEN]

def fill_p(p, color):
	for id in p:
		pixels[id] = color
		time.sleep(0.05)
		pixels.show()

def check_distance(px1, px2):
    dist = [0, 0, 0, 0]
    dist_mag = dist
    for i in [0, 1, 2, 3]:
        dist[i] = px1[i] - px2[i]
        dist_mag[i] = abs(dist[i])
    #dist = tuple(map(lambda i, j: i - j, px1, px2))
    #dist_mag = tuple(map(lambda i, j: abs(i - j), px1, px2)) 
    return tuple(dist), tuple(dist_mag) 
    
def get_max(dist_mag):
    max_dist = max(dist_mag)
    idx = dist_mag.index(max_dist)
    return max_dist, idx

def change_color(pixels, goals):

#    px_color = list(pixels[pIDX])
#    dist, dist_mag = check_distance(px_color, goal)
#    max_dist, idx = get_max(dist)
    #while sum(list(dist_mag)) != 0:
    for i in range(0, 10000):
        for j in range(num_pixels):
            px_color = list(pixels[j])
            dist, dist_mag = check_distance(px_color, goals[j])
            max_dist, idx = get_max(dist)
    	    if dist[idx] > 0:
    	        px_color[idx] = px_color[idx] - random.randint(1, jump)
    	    else:
    	        px_color[idx] = px_color[idx] + random.randint(1, jump)
            pixels[j] = tuple(px_color)
            time.sleep(rate) 
        pixels.show()
        
        #dist, dist_mag = check_distance(px_color, goal)
        #max_dist, idx = get_max(dist)
    #pixels[pIDX] = RED
    return 0

def rand_state(pixels):
    for i in range(num_pixels):
    	pixels[i] = (random.randint(0,1),random.randint(0,255),random.randint(0,1),random.randint(0,0))
    pixels.show()
    return pixels

def get_neighbors(idx):
    if idx == 0:
    	n1 = num_pixels-1
    else:
    	n1 = idx-1
    if idx == num_pixels-1:
    	n2 = 0
    else:
	n2 = idx+1
    return n1, n2
   
def find_midpoint(px1, px2):

    color = [0, 0, 0, 0]
    for i in [0, 1, 2, 3]:
    	midpoint = round((px1[i]+px2[i])/2)
	color[i]=midpoint
    return tuple(color)   


pixels = rand_state(pixels)
time.sleep(0.1)

while True:
    #i = random.randint(0, 23)
    #for i in list(range(num_pixels)):
    #time.sleep(0.011)
    #i = 23#random.randint(0, num_pixels)
    px_set = []
    goals = []
    #dists = []   
    #dist_mags = []
    for j in range(num_pixels):
    	n1, n2 = get_neighbors(j)
    	px1 = pixels[n1]
    	px2 = pixels[n2]
    	#px_set.append((px1, px2))
    	goal = find_midpoint(px1, px2)
    	dist, dist_mag = check_distance(px1, px2)
        if sum(dist_mag) < LB:
            goal = (random.randint(0,1),random.randint(0,255),random.randint(0,1),random.randint(0,1))    	
        goals.append(goal)
        
        #dists.append(dist)
        #dist_mags.append(dist_mag)
    	

    change_color(pixels, goals)
        #time.sleep(0.5)
        #pixels.show()	
        

    

