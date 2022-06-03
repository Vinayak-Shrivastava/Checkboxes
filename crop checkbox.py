import cv2
import numpy as np

for j in [0,1,2,3,4,5,6,7,8,9,10]:       #to open and crop each image one by one
    nm =  r'{}'.format(j)
    path = r"C:\Users\Vinayak Shrivastava\PycharmProjects\pythonProject\checkbox\Raw images\img-" + nm +".jpg"
    img = cv2.imread(path)
    sharpen_kernel = np. array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])      #sharpens the image if it is blurry
    imgs = cv2. filter2D(img, -1, sharpen_kernel)
    imgg = cv2.cvtColor(imgs,cv2.COLOR_BGR2GRAY)                       #processing the image
    imgb = cv2.GaussianBlur(imgg,(5,5), 1)
    imgf = cv2.Canny(imgb,10,50)

    contours, hierarchy = cv2.findContours(imgf,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)           # making contours to detect the curves available

    z=0                                           #to find the checkbox as the checkbox's contour will have maximum points
    i = len(contours) - 1
    while(i>0):
        if(z < len(contours[i])):
            z = len(contours[i])
            a=i
        i=i-1

    x_max=y_max=0                                   #finding the two corner points in the contours
    y_min, x_min, _ = img.shape                     #the corner points will help us to crop the desired region which contains the chekbox only

    for [[x, y]] in contours[a]:
        if(x > x_max): x_max = x
        if(y > y_max): y_max = y
        if(x < x_min): x_min = x
        if(y < y_min): y_min = y

    img = img[y_min:y_max,x_min:x_max]                  #croping the image

    nm = r"image-"+nm+" crop.jpg"                       #naming the image accordingly
    cv2.imwrite(nm,img)                                  #saving the cropped image
