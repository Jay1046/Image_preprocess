import numpy as np
import cv2
import datetime


class ROI3:
    def __init__(self):
        self.name = 'lena'
        self.today = str(datetime.datetime.today()).replace(' ','').replace(':','')
        self.isDragging = False
        self.x0 = -1
        self.y0 = -1
        self.img = cv2.imread('/Users/jylee/Desktop/codes/Image_preprocessing/Images/lena.jpg')
        self.path = '/Users/jylee/Desktop/codes/Image_preprocessing/Image_cropped/{}_partial_{}.jpg'.format(self.name, self.today)
        self.coordinate = []

    def onMouse(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN: 
            self.isDragging = True
            self.x0, self.y0 = x, y 
            print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

        elif event == cv2.EVENT_LBUTTONUP: 
            if self.isDragging:
                self.isDragging = False               

                print(self.coordinate)
                print('EVENT_LBUTTONUP: %d, %d' % (x, y)) 

                cv2.line(self.img, self.coordinate[0], self.coordinate[-1], 1, cv2.LINE_AA)
                cv2.imshow('image', self.img)
                result = np.array(self.coordinate)
                cv2.fillPoly(self.img, [result], (0, 255, 0))
                cv2.imshow('image', self.img)
                
            
                xmin = min([result[i, 0] for i in range(len(result))])-15
                ymin = min([result[i, 1] for i in range(len(result))])-15
                xmax = max([result[i, 0] for i in range(len(result))])+15
                ymax = max([result[i, 1] for i in range(len(result))])+15
                
                w = (xmax) - (xmin)
                h = (ymax) - (ymin)
                
                cv2.rectangle(self.img, (xmin, ymin), (xmax, ymax), (0,0,255), 2)
                cv2.imshow('image', self.img)
                
                roi = self.img[ymin:ymin+h, xmin:xmin+w]
                
                for h in range(roi.shape[0]):
                    for w in range(roi.shape[1]):
                        if (roi[h,w,:] == (0,255,0)).all():
                            continue
                        else:
                            roi[h,w, :] = (255,255,255)
                        
                cv2.imshow('cropped', roi)         
                cv2.moveWindow('cropped', 0,0)     
                cv2.imwrite(self.path, roi)  

        elif event == cv2.EVENT_MOUSEMOVE: 
            if self.isDragging:
                cv2.line(self.img, (self.x0, self.y0), (x, y), 1, cv2.LINE_AA)

                cv2.imshow('image', self.img)
                self.x0, self.y0 = x, y 
                self.coordinate.append([x,y])


    def save(self):
        img = self.img
        cv2.imshow('img', self.img)
        cv2.setMouseCallback('img', self.onMouse)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
