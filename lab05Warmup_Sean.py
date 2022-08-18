from PIL import Image

bear = Image.open( "bear.png" )

pixel = bear.getpixel( ( 100, 200) )

print(pixel)

for i in range(100):

    bear.putpixel( (i, 200) , (0, 0, 0) )

pixel = bear.getpixel( ( 100, 200) )

print(pixel)


    
def invert( im ):
    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range( width ):

        for y in range( height ):

            (red, green, blue) = im.getpixel((x, y))

            im.putpixel( (x, y) , (255-red, 255-green, 255-blue) )
#invert(bear)

#bear.save("tmp_Sean_1.png")

def invert_block( im ):
    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range(300,width):

        for y in range(0,400):

            (red, green, blue) = im.getpixel((x, y))

            im.putpixel( (x, y) , (255-red, 255-green, 255-blue) )


invert_block(bear)

bear.save("tmp_Sean_2.png")




