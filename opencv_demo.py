# coding:utf-8
import cv2 as cv


def face_detect_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray,1.02,2)
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",image)
#图片检测
def detectImg():
    src = cv.imread("images/2.jpg")
    # print(type(src))
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    face_detect_demo(src)
    cv.waitKey(0)
    cv.destroyAllWindows()
#视频实时监测
def detectCapture():
    capture = cv.VideoCapture()
    cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
    while True:
        ret,frame = capture.read()
        if ret is True:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            print('1223')
        else:
            break
        frame = cv.flip(frame,1)
        #face_detect_demo(frame)
        face_detector = cv.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
        faces = face_detector.detectMultiScale(gray, 1.02, 3)
        for x, y, w, h in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.imshow("result", frame)
        c=cv.waitKey(10)
        if c==27:#esc
            break
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():
    #detectImg()
    detectCapture()
if __name__ == "__main__":
    main()




