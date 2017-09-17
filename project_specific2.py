import time # Checks for the runtime of code
from PIL import Image # Main library for use with image manipulation 
start = time.time() # On your setti, get ready, spaghetti!

im1 = Image.open("1.png").load() # simulateously opens the image and loads the RGB for later reference
im2 = Image.open("2.png").load() # simulateously opens the image and loads the RGB for later reference
im3 = Image.open("3.png").load() # simulateously opens the image and loads the RGB for later reference
im4 = Image.open("4.png").load() # simulateously opens the image and loads the RGB for later reference
im5 = Image.open("5.png").load() # simulateously opens the image and loads the RGB for later reference
im6 = Image.open("6.png").load() # simulateously opens the image and loads the RGB for later reference
im7 = Image.open("7.png").load() # simulateously opens the image and loads the RGB for later reference
im8 = Image.open("8.png").load() # simulateously opens the image and loads the RGB for later reference
im9 = Image.open("9.png").load() # simulateously opens the image and loads the RGB for later reference

width, height = Image.open("1.png").size # sets the width and height of our base image to a variable for easier reference

final_list = [] # empty list to store the median RGB tuples from each pixel coordinate

redlist = [] # empty list to store RGB values from all 9 images for this pixel coordinate
greenlist = [] # at the top of loop so each iteration starts with an empty list
bluelist = [] # will be used to find the median RGB value

# Loops through height of image
for y in range(height):
    
    # Loops through width of image
    for x in range(width):
        red1, green1, blue1 = im1[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red1) # append the R value to the red value list
        greenlist.append(green1) # appends the G value to the green value list
        bluelist.append(blue1) # appends the B value to the blue value list
        
        red2, green2, blue2 = im2[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red2) # append the R value to the red value list
        greenlist.append(green2) # appends the G value to the green value list
        bluelist.append(blue2) # appends the B value to the blue value list
        
        red3, green3, blue3 = im3[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red3) # append the R value to the red value list
        greenlist.append(green3) # appends the G value to the green value list
        bluelist.append(blue3) # appends the B value to the blue value list
        
        red4, green4, blue4 = im4[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red4) # append the R value to the red value list
        greenlist.append(green4) # appends the G value to the green value list
        bluelist.append(blue4) # appends the B value to the blue value list
        
        red5, green5, blue5 = im5[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red5) # append the R value to the red value list
        greenlist.append(green5) # appends the G value to the green value list
        bluelist.append(blue5) # appends the B value to the blue value list
        
        red6, green6, blue6 = im6[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red6) # append the R value to the red value list
        greenlist.append(green6) # appends the G value to the green value list
        bluelist.append(blue6) # appends the B value to the blue value list
        
        red7, green7, blue7 = im7[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red7) # append the R value to the red value list
        greenlist.append(green7) # appends the G value to the green value list
        bluelist.append(blue7) # appends the B value to the blue value list
        
        red8, green8, blue8 = im8[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red8) # append the R value to the red value list
        greenlist.append(green8) # appends the G value to the green value list
        bluelist.append(blue8) # appends the B value to the blue value list
        
        red9, green9, blue9 = im9[x,y] # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
        redlist.append(red9) # append the R value to the red value list
        greenlist.append(green9) # appends the G value to the green value list
        bluelist.append(blue9) # appends the B value to the blue value list
            
        redlist.sort() # sorts the values in the list
        greenlist.sort() # can now reference the median using list[len(list)/2] format
        bluelist.sort() # Sort the values to find the median
        final_list.append((redlist[4], greenlist[4], bluelist[4]))
    
        del redlist[:] # clear the lists so it can be used again
        del greenlist[:] # keeps the code fresh and running
        del bluelist[:] # crucial otherwise you could be sorting thousands of values


result_image = Image.new("RGB", (width, height)) # creates a new image with the same properties as our base image

result_image.putdata(final_list) # places our final_list of tuples into the pixel slots of the result_image
result_image.save("final.png") # saves the changes made and places it over "final.png"

end = time.time() # And tiiimmee's up!!
print "Literroni pepperoni, this code ran in " + str((end-start)) + " secerronis!" # #aesthetics
