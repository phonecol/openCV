path = "./images/nemo"

nemos_friends = []

for i in range(6):
    friend = cv2.cvtColor(cv2.imread(path + str(i) + ".jpg"), cv2.COLOR_BGR2RGB)
    nemos_friends.append(friend)

def segment_fish(image):

    #convert the image into HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    #set the orange range
    light_orange = (1,190,200)
    dark_orange = (18,255,255)

    #apply the orange mask
    mask = cv2.inRange(hsv_image,light_orange,dark_orange)

    #set a white range
    light_white = (0,0,200)
    dark_white = (145,60,255)

    #apply the white mask
    mask_white = cv2.inRange(hsv_image, light_white, dark_white)

    #combine the two masks
    final_mask = mask + mask_white
    result = cv2.bitwise_and(image,image, mask=final_mask)

    #clean up the segmentation using a blur
    blur = cv2.GaussianBlur(result,(7,7),0)
    return blur

results = [segment_fish(friend for friend in nemos_friends)]

for i in range(1,6):
    plt.subplot(1,2,1)
    plt.imshow(nemos_friends)[i])
    plt.subplot(1,2,2)
    plt.imshow(results[i])
    plt.show()