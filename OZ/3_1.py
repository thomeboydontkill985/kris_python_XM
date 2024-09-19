import cv2


zrn = cv2.imread("./3_1.jpg")
print("图片类型",type(zrn))
print(zrn.shape)
blue = zrn[190,168,0]
green = zrn[190,168,1]
red = zrn[190,168,2]
print(blue,green,red)
