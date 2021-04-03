# coding=utf-8
# 2021.4.2

# import cv2 as cv
from cv2 import cv2


def main():
    # load a pic
    # colored img
    img = cv2.imread("2.png",1)
    # Black&white img
    img1 = cv2.imread("2.png",0)
    
    # check img shape
    print(type(img))
    print(img.shape)
    print(img1.shape)

    # show pic
    cv2.imshow("Penguins", img1)
    cv2.waitKey(0)# hold
    cv2.destroyAllWindows()

    # change pic shape
    resizedImg = cv2.resize(img, (300,300))# only change high & wide, can not change channal
    cv2.imshow("Penguins", resizedImg)
    cv2.waitKey(0)# hold
    cv2.destroyAllWindows()

    # change pic color
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Penguins", gray_img)
    cv2.waitKey(0)# hold
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()