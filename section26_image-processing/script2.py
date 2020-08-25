import cv2 as c
import glob
from pathlib import Path

file_list = glob.glob("images/*.jpg")

for file in file_list:
    img=c.imread(file)
    resized_image=c.resize(img,(100,100))
    obj=Path(file)
    c.imwrite(f"{obj.parent}\\{obj.stem}_resized.jpg",resized_image)
    c.imshow("",resized_image)
    c.waitKey(0)
    c.destroyAllWindows()