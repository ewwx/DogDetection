from PIL import Image
import os

L = os.listdir("rawdata")
index = 0
for i in L:
    print("/home/efka/Sign recognition/opencv-haar-classifier-training-master/positive_dogs/rawdata"+i)
    img = Image.open("/home/efka/Sign recognition/opencv-haar-classifier-training-master/positive_dogs/rawdata/"+i)
    file_out = "dog" + str(index) + ".bmp"
    img.save(file_out)
    os.remove("/home/efka/Sign recognition/opencv-haar-classifier-training-master/positive_dogs/rawdata/"+i)
    index += 1

