import cv2
import os
import sys
import time
from PIL import Image
from playsound import playsound
from pygame import mixer


ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def getVideo(path):
    getvideo = cv2.VideoCapture(path)
    
    while(True):
        ret,frame = getvideo.read()
        if ret:
            convertImage(Image.fromarray(frame))
        else:
            break
    getvideo.release()
    cv2.destroyAllWindows()


def resize_image(image, new_width=100):
    (input_width, input_height) = image.size
    ratio = input_height/float(input_width)
    changed_height = int(ratio*new_width)
    changed_image = image.resize((new_width,changed_height))
    return changed_image

def makeGrey(image):
    return image.convert('L')

def pixelToAscii(image):
    pixel_in_image = list(image.getdata())
    pixel_to_chars = [ASCII_CHARS[pixel_value//25] for pixel_value in pixel_in_image]
    return "".join(pixel_to_chars)

def image_to_ascii(image, new_width = 100):
    image = resize_image(image)
    image = makeGrey(image)
    pixelsToChars = pixelToAscii(image)
    lenPixelToChar = len(pixelsToChars)
    imageAscii = [pixelsToChars[index: index + new_width] for index in range(0, lenPixelToChar, new_width)]
    return "\n".join(imageAscii)


frames = []
def convertImage(img):
    imageAscii = image_to_ascii(img)
    frames.append(imageAscii)
    
        
def run(videoPath):
    getVideo(videoPath)
    #os.startfile(videoPath)
    #playsound(videoPath)
    mixer.init()
    mixer.music.load("E:\\nummathproject\\video\\Bongocat.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    
    for x in range (0,len(frames)):
        time.sleep(0.01)
        
        print(frames[x],'\r')
        #os.system('cls')
    mixer.music.stop()    

filenames = run("E:\\nummathproject\\video\\Bongocat.mp4")
