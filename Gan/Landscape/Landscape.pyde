def setup():
    size (640, 480)

def draw():
    background (135, 206, 235)
    noStroke ()
    fill (0, 128, 0)
    rect(0, height - 50, width, 50)
    fill (200)
    triangle(640, 430, 480, 300, 320, 430)
    fill (255)
    triangle(516, 330, 480, 300, 444, 330)
    
