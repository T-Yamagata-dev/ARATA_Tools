import subprocess
import cv2
import shutil

# bUnwarpJによる画像の差分抽出
def bUnwarpJ(next_img, Fiji_path, macro_path):
    shutil.copy(next_img, fr"C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/next.png")
    Fiji = Fiji_path
    macro = macro_path
    subprocess.run([Fiji, "-macro", macro])
    bUnwarpJ_img = cv2.imread("C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/tmp.png", 0)
    ret, img_thresh = cv2.threshold(bUnwarpJ_img, 128, 255, cv2.THRESH_BINARY)
    # cv2.imwrite("C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/tmp.png", img_thresh)
    return img_thresh

#Fijiポータブル版とJREを同梱することによってOSにかかわらず使用できるようにすることができる
# import subprocess
# import os

# Fiji = r"C:/bunTest/Fiji.app/ImageJ-win64.exe"
# macro = r"C:/bunTest/bunwarpj_macro.ijm"

# # Windows の CREATE_NO_WINDOW フラグ
# CREATE_NO_WINDOW = 0x08000000

# result = subprocess.run(
#     [Fiji, "-macro", macro],
#     creationflags=CREATE_NO_WINDOW,
#     capture_output=True,
#     text=True
# )

# print("STDOUT:/n", result.stdout)
# print("STDERR:/n", result.stderr)
# print("RETURN CODE:", result.returncode)
# https://www.azul.com/products/core/
