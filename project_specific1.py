import time # Checks for the runtime of code
from PIL import Image # Main library for use with image manipulation 

# Start timer
start = time.time() 

# sets the ratio of the image for reference in for loop
width, height = Image.open("1.png").size

# Loads the image to acess RGB values per pixel
pix1 = Image.open("1.png").load()
pix2 = Image.open("1.png").load()
pix3 = Image.open("3.png").load()
pix4 = Image.open("4.png").load()
pix5 = Image.open("5.png").load()
pix6 = Image.open("6.png").load()
pix7 = Image.open("7.png").load()
pix8 = Image.open("8.png").load()
pix9 = Image.open("9.png").load()

#RGB color list for finding the median
redlist = []
greenlist = []
bluelist = []

# To hold final pixels
final_list = []

# Loops through height of image
for y in range(height):
    
    # Loops through width of image
    for x in range(width):
        red1, green1, blue1 = pix1[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red1) # append the R value to the red value list
        greenlist.append(green1) # appends the G value to the green value list
        bluelist.append(blue1) # appends the B value to the blue value list
        
        red2, green2, blue2 = pix2[x,y] #repeat for each image
        redlist.append(red2)
        greenlist.append(green2)
        bluelist.append(blue2)
        
        red3, green3, blue3 = pix3[x,y]
        redlist.append(red3)
        greenlist.append(green3)
        bluelist.append(blue3)
        
        red4, green4, blue4 = pix4[x,y]
        redlist.append(red4)
        greenlist.append(green4)
        bluelist.append(blue4)
        
        red5, green5, blue5 = pix5[x,y]
        redlist.append(red5)
        greenlist.append(green5)
        bluelist.append(blue5)
        
        red6, green6, blue6 = pix6[x,y]
        redlist.append(red6)
        greenlist.append(green6)
        bluelist.append(blue6)
        
        red7, green7, blue7 = pix7[x,y]
        redlist.append(red7)
        greenlist.append(green7)
        bluelist.append(blue7)
        
        red8, green8, blue8 = pix8[x,y]
        redlist.append(red8)
        greenlist.append(green8)
        bluelist.append(blue8)
        
        red9, green9, blue9 = pix9[x,y]
        redlist.append(red9)
        greenlist.append(green9)
        bluelist.append(blue9)
        
        redlist.sort() # Sort the values to find the median
        greenlist.sort()
        bluelist.sort()
        
        # the pixel that you will use for the final image = (medianR, medianG, medianB) --> (R,G,B)
        median_pixel = (redlist[4], greenlist[4], bluelist[4])
        
        final_list.append(median_pixel) # append this pixel to the final list
        del redlist[:] # clear the lists so it can be used again
        del greenlist[:]
        del bluelist[:]

# Creates a blank image where you place the median RGB values for each pixel
final = Image.new("RGB", (width, height), "white")

# puts the final list data into the new image
final.putdata(final_list)

# saves the image
final.save("final.png")

# Stop timer
end = time.time()

# Prints run time
print(end-start)
