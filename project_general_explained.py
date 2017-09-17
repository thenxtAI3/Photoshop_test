import time # Checks for the runtime of code
from PIL import Image # Main library for use with image manipulation 
import glob # Library to pull images from a directory

start = time.time() # Start timer

pictures, final_list = map(Image.open, glob.glob("../Project/Photos/*.png")), [] # creates a list of available.png files in the given folder | creates an empty final_list to hold median tuples

width, height = pictures[0].size # sets the ratio of the image for reference in for loop

for y in range(height): # Loops through height of image
    
    #RGB color list for finding the median
    redlist = [] # empty list for each color
    greenlist = [] # outside second loop to keep empty property after loop
    bluelist = [] # allows values to be sorted
    
    for x in range(width):     # Loops through width of image
        for image in pictures:
           
            red1, green1, blue1 = image.getpixel((x,y)) # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
            redlist.append(red1) # append the R value to the red value list
            greenlist.append(green1) # appends the G value to the green value list
            bluelist.append(blue1) # appends the B value to the blue value list
   
    median = ((sorted(redlist)[len(redlist)/2]), (sorted(greenlist)[len(greenlist)/2]), (sorted(bluelist)[len(bluelist)/2])) #sorts each list and finds the median value simultaniously
    final_list.append(median) # appends median tuple into final_list

final = Image.new("RGB", (width, height), "white") # Creates a blank image where you place the median RGB values for each pixel
final.putdata(final_list) # puts the final list data into the new image
final.save("final.png") # saves the image

end = time.time() # ends timer

print "It took " + str(end-start) + " to edit the image." # Prints run time
