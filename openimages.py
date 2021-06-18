
import matplotlib.pyplot as plt
import numpy as np
import cv2


def coords_mouse_disp(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #left mouse double click
        print("Orginal BGR:",img[x,y])
        print("HSV values:", HSV[x,y])
        print("Gray Values:", gray[x,y])
        print("masked BGR:",imgResult[x,y])
        print("masked HSV values:", imgResultHSV[x,y])
        bValue = img[x,y][0]
        gValue = img[x,y][1]
        rValue = img[x,y][2]
        bVal.append(bValue)
        gVal.append(gValue)
        rVal.append(rValue)
        print(bValue)
        print(gValue)
        print(rValue)
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

        # print(totalPixelValues[0]/nonBlack)

        # print(totalPixelValues[1]/nonBlack)

        # print(totalPixelValues[2]/nonBlack)

        # print(paperSensors)
        # print(rVal)
        # print(bVal)
        # print(gVal)
        print(bVal)
        print(gVal)
        print(rVal)
    return bValue,gValue,rValue

def bgrVal(x,y):
    pass

paperSensors = []
for i in range(1,10):
   paperSensor = cv2.imread(str(i) +"0ppm.PNG")
   paperSensors.append(paperSensor)
   print(i)

bVal = []
gVal = []
rVal = []

bVals = []
gVals = []
rVals = []
for i in range(1, 10):
    while True:
        # img = paperSensors[i]
        # img = cv2.cvtColor(paperSensors[i],cv2.COLOR_BGR2HSV)
        img = paperSensors[i]
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

        cv2.imshow("Original",img)
        # cv2.imshow("HSV", HSV)
        # cv2.imshow("Gray",gray)
        # cv2.imshow("Mask", mask)
        # cv2.imshow("asd",imgResult)
        # cv2.imshow("imgResultHSV",imgResultHSV)
        # left mouse click event
        # imgStack = stackImages(1,([img, HSV],[mask,imgResult]))
        # cv2.imshow("Stacked Images", imgStack)
        cv2.setMouseCallback("imgResultHSV", coords_mouse_disp)
        cv2.setMouseCallback("HSV", coords_mouse_disp)
        cv2.setMouseCallback("Gray", coords_mouse_disp)
        cv2.setMouseCallback("Original", coords_mouse_disp )
        cv2.setMouseCallback("asd", coords_mouse_disp)
        # bValue,gValue,rValue = bgrVal()
        # cv2.setMouseCallback("Stacked Images", coords_mouse_disp)
        if cv2.waitKey(1) &0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        bVals.append(bValue)
        gVals.append(gValue)
        rVals.append(rValue)
        print(bVal)
        print(gVal)
        print(rVal)

