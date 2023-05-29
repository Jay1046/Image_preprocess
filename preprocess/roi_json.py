import cv2
import numpy as np
import json
import datetime
import random


class ROI1:
    def __init__(self):
        self.name = 'lena'
        self.today = str(datetime.datetime.today()).replace(' ','').replace(':','')
        self.isDragging = False
        self.x0 = -1
        self.y0 = -1
        self.coordinate = []
        self.result = {}
        self.colors = []
        self.img = cv2.imread('/Users/jylee/Desktop/codes/Image_preprocessing/Images/lena.jpg')
        self.path = '/Users/jylee/Desktop/codes/Image_preprocessing/json/{}_{}.json'.format(self.name, self.today)

    def onMouse(self, event, x, y, flags, param):
        
    
        if event == cv2.EVENT_LBUTTONDOWN:
            self.isDragging = True
            self.x0 = x
            self.y0 = y
            self.coordinate.append((x,y))
            
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.isDragging:
                img_draw = self.img.copy() 
                cv2.rectangle(img_draw, (self.x0,self.y0), (x,y), (255,0,0), 2)
                cv2.imshow('img', img_draw)
                
        elif event == cv2.EVENT_LBUTTONUP:
            if self.isDragging:
                self.isDragging = False
                
                if True:
                    self.result['result'] = 'True'
                    
                rand_col = (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
                cv2.rectangle(self.img, (self.x0, self.y0), (x, y), rand_col, 2)
                cv2.imshow('img', self.img)
                self.coordinate.append((x,y))
                self.colors.append(rand_col)
                    
                print(self.coordinate)


    def write_json(self, dict):
        with open(self.path, 'w') as f:
            json.dump(dict, f)

    def save(self):
        img = self.img
        cv2.imshow('img', self.img)
        cv2.setMouseCallback('img', self.onMouse)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        id = 1
        a = 0
        for color in self.colors:
        
            data = {'id': id, 'color':color, 'x1':self.coordinate[a][0], 'y1':self.coordinate[a][1],
                            'x2': self.coordinate[a+1][0], 'y2': self.coordinate[a+1][1]}
            if id == 1:
                self.result['data'] = [data]
            else:
                self.result['data'].append(data)
            id += 1
            a += 2

        print(self.result)

        self.write_json(self.result)


