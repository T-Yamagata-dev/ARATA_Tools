#モルフォロジー変換を用いた成長・枯死根からの微小ノイズ除去
import numpy as np
import cv2

#拡大
def dilate(img, num):
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.dilate(img,kernel,iterations = num)
    return dst

#縮小
def erode(img, num):
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.erode(img.astype(np.uint8),kernel,iterations = num)
    return dst

#縮小＆拡大
def open(img, num):
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.morphologyEx(img.astype(np.uint8), cv2.MORPH_OPEN, kernel,iterations = num)
    return dst

#バケツ塗（difがある箇所のbaseの塊を塗る）
def fill(dif, base):
    points = (list(zip(*np.where(dif == 255))))
    h, w = dif.shape
    mask = np.zeros((h+2, w+2), np.uint8)
    for i in points:
        cv2.floodFill(base, mask, (i[1], i[0]), 122)
    output = np.where(base  == 122, 255, 0)
    return output

#前処理（成長根用）
def forgrowth(POC_img, growth, kernel):
    POC_ex = cv2.dilate(POC_img.astype(np.uint8), kernel, iterations = 1)
    img = growth - POC_ex
    return img

#前処理（枯死根用）
def fordeath(extract, death, kernel):
    extract_ex = cv2.dilate(extract.astype(np.uint8), kernel, iterations = 1)
    img = death - extract_ex
    return img

#ノイズ除去
def remove(img,num):
    dst = erode(img, num)
    dst = dilate(dst, num)
    dst = open(dst, num)
    return dst

def main(regist_img, POC_img, growth_img, death_img, num):
    #画像を引く 成長画像ー前全抽出の画像を大きくした画像(2)
    kernel = np.ones((2,2),np.uint8)
    growth = forgrowth(regist_img, growth_img, kernel)
    death  = fordeath(POC_img, death_img, kernel)
    
    #ノイズ除去
    growth_remove = remove(growth, num)
    death_remove  = remove(death, num)

    #塗りつぶし
    growth_fill = fill(growth_remove, growth)
    death_fill  = fill(death_remove, death)

    #画像保存
    return growth_fill, death_fill
