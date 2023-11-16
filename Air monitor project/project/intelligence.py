# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import skimage as io
import numpy as np
def find_red_pixels(*args,**kwargs):
  
    # Your code goes here
    image=io.imread(r'data\map.png')
    image1=image.copy()
    Red=[]
    for i in image1:
        pixels=[]
        for pixel in i:
            if pixel[0]>=110 and pixel[1]<=40 and pixel[2]<=20:
                pixels.append([255,255,255])
            else:
                pixels.append([0,0,0])
        Red.append(pixels)
    Red=np.array(Red)
    io.imsave("map-red-pixels.jpg",Red)
    return Red
#test#find_red_pixels()
def find_cyan_pixels():
    
    # Your code goes here
    image=io.imread(r'data\map.png')
    image2=image.copy()
    Cyan=[]
    for i in image2:
        pixels=[]
        for pixel in i:
            if pixel[0]<=40 and pixel[1]>=30 and pixel[2]>=50:
                pixels.append([255,255,255])
            else:
                pixels.append([0,0,0])
        Cyan.append(pixels)
    Cyan=np.array(Cyan)
    io.imsave("map-cyan-pixels.jpg",Cyan)
    return Cyan
#test#find_cyan_pixels()


def detect_connected_components(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

def detect_connected_components_sorted(*args,**kwargs):
    """Your documentation goes here"""
    # Your code goes here

