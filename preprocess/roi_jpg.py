import cv2
import numpy as np
import datetime


class ROI2:
    def __init__(self):
        self.name = 'lena'
        self.today = str(datetime.datetime.today()).replace(' ','').replace(':','')
        self.isDragging = False
        self.x0 = -1
        self.y0 = -1
        self.w = -1
        self.h = -1
        self.img = cv2.imread('/Users/jylee/Desktop/codes/Image_preprocessing/Images/lena.jpg')
        self.path = '/Users/jylee/Desktop/codes/Image_preprocessing/Image_cropped/{}_cropped_{}.jpg'.format(self.name, self.today)
        self.blue = (255,0,0)
        self.red = (0,0,255)



    def onMouse(self, event, x, y, flags, param):     
        
        if event == cv2.EVENT_LBUTTONDOWN:      
            self.isDragging = True
            self.x0 = x
            self.y0 = y
            
        elif event == cv2.EVENT_MOUSEMOVE:      
            if self.isDragging:                      
                img_draw = self.img.copy()            
                cv2.rectangle(img_draw, (self.x0,self.y0), (x,y), self.blue, 2) 
                cv2.imshow('img', img_draw)      
                
        elif event == cv2.EVENT_LBUTTONUP:       
            if self.isDragging:                        
                self.isDragging = False           
                    
                self.w= x - self.x0                         
                self.h= y - self.y0                         

                if self.w>0 and self.h>0:                  
                    img_draw = self.img.copy()        
                    cv2.rectangle(img_draw, (self.x0, self.y0), (x, y), self.red, 2) 
                    cv2.imshow('img', img_draw)         
                    roi = self.img[self.y0:self.y0+self.h, self.x0:self.x0+self.w]         
                    cv2.imshow('cropped', roi)          
                    cv2.moveWindow('cropped', 0,0)    
                    cv2.imwrite(self.path, roi)  

                
                else:
                    cv2.imshow('img', self.img)
                    print('Please drag the image from left to right')

    def save(self):
        img = self.img
        cv2.imshow('img', self.img)
        cv2.setMouseCallback('img', self.onMouse)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

