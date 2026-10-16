#ローカルのpython環境からのImageJプラグインbUnwarpJの実行（jdk8のインストール、パス設定が必要かも）
# import imagej
import cv2
import numpy as np
# import psutil
import subprocess

def bUnwarpJ(Fiji_path, img1, img2, temp_path):
    # ij = imagej.init(Fiji_path, mode='legacy')

    # # 画像ファイルを開く
    # """image1 = ImagePlus("Image from NumPy", img1)
    # image2 = ImagePlus("Image from NumPy", img2)"""
    # image1 = ij.io().open(img1)
    # image2 = ij.io().open(img2)

    # # 画像をセット
    # ij.ui().show(image2)
    # ij.ui().show(image1)

    # # プラグインの実行パラメータ
    # params = "registration=Mono image_subsample_factor=0 initial_deformation=[Very Coarse] final_deformation=Fine divergence_weight=0 curl_weight=0 landmark_weight=0 image_weight=1 consistency_weight=10 stop_threshold=0.01"

    # # `IJ.run` を使用して、ImageJのコマンドとしてbUnwarpJを実行
    # ij.IJ.run("bUnwarpJ", params)
    # ij.IJ.saveAs("Registered Source Image.png", temp_path)

    # # ImageJを終了
    # ij.dispose()
    print("temp_path:"+temp_path)

    

    Fiji = r"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/Fiji.app/ImageJ-win64.exe"
    macro = r"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/bunwarpj_macro.ijm"

    result = subprocess.run([Fiji, "-macro", macro])

    img = binary(temp_path)
    return img

    #必要であれば、ガーベジコレクションを呼び出してメモリ解放を行う
    #import gc
    #gc.collect()

def binary(regist_temp_path):
    img = cv2.imread(regist_temp_path, 0).astype(np.uint8)
    img = np.where(img > 127, 255, 0)
    return img

def main(Fiji_path, imgs, temp_path):
    imgs = list(bUnwarpJ(Fiji_path, imgs[i], imgs[i+1], temp_path) for i in range(len(imgs)-1))
    return imgs





# import subprocess
# import os
# import platform

# base = os.path.dirname(os.path.abspath(__file__))
# os_name = platform.system()

# if os_name == "Windows":
#     java = os.path.join(base, "jre_win", "bin", "java.exe")
# elif os_name == "Darwin":
#     java = os.path.join(base, "jre_mac", "Contents", "Home", "bin", "java")
# elif os_name == "Linux":
#     java = os.path.join(base, "jre_linux", "bin", "java")

# fiji = os.path.join(base, "fiji_portable", "ImageJ-launcher.jar")
# macro = os.path.join(base, "fiji_portable", "macros", "bunwarpj_macro.ijm")

# subprocess.run([java, "-jar", fiji, "-macro", macro])
