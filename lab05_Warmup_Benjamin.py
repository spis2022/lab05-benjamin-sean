from PIL import Image

bear = Image.open( "bear.png" )

def invert_block( im ):

    ''' Invert the colors in the input image, im '''

    

    # Find the dimensions of the image

    (width, height) = im.size



    # Loop over the entire image

    for x in range(300):

        for y in range( 400 ):

            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y) , (255-red, 255-green, 255-blue))

            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them


def invert( im ):

    ''' Invert the colors in the input image, im '''

    

    # Find the dimensions of the image

    (width, height) = im.size



    # Loop over the entire image

    for x in range(width):

        for y in range(height):

            (red, green, blue) = im.getpixel((x, y))
            im.putpixel((x,y) , (255-red, 255-green, 255-blue))

            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them
invert_block(bear)

bear.save("tmp_Ben_2.png")
