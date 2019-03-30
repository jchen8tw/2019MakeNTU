import cv2
import os
def captureImg():
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280.0)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT ,720.0)
    if os.path.exists("opencv.jpg"):
          os.remove("opencv.jpg")
    return_value, image = camera.read()
    cv2.imwrite('opencv.jpg', image)
    f = open('opencv.jpg','rb')
    del(camera)
    return f
if __name__ == "__main__":
    captureImg()
