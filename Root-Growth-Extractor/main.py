#POC同士の位置合わせを行いながら補正を行う（前　→　後　でbUnwarpJをしている　（元のauto4から変更）
#パディング、切り抜きを縦横でサイズを調整できるようにする予定
from modules import bUnwarpJ, growth_death, image_prepare, iso, line_noize, mkdirs
import glob
import cv2
import os

def save(imgs, path, names):
    for i,j in zip(imgs, names):
        cv2.imwrite(fr"{path}\{j}", i)

def main():
    exracted_imgs_path = fr"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/extract"
    Fiji_path = fr"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/Fiji.app/ImageJ-win64.exe"
    macro_path = fr"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/bunwarpj_macro.ijm"
    pxcel_v = 200
    pxcel_h = 100
    #Javaヒープメモリを8GBに設定(実行環境によっては不要)
    os.environ["JAVA_TOOL_OPTIONS"] = "-Xmx8g" 
    names = list(i.split("\\")[-1] for i in glob.glob(fr"{exracted_imgs_path}\*"))
    mkdirs.main(rf"C:\Users\takuf\Documents\ARATA_tools\Root-Growth-Extractor")
    #抽出画像を二値化
    imgs = image_prepare.main(fr"extract")
    #パディング
    save(imgs, fr"output\total", names)
    # temp_path = fr"tmp\tmp.png"
    path = glob.glob(fr"output\total\*")
    #imgsを適宜最新のtotalから画像をとるようにする（ノイズの除去を反映させる）
    for i in range(len(path)-1):
        img_pre = cv2.imread(path[i], 0)
        img_next = cv2.imread(path[i+1], 0)
        # POC_img = iso.main(imgs[i], imgs[i+1], pxcel_v, pxcel_h)
        POC_img = iso.main(img_pre, img_next, pxcel_v, pxcel_h)
        cv2.imwrite(fr"tmp\POC.png", POC_img)
        # bUn_img = bUnwarpJ.bUnwarpJ(path[i+1], Fiji_path, macro_path)
        bUn_img = bUnwarpJ.bUnwarpJ(path[i+1], Fiji_path, macro_path)
        growth_img, death_img = growth_death.growth_death(bUn_img, img_next)
        # bUn_img = bUnwarpJ_old.bUnwarpJ(Fiji_path, fr"tmp\POC.png", path[i+1], temp_path)
        # growth_img, death_img = growth_death.growth_death(bUn_img, imgs[i+1])
        total, growth, death =  line_noize.main(bUn_img, img_next, growth_img, death_img, 2)
        cv2.imwrite(fr"output\total\{names[i+1]}",  total)
        cv2.imwrite(fr"output\growth\{names[i+1]}", growth)
        cv2.imwrite(fr"output\death\{names[i+1]}",  death)

if __name__ == "__main__":
    main()
