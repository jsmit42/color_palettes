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
    image = np.zeros((400, 600, 3), dtype=np.uint8)
    image[:,:] = [255, 0, 0]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mono = image
    analagous = image
    compliment = image
    tri = image
    tet = image
    split = image
    hue = 120 #blue
    row, col, _ = image.shape

    # generate monochrome
    mono[:, :int(col / 3)] = [hue, 255, 255]
    mono[:, int(col / 3):int(2 * col / 3)] = [hue, 255, 170]
    mono[:, int(-1 * col / 3):] = [hue, 255, 85]
    mono = cv2.cvtColor(mono, cv2.COLOR_HSV2BGR)
    cv2.imshow('monochrome', mono)
    cv2.waitKey(0)
    cv2.imwrite('monochrome.png', mono)

    # generate analagous
    hue2, hue3 = find_analagous(hue)
    analagous[:int(row / 3), :int(col / 3)] = [hue2, 255, 255]
    analagous[int(row / 3):int(-1 * row / 3), :int(col / 3)] = [hue2, 255, 170]
    analagous[int(-1 * row / 3):, :int(col / 3)] = [hue2, 255, 85]

    analagous[:int(row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 255]
    analagous[int(row / 3):int(2 * row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 170]
    analagous[int(-1 * row / 3):, int(col / 3):int(2 * col / 3)] = [hue, 255, 85]

    analagous[:int(row / 3), int(-1 * col / 3):] = [hue3, 255, 255]
    analagous[int(row / 3):int(2 * row / 3), int(-1 * col / 3):] = [hue3, 255, 170]
    analagous[int(-1 * row / 3):, int(-1 * col / 3):] = [hue3, 255, 85]

    analagous = cv2.cvtColor(analagous, cv2.COLOR_HSV2BGR)
    cv2.imshow('analagous', analagous)
    cv2.waitKey(0)
    cv2.imwrite('analagous.png', analagous)

    # generate split compliment
    hue2, hue3 = find_split_compliments(hue)
    split[:int(row / 3), :int(col / 3)] = [hue2, 255, 255]
    split[int(row / 3):int(-1 * row / 3), :int(col / 3)] = [hue2, 255, 170]
    split[int(-1 * row / 3):, :int(col / 3)] = [hue2, 255, 85]

    split[:int(row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 255]
    split[int(row / 3):int(2 * row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 170]
    split[int(-1 * row / 3):, int(col / 3):int(2 * col / 3)] = [hue, 255, 85]

    split[:int(row / 3), int(-1 * col / 3):] = [hue3, 255, 255]
    split[int(row / 3):int(2 * row / 3), int(-1 * col / 3):] = [hue3, 255, 170]
    split[int(-1 * row / 3):, int(-1 * col / 3):] = [hue3, 255, 85]

    split = cv2.cvtColor(split, cv2.COLOR_HSV2BGR)
    cv2.imshow('split', split)
    cv2.waitKey(0)
    cv2.imwrite('split.png', split)

    # generate triadic
    hue2, hue3 = find_triadic(hue)
    tri[:int(row / 3), :int(col / 3)] = [hue2, 255, 255]
    tri[int(row / 3):int(-1 * row / 3), :int(col / 3)] = [hue2, 255, 170]
    tri[int(-1 * row / 3):, :int(col / 3)] = [hue2, 255, 85]

    tri[:int(row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 255]
    tri[int(row / 3):int(2 * row / 3), int(col / 3):int(2 * col / 3)] = [hue, 255, 170]
    tri[int(-1 * row / 3):, int(col / 3):int(2 * col / 3)] = [hue, 255, 85]

    tri[:int(row / 3), int(-1 * col / 3):] = [hue3, 255, 255]
    tri[int(row / 3):int(2 * row / 3), int(-1 * col / 3):] = [hue3, 255, 170]
    tri[int(-1 * row / 3):, int(-1 * col / 3):] = [hue3, 255, 85]

    tri = cv2.cvtColor(tri, cv2.COLOR_HSV2BGR)
    cv2.imshow('tri', tri)
    cv2.waitKey(0)
    cv2.imwrite('triadic.png', tri)

    # generate compliment
    hue2 = find_compliment(hue)
    compliment[:int(row / 3), :int(col / 3)] = [hue2, 255, 255]
    compliment[int(row / 3):int(-1 * row / 3), :int(col / 3)] = [hue2, 255, 170]
    compliment[int(-1 * row / 3):, :int(col / 3)] = [hue2, 255, 85]

    compliment[:int(row / 3), int(col / 3):] = [hue, 255, 255]
    compliment[int(row / 3):int(2 * row / 3), int(col / 3):] = [hue, 255, 170]
    compliment[int(-1 * row / 3):, int(col / 3):] = [hue, 255, 85]

    compliment = cv2.cvtColor(compliment, cv2.COLOR_HSV2BGR)
    cv2.imshow('compliment', compliment)
    cv2.waitKey(0)
    cv2.imwrite('compliment.png', compliment)

    # generate tetradic
    hue2, hue3, hue4 = find_tetradic(hue)

    tet[:int(row / 3), :int(col / 4)] = [hue, 255, 255]
    tet[int(row / 3):int(row / -3), :int(col / 4)] = [hue, 255, 170]
    tet[int(row / -3):, :int(col / 4)] = [hue, 255, 85]

    tet[:int(row / 3), int(col / 4):int(col / 2)] = [hue2, 255, 255]
    tet[int(row / 3):int(row / -3), int(col / 4):int(col / 2)] = [hue2, 255, 170]
    tet[int(row / -3):, int(col / 4):int(col / 2)] = [hue2, 255, 85]

    tet[:int(row / 3), int(col / 2):int(row / -4)] = [hue3, 255, 255]
    tet[int(row / 3):int(row / -3), int(col / 2):int(row / -4)] = [hue3, 255, 170]
    tet[int(row / -3):, int(col / 2):int(row / -4)] = [hue3, 255, 85]

    tet[:int(row / 3), int(col / -4):] = [hue4, 255, 255]
    tet[int(row / 3):int(row / -3), int(col / -4):] = [hue4, 255, 170]
    tet[int(row / -3):, int(col / -4):] = [hue4, 255, 85]

    tet = cv2.cvtColor(tet, cv2.COLOR_HSV2BGR)
    cv2.imshow('tet', tet)
    cv2.waitKey(0)
    cv2.imwrite('tetradic.png', tet)

main()
