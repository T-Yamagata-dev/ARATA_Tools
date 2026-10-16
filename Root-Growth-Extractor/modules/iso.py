import cv2
import numpy as np
# import glob
# import shutil

def padding(img1, img2,  pxcel_v, pxcel_h):
    img1_pad = cv2.copyMakeBorder(img1, pxcel_v, pxcel_v, pxcel_h, pxcel_h, cv2.BORDER_CONSTANT, 0).astype(np.float32) #np.uint8
    img2_pad = cv2.copyMakeBorder(img2, pxcel_v, pxcel_v, pxcel_h, pxcel_h, cv2.BORDER_CONSTANT, 0).astype(np.float32) #np.uint8
    return img1_pad, img2_pad

def iso(img_pad1, img_pad2):
    (x, y), r = cv2.phaseCorrelate(img_pad2, img_pad1)
    img_h = np.roll(img_pad2, int(x), axis=1)  #横回転、正で右向き
    img_v = np.roll(img_h, int(y), axis=0) #縦回転、正で下向き
    return img_v

def crip(iso_img, pxcel_v, pxcel_h):
    size = iso_img.shape
    crip_img = iso_img[pxcel_v:size[0]-pxcel_v, pxcel_h:size[1]-pxcel_h]
    return crip_img

def main(img1, img2, pxcel_v, pxcel_h):
    img1_pad, img2_pad = padding(img1, img2, pxcel_v, pxcel_h)
    iso_img = iso(img2_pad, img1_pad)
    crip_img = crip(iso_img, pxcel_v, pxcel_h).astype(np.uint8) #astypeの編集あり
    return crip_img
