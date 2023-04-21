import sys
import numpy as np
import cv2
import datetime

img = cv2.imread('./Image_Processing/lena.jpg')
oldx = oldy = -1 # 좌표 기본값 설정

name = 'lena'
today = str(datetime.datetime.today()).replace(' ','').replace(':','')

isDragging = False 
coordinate = []



def on_mouse(event, x, y, flags, param):

    global oldx, oldy, isDragging, img

    if event == cv2.EVENT_LBUTTONDOWN: 
        isDragging = True
        oldx, oldy = x, y 
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP: 
        if isDragging:
            isDragging = False               

            print(coordinate)
            print('EVENT_LBUTTONUP: %d, %d' % (x, y)) 

            cv2.line(img, coordinate[0], coordinate[-1], 1, cv2.LINE_AA)
            cv2.imshow('image', img)
            result = np.array(coordinate)
            cv2.fillPoly(img, [result], (0, 255, 0))
            cv2.imshow('image', img)
            
        
            xmin = min([result[i, 0] for i in range(len(result))])-15
            ymin = min([result[i, 1] for i in range(len(result))])-15
            xmax = max([result[i, 0] for i in range(len(result))])+15
            ymax = max([result[i, 1] for i in range(len(result))])+15
            
            w = (xmax) - (xmin)
            h = (ymax) - (ymin)
            
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0,0,255), 2)
            cv2.imshow('image', img)
            
            roi = img[ymin:ymin+h, xmin:xmin+w]
            
            for h in range(roi.shape[0]):
                for w in range(roi.shape[1]):
                    if (roi[h,w,:] == (0,255,0)).all():
                        continue
                    else:
                        roi[h,w, :] = (255,255,255)
                     
            cv2.imshow('cropped', roi)         
            cv2.moveWindow('cropped', 0,0)     
            cv2.imwrite('./Image_cropped/{}_partial_{}.jpg'.format(name, today), roi)  

    elif event == cv2.EVENT_MOUSEMOVE: 
        if isDragging:
            cv2.line(img, (oldx, oldy), (x, y), 1, cv2.LINE_AA)

            cv2.imshow('image', img)
            oldx, oldy = x, y 
            coordinate.append([x,y])
            
cv2.namedWindow('image')


cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()