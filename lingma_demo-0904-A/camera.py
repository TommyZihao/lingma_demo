# 实时显示摄像头画面
# 同济子豪兄 2024-8-29

import cv2
import time
import hiwonder.Camera as Camera

my_camera = Camera.Camera()
my_camera.camera_open()           

while True:
    ret, img = my_camera.read()
    if ret:
        frame = img.copy()       
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        time.sleep(0.01)
my_camera.camera_close()
cv2.destroyAllWindows()