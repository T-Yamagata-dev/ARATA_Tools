import os
import shutil
import glob
import cv2
from itertools import product

# 既存ファイルの削除、新規ファイルの作成
def make_file(filepath):
    if os.path.exists(filepath) == True:
        shutil.rmtree(filepath)
        os.mkdir(filepath)
    else:
        os.mkdir(filepath)

# 画像ファイルの選択
def image_select():
    image_file = input("Enter image file path: ").strip('"')
    if os.path.exists(image_file) == False:
        print(f"\nThe specified image file could not be found: {image_file}")
    return image_file

# 画像読み込み 
def image_read(image_file):
    img_path = list(i for i in glob.glob(f"{image_file}/*"))
    img_list = list(cv2.imread(i) for i in img_path)
    img_name_list = list(os.path.split(i)[1] for i in glob.glob(f"{image_file}/*"))

    return img_list, img_name_list

# 画像切り分け
def image_cut(img_list, img_name_list, img_type):
    #切り分けサイズの計算
    cut_width = 400
    cut_height = 400
    img_num = list({"horizontal":i.shape[0]//cut_width, "vartical":i.shape[1]//cut_height} for i in img_list)

    # 画像切り分け処理
    for img, num, name in zip(img_list, img_num, img_name_list):     
        for  v, h  in product(range(num["horizontal"]), range(num["vartical"])):
                #[x開始:x終了, y開始:y終了]
                cut_img = img[
                    cut_width*v: cut_width+cut_width*v, 
                    cut_height*h: cut_height+cut_height*h
                    ] 
                save_path = f"{img_type}/{name}{str(v)}-{str(h)}.png" 
                cv2.imwrite(save_path, cut_img)

# メイン実行
def make_train_iamge(img_type):
    make_file(f"{img_type}")
    img_file = image_select()
    img_list, img_name_list = image_read(img_file)
    image_cut(img_list, img_name_list, img_type)

if  __name__ == "__main__":
    img_type = "img"
    make_train_iamge(img_type)
