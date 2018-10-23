xplace = 0
xplace2 = 0

def setup():
    size (640, 480)

def draw():
    background (135, 206, 235)
    noStroke ()
    
    #sun
    fill (255, 255, 0)
    ellipse(0, 0, 200, 200)
    
    #ground
    fill (0, 128, 0)
    rect(0, height - 50, width, 50)
    
    #mountain 1
    fill (200)
    triangle(640, 430, 480, 300, 320, 430)
    fill (255)
    triangle(516, 330, 480, 300, 444, 330)
    
    #mountain 2
    fill (150)
    triangle(560, 430, 400, 300, 240, 430)
    fill (255)
    triangle(436, 330, 400, 300, 364, 330)
    
    #mountain 3
    fill (200)
    triangle(740, 430, 580, 300, 420, 430)
    fill (255)
    triangle(616, 330, 580, 300, 544, 330)
    #tree
    
    #houses
    fill(203, 65, 84)
    for x in range(20, 180, 30):
        rect(x, height - 75, 25, 25)
    fill(0, 0, 200)
    for x in range(20, 180, 30):
        rect(x + 5, height - 70, 7, 7)
        rect(x + 15, height - 70, 7, 7)
    fill(222,184,135)
    for x in range(20, 180, 30):
        triangle (x-5, 405, x+12.5, 385, x+30, 405)
        rect(x + 10, height - 60, 7, 10)
    
    #clouds
    global xplace
    if xplace >= 640:
        xplace = 0
    xplace += 3
    fill(255)
    ellipse(xplace, height/4, 70, 70)
    ellipse(xplace+50, height/4, 70, 70)
    ellipse(xplace+20 , height/4-20, 70, 70)
    global xplace2

    if xplace2 >= 640:
        xplace2 = 0
    xplace2 += 1
    ellipse(xplace2-250, height/4, 70, 70)
    ellipse(xplace2-200, height/4, 70, 70)
    ellipse(xplace2-220 , height/4-20, 70, 70)
    
    

    
