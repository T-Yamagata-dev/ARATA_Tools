# import cv2

def growth_death(mae_img, ato_img):    #成長・枯死根画像の作成
    growth = ato_img - mae_img
    death  = mae_img - ato_img
    return growth, death
