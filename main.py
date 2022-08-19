

#INDIVIDUAL PORTION

#print("Running lab05Warmup_Sean.py")
#import lab05Warmup_Sean
#print("Running lab05Warmup_Benjamin.py")
#import lab05Warmup_Benjamin

#PAIR PORTION

from PIL import Image

bear = Image.open( "bear.png" )

def grayscale( im ):
    (width, height) = im.size
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            a = int((red*0.21+green*0.72+blue*0.07))
            im.putpixel( (x, y) , (a, a, a) )

#grayscale(bear)
#bear.save("tmp_grayscale.png")

def binarize(im, thresh, startx, starty, endx, endy):
    (width, height) = im.size
    for x in range( startx, endx ):
        for y in range( starty, endy ):
            (red, green, blue) = im.getpixel((x, y))
            if thresh > 255 | thresh < 0:
                print("ERROR")
                return
            elif (red+green+blue)//3 >= thresh:
                im.putpixel( (x, y) , (255, 255, 255) )
            elif (red+green+blue)//3 < thresh:
                im.putpixel( (x, y) , (0, 0, 0) )

#binarize(bear, 100, 0, 0, 600, 800)
#bear.save("tmp_binarize.png")

def mirrorVert( im ):
    (width, height) = im.size
    for x in range( width ):
        for y in range( height//2 ):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel( (x-width+1, height-y-1) , (red, green, blue) )

#mirrorVert(bear)
#ear.save("tmp_mirrorVert.png")

def mirrorHoriz( im ):
    (width, height) = im.size
    for x in range( width//2 ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel( (width-x-1, y-height+1) , (red, green, blue) )

#mirrorHoriz(bear)
#bear.save("tmp_mirrorHoriz.png")

def flipVert( im ):
   (width, height) = im.size
   for x in range( width ):
       for y in range( height//2 ):
           (red, green, blue) = im.getpixel((x, y))
           (red1, green1, blue1) = im.getpixel((x, 800-y-1))
           im.putpixel( (x, 800-y-1), (red, green, blue))
           im.putpixel( (x, y), (red1, green1, blue1))

#flipVert(bear)
#bear.save("tmp_flipVert.png")   


def scale( im ):
    (width, height) = im.size
    im = Image.new('255,0,0', (width//2,height//2))
    return(Image.new)


scale(bear)
    


