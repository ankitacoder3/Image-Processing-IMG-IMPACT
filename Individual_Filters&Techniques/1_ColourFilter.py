from PIL import Image

img = Image.open(r"Images/1_2_rover.jpg").convert("RGB")

width,height = img.size

pixels = img.load()

def red(r,g,b):
    newr = r
    newg = 0
    newb = 0
    return(newr,newg,newb)

def darkpink(r,g,b):
    newr = g
    newg = b
    newb = r
    return(newr,newg,newb)

def skyblue(r,g,b):
    newr = b
    newg = g
    newb = r
    return(newr,newg,newb)

def lemongreen(r,g,b):
    newr = g
    newg = r
    newb = b
    return(newr,newg,newb)

def grey(r,g,b):
    newr = (r+g+b)//3
    newg = (r+g+b)//3
    newb = (r+g+b)//3
    return(newr,newg,newb)

def sepia(r,g,b):
    newr = int((r*.393) + (g*.769) + (b*.189))
    newg = int((r*.349) + (g*.686) + (b*.168))
    newb = int((r*.272) + (g*.534) + (b*.131))
    return(newr,newg,newb)

choice = '''
enter your choice
1 red
2 darkpink
3 skyblue
4 lemonyellow
5 grey
6 sepia
'''


print(choice)
no = int(input())


for py in range(height):
    for px in range(width):
        r,g,b = img.getpixel((px,py))
        if no==1:
            pixels[px,py] = red(r,g,b)
        if no==2:
            pixels[px,py] = darkpink(r,g,b)
        if no==3:
            pixels[px,py] = skyblue(r,g,b)
        if no==4:
            pixels[px,py] = lemongreen(r,g,b)
        if no==5:
            pixels[px,py] = grey(r,g,b)
        if no==6:
            pixels[px,py] = sepia(r,g,b)

img.show()
img.save(r"Images/1_new_filtering.jpg")













