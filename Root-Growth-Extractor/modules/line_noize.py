import cv2
import numpy as np
# from matplotlib import pyplot as plt
from modules import mini_noize

#縦線ノイズ検出
def line(img):
    size = img.shape
    base = np.zeros(size[0]*size[1]).reshape(size[0],size[1])
    line_v = size[0]-1
    Length = 1000
    lines = cv2.HoughLinesP(img.astype(np.uint8), rho=1, theta=np.pi/180, threshold=450, minLineLength=Length, maxLineGap=500)  
    print("linesの中身")
    if lines is not None:
        for line in lines:
            # print(line)
            #x座標が同じ線を検出
            x1, y1, x2, y2 = line
            print("line")
            print(x1,y1,x2,y2)

            # x1, y1, x2, y2 = line[0]

            # 白線を引く
            if x1 == x2:
                base = cv2.line(base, (x1,line_v), (x2,0), (255,255,255), 3) #base = cv2.line(base, (x1,y1), (x2,y2), (255,255,255), 3)
                
        return base
    else:
        return base
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#成長・枯死根画像の細かいノイズを除去
def Noize(regist_img, POC_img, growth_img, death_img, num):
    num = 2
    growth_fill, death = mini_noize.main(regist_img, POC_img, growth_img, death_img, num)
    return growth_fill, death

#成長・枯死根画像の縦線ノイズを検出
def LineNoize(growth_fill):
    growth_line = line(growth_fill)
    cv2.imwrite("line.png",growth_line)
    return growth_line

#縦線ノイズの除去
def Eraze(POC_img, growth_fill, growth_line):
    total = POC_img - growth_line
    growth = growth_fill - growth_line
    return total, growth

#メイン関数
def main(regist_img, POC_img, growth_img, death_img, num): 
    growth_fill, death = Noize(regist_img, POC_img, growth_img, death_img, num)
    growth_line = LineNoize(growth_fill)
    total, growth = Eraze(POC_img, growth_fill, growth_line)
    return total, growth, death
