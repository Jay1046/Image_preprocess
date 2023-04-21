import cv2
import numpy as np
import json
import datetime
import random

name = 'lena'
today = str(datetime.datetime.today()).replace(' ','').replace(':','')
isDragging = False
x0,y0 = -1,-1                 
# blue,red,green = (255,0,0),(0,0,255),(0,255,0)            

coordinate = [] # 시작점과 끝점을 저장할 list
result = {} # Json 파일 저장을 위한 dictionary
colors = []

def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
        coordinate.append((x,y))
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy() 
            cv2.rectangle(img_draw, (x0,y0), (x,y), (255,0,0), 2)
            cv2.imshow('img', img_draw)
            
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            
            if True:
                result['result'] = 'True'
                
            rand_col = (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
            cv2.rectangle(img, (x0, y0), (x, y), rand_col, 2)
            cv2.imshow('img', img)
            coordinate.append((x,y))
            colors.append(rand_col)
                
            print(coordinate)
            
#########################
# json save
def write_json(path, dict):
    with open(path, 'w') as file:
        json.dump(dict, file)
        
##########################

img = cv2.imread('./Image_Processing/lena.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse) # 마우스 이벤트 등록

cv2.waitKey()
cv2.destroyAllWindows()

id = 1
a = 0
for color in colors:
    
    data = {'id': id, 'color':color, 'x1':coordinate[a][0], 'y1':coordinate[a][1],
                    'x2': coordinate[a+1][0], 'y2': coordinate[a+1][1]}
    if id == 1:
        result['data'] = [data]
    else:
        result['data'].append(data)
    id += 1
    a += 2

print(result)

write_json('./json/{}_{}.json'.format(name, today), result)