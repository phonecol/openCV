import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Plot the data

def get_bgr_values(x,y,img):
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
    # print(bVal)
    # print(gVal)
    # print(rVal)
    return bValue,gValue,rValue


x_val = []
paperSensors = []
for i in range(0,12):
   paperSensor = cv2.imread(str(i)+"0ppm.PNG")
   paperSensors.append(paperSensor)


bVal = []
gVal = []
rVal = []

bVals = []
gVals = []
rVals = []
x = []
for i in range(0, 12):
    while True:
        # img = paperSensors[i]
        # img = cv2.cvtColor(paperSensors[i],cv2.COLOR_BGR2HSV)
        img = paperSensors[i+1]
        #img = cv2.resize(img, None, fx=0.5, fy=0.5)

        HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        lower = np.array([160,9,110]) #how to get this value
        upper = np.array([179,40,150]) #how to get this value
        mask = cv2.inRange(HSV,lower,upper)
        imgResult = cv2.bitwise_and(img,img, mask=mask)
        # ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        imgResultHSV = cv2.cvtColor(imgResult,cv2.COLOR_BGR2HSV)

        bValue,gValue,rValue = get_bgr_values(60,60,img)
        # cv2.imshow("Grays",gray)
        bVals.append(bValue)
        gVals.append(gValue)
        rVals.append(rValue)
        print("bvals",bVals)
        print("gvals",gVals)
        print("rvals",rVals)
        print(i+1)
        x_val.append(i)
        print(x_val)
        cv2.imshow("Original",img)

        plt.plot( x_val,bVals, label='linear')
        plt.plot( x_val,gVals, label='linear')
        plt.plot( x_val,rVals, label='linear')
        # Add a legend
        plt.legend()

        # Show the plot
        plt.show()




        if cv2.waitKey(0) &0xFF == ord("q"):
            cv2.destroyAllWindows()
            break



