import glob
import cv2
# import shutil

#画像二値化と保存
def main(extract_path):
    def white(img):
        img = cv2.imread(img, 0)
        ret, img_thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
        return img_thresh
    
    extract = glob.glob(fr"{extract_path}\*")
    imgs = list(white(i) for i in extract)
    return imgs
