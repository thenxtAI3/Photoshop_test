import glob
from PIL import Image # Main library for use with image manipulation 
import time # Checks for the runtime of code
start = time.time() # On your setti, get ready, spaghetti!
pictures, final_list = map(Image.open, glob.glob("../Project/Photos/*.png")), []
for y in range(pictures[0].size[1]): # Loops through height of image
    redlist, greenlist, bluelist = [],[],[]
    for x in range(pictures[0].size[0]): # Loops through width of image
        for image in pictures:
            red, green, blue = image.getpixel((x,y)) # image[x,y] pulls the RGB value for that pixel and returns it as a tuple (R, G, B)
            redlist.append(red), greenlist.append(green), bluelist.append(blue)
    final_list.append((sorted(redlist)[len(redlist)/2], sorted(greenlist)[len(greenlist)/2], sorted(bluelist)[len(bluelist)/2]))
result = Image.new("RGB", (pictures[0].size[0], pictures[0].size[1]))
result.putdata(final_list)
result.save("final.png")
end = time.time() # And tiiimmee's up!!
print(end-start)