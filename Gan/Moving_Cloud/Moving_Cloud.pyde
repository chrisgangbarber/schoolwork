x = 0
 
def setup():
    size(640,480)

def draw():
    global x
    print (x)
    if x >= 640:
        x = 0
    x += 10
    background(135, 206, 235) # sky blue
    #clouds
    fill(255)
    ellipse (x, height/6 + 10, 50, 50)
    ellipse (x, height/6 - 12, 50, 50)
    ellipse (x - 33, height/6, 50, 50)
    ellipse (x+40, height/6 + 15, 50, 50)
    ellipse (x+81, height/6 + 15, 50, 50)
    ellipse (x+38, height/6 - 15, 50, 50)
    ellipse (x+80, height/6 - 15, 50, 50)
    ellipse (x+120, height/6 + 8, 50, 50)
    ellipse (x+120, height/6 - 10, 50, 50)
    ellipse (x+150, height/6, 50, 50)
    noStroke()
    
    # ground
    fill(0, 128, 0)
    rect(0, height - 50, width, 50)
    
