import cv2
import numpy as np
from matplotlib import pyplot as plt

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def coords_mouse_disp(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #left mouse double click
        print("Orginal BGR:",img[x,y])
        print("HSV values:", HSV[x,y])
        print("Gray Values:", gray[x,y])
        print("masked BGR:",imgResult[x,y])
        print("masked HSV values:", imgResultHSV[x,y])


        print(np.average(imgResult, axis = (0,1)))
        print(x,y)
        nonBlack = cv2.countNonZero(mask)
        totalPixel = imgResult.shape[1] * imgResult.shape[0]
        #  maskedPixel = totalPixel- number_of_black_pix

        totalPixelValues = cv2.sumElems(imgResult)
        print("Not Black", nonBlack)
        print("Widths",imgResult.shape[1])

        print("Height",imgResult.shape[0])
        print("Total Pixel",totalPixel)
        print("masked Pixel",nonBlack)
        #  print("number of black Pixel",number_of_black_pix)
        print(totalPixelValues)

        print(totalPixelValues[0]/nonBlack)

        print(totalPixelValues[1]/nonBlack)

        print(totalPixelValues[2]/nonBlack)
path = "100ppm.png"
while True:
    img = cv2.imread(path)
    #img = cv2.resize(img, None, fx=0.5, fy=0.5)
    HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lower = np.array([160,9,110]) #how to get this value
    upper = np.array([179,40,150]) #how to get this value
    mask = cv2.inRange(HSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img, mask=mask)
    # ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    imgResultHSV = cv2.cvtColor(imgResult,cv2.COLOR_BGR2HSV)

    # cv2.imshow("Grays",gray)
    b,g,r = cv2.split(imgResult)

    # cv2.imshow("img",img)
    # cv2.imshow("b",r)
    # cv2.imshow("g",g)
    # cv2.imshow("r",r)

    # plt.hist(b.ravel(),256,[0,256])
    # plt.hist(g.ravel(),256,[0,256])
    plt.hist(b.ravel(),256,[0,256])
    plt.hist(g.ravel(),256,[0,256])
    plt.hist(r.ravel(),256,[0,256])
    plt.show()

    cv2.imshow("Original",img)
    cv2.imshow("HSV", HSV)
    cv2.imshow("Gray",gray)
    cv2.imshow("Mask", mask)
    cv2.imshow("asd",imgResult)
    cv2.imshow("imgResultHSV",imgResultHSV)
    # left mouse click event
    imgStack = stackImages(1,([img, HSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    cv2.setMouseCallback("imgResultHSV", coords_mouse_disp)
    cv2.setMouseCallback("HSV", coords_mouse_disp)
    cv2.setMouseCallback("Gray", coords_mouse_disp)
    cv2.setMouseCallback("Original", coords_mouse_disp)
    cv2.setMouseCallback("asd", coords_mouse_disp)
    cv2.setMouseCallback("Stacked Images", coords_mouse_disp)
    if cv2.waitKey(1) &0xFF == ord("q"):
        cv2.destroyAllWindows()
        break