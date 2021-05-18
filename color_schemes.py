import numpy as np
import cv2
import random

def random_hue():
    return random.randrange(0,180)

def random_sv(hue):
    return [hue, random.randrange(0,255), random.randrange(0, 255)]

def find_split_compliments(hue):
    con1 = (hue + 90) % 180 - 15
    con2 = (hue + 90) % 180 + 15
    return con1, con2

def find_compliment(hue):
    return (hue + 90) % 180

def find_triadic(hue):
    return (hue + 60) % 180, (hue + 120) % 180

def find_tetradic(hue):
    return (hue + 45) % 180, (hue + 90) % 180, (hue + 135) % 180

def find_analagous(hue):
    return (hue + 15) % 180, (hue - 15) % 180

def main():
    image = np.zeros((300, 1050, 3), dtype=np.uint8)
    image[:,:] = [255, 0, 0]

    hue1 = random_hue()
    hue2, hue3 = find_split_compliments(hue1)
    hue4, hue5 = find_analagous(hue2)
    hue6, _    = find_analagous(hue1)

    image[:, :150] = random_sv(hue1)
    image[:, 150:300] = random_sv(hue2)
    image[:, 300:450] = random_sv(hue3)
    image[:, 450:600] = random_sv(hue4)
    image[:, 600:750] = random_sv(hue5)
    image[:, 750:900] = random_sv(hue6)
    image[:, 900:] = random_sv(hue3)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('test',cv2.cvtColor(image, cv2.COLOR_HSV2BGR))
    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.waitKey(0)
    cv2.imwrite('random_palette.png', image)


main()
