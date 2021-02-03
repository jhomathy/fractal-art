from math import *
import numpy as np
import cv2
import random as lol_so_random

out_path = "/Users/tommy/Dropbox/music made by me/social media/github/fractal-art"

# 2 ** math.floor(math.log2(512))
sam512 = cv2.imread("sam512.png")

cut_in_half = lambda x : floor(x // 2)

def samify(sam, its_deep, its_max, prob=0.5):
    '''
    sam      : exactly the sam image from
                sam512 or "sam512.png"; no
                other images allowed!
    its_deep : how many iterations we've done
    its_max  : maximum number of iterations allowed
    '''

    # helper function
    def magic_eight(sam):
        to_split = lol_so_random.random() > prob
        if to_split:
            return(sam)
        else:
            the_new_sam = samify(sam, its_deep + 1, its_max)
            return(the_new_sam)
    # end helper function 

    if its_deep > its_max:
        return(sam)
    else:
        half_of_sam = halve(sam)

        ul = magic_eight(half_of_sam)
        bl = magic_eight(half_of_sam)
        ur = magic_eight(half_of_sam)
        br = magic_eight(half_of_sam)

        left = np.concatenate((ul, bl), axis=0)
        right = np.concatenate((ur, br), axis=0)

        return(np.concatenate((left, right), axis=1))


def halve(image_of_sam):
    length_of_sam = 2 ** floor(log2(len(image_of_sam)))
    if length_of_sam == 1:
        return(image_of_sam)
    else:
        return(cv2.resize(image_of_sam,
                          (length_of_sam // 2,
                           length_of_sam // 2)))

# the making and saving the images

sam256 = halve(sam512)
sam128 = halve(sam256)
sam64  = halve(sam128)
sam32  = halve(sam64)
sam16  = halve(sam32)
sam8   = halve(sam16)
sam4   = halve(sam8)
sam2   = halve(sam4)
sam1   = halve(sam2)

