import numpy as np
import cv2
import matplotlib
import pandas as pd
import glob

def area_ana(path):
    areas = []
    for i in path:
        img = cv2.imread(i, 0)
        area = int(np.sum(img)/255)
        areas.append(area)
    return areas


path = fr"ARATA_images"
path2 = glob.glob(fr"{path}\*")
for site in path2:
    path3 = glob.glob(fr"{site}\*")
    columns = ["Total", "Growth", "Death"]
    index = []

    total  = fr"{site}\POC"
    growth = fr"{site}\noize\growth"
    death  = fr"{site}\noize\death"
    total_path  = glob.glob(fr"{total}\*")
    growth_path = glob.glob(fr"{growth}\*")
    death_path  = glob.glob(fr"{death}\*")

    for j in total_path:
        ind_name = j[-17: -4]
        index.append(ind_name)
    total_areas  = area_ana(total_path)
    growth_areas = area_ana(growth_path)
    death_areas  = area_ana(death_path)
    data = np.array([total_areas,
                     growth_areas,
                     death_areas]).T
df = pd.DataFrame(data=data, index=index, columns=columns)
df.to_excel(fr"{site}\area.xlsx", index=True, header=True)
df.to_csv(fr"{site}\area.csv", index=True, header=True)


for i in path2:
    pandas.read_csv