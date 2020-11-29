from cv2 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import *
from PyQt5.QtGui import *
from time import sleep
from timeit import timeit
from Base import Ui_MainWindow
from Settings import Ui_Dialog
from time import sleep


class Settings(QDialog, Ui_Dialog):
    def __init__(self, number, color):
        super().__init__()
        self.setupUi(self)
        '''try:
            self.cap = VideoCapture(number, CAP_DSHOW)
        except Warning:
            self.cap = VideoCapture(number)'''
        self.color = 38
        c = [20, 0, 95, 75, 85, 175]
        if color == 'Blue':
            self.color = 51
            c = [50, 15, 10, 130, 70, 70]
        print(color)
        self.setWindowTitle(color)
        print(2)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.ret)
        self.s = [self.spinBox, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5,
                  self.spinBox_6]
        self.z = [self.horizontalSlider, self.horizontalSlider_2, self.horizontalSlider_3,
                  self.horizontalSlider_4, self.horizontalSlider_5, self.horizontalSlider_6]
        for i in range(6):
            self.z[i].setValue(c[i])
            self.z[i].valueChanged.connect(self.valuechange)
            self.s[i].setValue(c[i])
            self.s[i].valueChanged.connect(self.valuechangespin)
        print(2)
        self.run()

    def valuechangespin(self):
        print(22)
        self.z[self.s.index(self.sender())].setValue(self.sender().value())
        self.run()

    def valuechange(self):
        print(11)
        self.s[self.z.index(self.sender())].setValue(self.sender().value())
        #self.run()

    def ret(self):
        print(33)
        self.cap.release()
        # return [i.value() for i in self.z]
        self.close()

    def run(self):
        print(44)
        #ret, frame = self.cap.read()
        frame = imread('Colors.jpg')
        imgHLS = cvtColor(frame, self.color)
        print((self.z[0].value(), self.z[1].value(), self.z[2].value()),
                       (self.z[3].value(), self.z[4].value(), self.z[5].value()))
        mask = inRange(imgHLS, (self.z[0].value(), self.z[1].value(), self.z[2].value()),
                       (self.z[3].value(), self.z[4].value(), self.z[5].value()))
        mask = bitwise_and(frame, frame, mask=mask)
        pic = resize(frame, (632, 312), interpolation=INTER_AREA)
        # imshow("pic", pic)
        convertToQtFormat = QtGui.QImage(pic.data, 632, 312, QtGui.QImage.Format_RGB888)
        convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
        self.label_7.setPixmap(QPixmap(convertToQtFormat))
        #self.show()
        sleep(1)


class Vision(QWidget, Ui_MainWindow):
    def __init__(self, number):
        super().__init__()
        self.setupUi(self)
        try:
            self.cap = VideoCapture(number, CAP_DSHOW)
        except Warning:
            self.cap = VideoCapture(number)
        self.number = number
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.settings)
        self.pushButton_2.clicked.connect(self.settings)
        self.i = 0
        self.func = None
        '''self.setGeometry(100, 100, 370, 330)
        self.setWindowTitle('Изменение прозрачности')
        self.image = QLabel(self)
        self.image.move(50, 15)
        self.image.resize(300, 300)'''

    def settings(self):
        c = 'Red'
        if self.sender() == self.pushButton_2:
            c = 'Blue'
        print(1)
        # ap = QApplication(sys.argv)
        f = Settings(self.number, c).exec_()
        # f.run()
        # ap.exec_()
        # ap.exec()
        print(2222222)
        self.func(1000)

    def release(self):
        # self.out.release()
        # self.blue.release()
        # self.red.release()
        self.cap.release()
        print("Надеюсь мы не разбились, жду встречи ;)")

    def sign(self, occasion=1, time=0):
        def color(asd):
            c = [200, 10, 10, 255, 200, 110]
            if asd == "red_":
                c = [0, 10, 175, 20, 140, 255]
            r = ["minb", "ming", "minr", "maxb", "maxg", "maxr"]

            def nothing(x):
                pass

            f = asd + f"result"
            namedWindow(f)
            for i in range(6):
                createTrackbar(r[i], f, c[i], 255, nothing)
            frame = imread('Colors.jpg')
            while True:
                # ret, frame = self.cap.read()
                hsv = cvtColor(frame, COLOR_BGR2HSV)
                hsv = blur(hsv, (5, 5))
                c = []
                for i in range(6):
                    c.append(getTrackbarPos(r[i], f))
                mask = inRange(frame, (c[0], c[1], c[2]), (c[3], c[4], c[5]))
                maskEr = erode(mask, (3, 3), iterations=2)
                maskDi = dilate(maskEr, (3, 3), iterations=2)
                imshow("Dilate", maskDi)
                result = bitwise_and(frame, frame, mask=mask)
                imshow(f, result)
                if waitKey(1) == ord("q"):
                    break
            destroyAllWindows()
            return [minb, ming, minr, maxb, maxg, maxr]

        inp = input(
            "Если вы хотите сами написать границы, то напишите 'w', если вы хотите готовые границы, то напишите 'r', если хотите подобрать границы, то напишите любую другую букву или не пишите ничего, ввод: ")
        if inp == "w":
            r = list(int(i) for i in input("Red: ").split(", "))
            b = list(int(i) for i in input("Blue: ").split(", "))
        elif inp == "r":
            r = [0, 10, 175, 20, 140, 255]
            b = [200, 10, 10, 255, 200, 110]
        else:
            r = color("red_")
            b = color("blue_")
        rn = [(2, 32), (62, 32), (32, 62), (32, 2), (6, 60), (60, 60), (19, 20),
              (44, 44), (19, 44), (44, 19), (20, 31), (44, 33)]
        no_entry = [True, True, True, True, False, False, True, True, True, True, True,
                    True]
        stop_is_prohibited = [True, True, True, True, False, False, True, True, True,
                              True, False, False]
        no_parking = [True, True, True, True, False, False, True, True, False, False,
                      False, False]
        speed = [True, True, True, True, False, False, False, False, False, False,
                 False, False]
        bn = [(3, 3), (3, 60), (60, 3), (60, 60), (28, 3), (38, 3), (31, 25), (42, 13), (22, 13)]
        pedestrian_crossing = [True, True, True, True, True, True, False, True, True]
        park = [True, True, True, True, True, True, True, False, False]
        m = ''
        ma = ''
        start = timeit()
        for i in range(self.i, occasion):
            print(1)
            self.func = self.sign
            print(2)
            ret, frame = self.cap.read()
            '''if not ret:
                continue
            print(i)

            def e(ca):
                colo = (0, 0, 255)
                c = r
                rnt = rn
                if ca == "Blue":
                    c = b
                    rnt = bn
                    colo = (255, 0, 0)
                ra = blur(frame, (5, 5))
                ra = GaussianBlur(ra, (3, 3), 0)
                ra = erode(ra, (6, 6), iterations=3)
                ra = dilate(ra, (5, 5), iterations=2)
                ra = inRange(ra, (c[0], c[1], c[2]), (c[3], c[4], c[5]))
                # imshow(ca, ra)
                contours = findContours(ra, RETR_TREE, CHAIN_APPROX_NONE)
                contours = contours[0]  # or [1] в линуксе на ноуте
                pic = frame[0:64, 0:64]
                pic = inRange(pic, (0, 0, 0), (100, 100, 100))
                if contours:
                    contours = sorted(contours, key=contourArea, reverse=True)
                    drawContours(frame, contours[0], -1, (0, 255, 0), 3)
                    x, y, w, h = boundingRect(contours[0])
                    rectangle(frame, (x, y), (x + w, y + h), colo, 2)
                    pic = ra[y:y + h, x:x + w]
                    pic = resize(pic, (64, 64))
                imwrite('bw.png', pic)
                rt = imread('bw.png')
                rq = []
                for x, y in rnt:
                    if pic[y][x]:  # pic
                        circle(rt, (x, y), 3, (0, 250, 0), -1)  # rt
                        rq.append(True)
                    else:
                        circle(rt, (x, y), 3, colo, -1)  # rt
                        rq.append(False)
                imshow(ca, rt)  # rt
                if ca == "Blue":
                    self.blue.write(rt)
                else:
                    self.red.write(rt)
                return rq

            rrb = e("Red")

            # putText(frame, m, (50, 40), FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)'''
            pic = resize(frame, (352, 300), interpolation=INTER_AREA)
            convertToQtFormat = QtGui.QImage(pic.data, 352, 300,
                                             QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            self.label.setPixmap(QPixmap(convertToQtFormat))
            self.show()

            imshow("pic", pic)
            imshow("Frame", frame)
            # self.out.write(frame)
            if waitKey(1) == ord("q"):
                break
            sleep(time)
        print(timeit() - start)
        destroyAllWindows()
        self.i = 0


app = QApplication(sys.argv)
# Settings(0, 'Red').show()
f = Vision(0)
f.sign(1000)
f.release()
sys.exit(app.exec())
# -0.012709328999993552
'''
c = [20, 0, 95, 75, 85, 175]  # [42, 75, 170, 145, 145, 250]COLOR_RGB2HSV
b = [50, 15, 10, 130, 70, 70]  # [110, 40, 30, 190, 120, 135]COLOR_RGB2HSV


def nothing(x):
    passq


f = f"result"
namedWindow(f)
createTrackbar("minb", f, c[0], 255, nothing)
createTrackbar("ming", f, c[1], 255, nothing)
createTrackbar("minr", f, c[2], 255, nothing)
createTrackbar("maxb", f, c[3], 255, nothing)
createTrackbar("maxg", f, c[4], 255, nothing)
createTrackbar("maxr", f, c[5], 255, nothing)
# frame = imread('Colors.jpg')
while True:
    ret, frame = self.cap.read()
    hsv = cvtColor(frame, COLOR_RGB2HSV)
    hsv = blur(hsv, (7, 7))
    minb = getTrackbarPos("minb", f)
    ming = getTrackbarPos("ming", f)
    minr = getTrackbarPos("minr", f)
    maxb = getTrackbarPos("maxb", f)
    maxg = getTrackbarPos("maxg", f)
    maxr = getTrackbarPos("maxr", f)
    mask = inRange(frame, (minb, ming, minr), (maxb, maxg, maxr))
    maskEr = erode(mask, None, iterations=2)
    maskDi = dilate(maskEr, None, iterations=2)
    imshow("Dilate", maskDi)
    result = bitwise_and(frame, frame, mask=mask)
    imshow(f, result)
    if waitKey(1) == ord("q"):
        break
print(c)
destroyAllWindows()
i = 0
r = 0
s = {0, 1, 2, 3, 4, 5, 6, 7, 128, 129, 10, 11, 131, 132, 133, 130, 32, 33, 34, 35, 36, 37, 38, 39,
     40, 41, 134, 44, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 66, 67, 68, 69, 70, 71,
     72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 127}
s = [38, 51]
for i in s:
    r = True
    while r:
        try:
            ret, frame = red.read()
            imgHLS = cvtColor(frame, i)
            imshow('red', imgHLS)
            # s.add(i)
            # print(imgHLS[150, 50])
            mask = inRange(imgHLS, (0, 0, 0), (360, 255, 255))
            mask = bitwise_and(frame, frame, mask=mask)
            imshow('redj', mask)
            rt = imread('Colors.jpg')
            imshow('jgкккккккk', rt)
            rt = cvtColor(rt, i)
            imshow('jgk', rt)
            r += 1
            if waitKey(1) == ord('t'):
                print(i)
                break
            elif waitKey(10) == ord('q') or not ret:
                break
        except BaseException:
            i += 1
            r = 0
print(s)
red.release()
cv2.destroyAllWindows()  # 38 51'''
'''COLOR_BAYER_BG2BGR = 46
    COLOR_BAYER_BG2BGRA = 139
    COLOR_BAYER_BG2BGR_EA = 135
    COLOR_BAYER_BG2BGR_VNG = 62
    COLOR_BAYER_BG2GRAY = 86
    COLOR_BAYER_BG2RGB = 48
    COLOR_BAYER_BG2RGBA = 141
    COLOR_BAYER_BG2RGB_EA = 137
    COLOR_BAYER_BG2RGB_VNG = 64
    COLOR_BAYER_GB2BGR = 47
    COLOR_BAYER_GB2BGRA = 140
    COLOR_BAYER_GB2BGR_EA = 136
    COLOR_BAYER_GB2BGR_VNG = 63
    COLOR_BAYER_GB2GRAY = 87
    COLOR_BAYER_GB2RGB = 49
    COLOR_BAYER_GB2RGBA = 142
    COLOR_BAYER_GB2RGB_EA = 138
    COLOR_BAYER_GB2RGB_VNG = 65
    COLOR_BAYER_GR2BGR = 49
    COLOR_BAYER_GR2BGRA = 142
    COLOR_BAYER_GR2BGR_EA = 138
    COLOR_BAYER_GR2BGR_VNG = 65
    COLOR_BAYER_GR2GRAY = 89
    COLOR_BAYER_GR2RGB = 47
    COLOR_BAYER_GR2RGBA = 140
    COLOR_BAYER_GR2RGB_EA = 136
    COLOR_BAYER_GR2RGB_VNG = 63
    COLOR_BAYER_RG2BGR = 48
    COLOR_BAYER_RG2BGRA = 141
    COLOR_BAYER_RG2BGR_EA = 137
    COLOR_BAYER_RG2BGR_VNG = 64
    COLOR_BAYER_RG2GRAY = 88
    COLOR_BAYER_RG2RGB = 46
    COLOR_BAYER_RG2RGBA = 139
    COLOR_BAYER_RG2RGB_EA = 135
    COLOR_BAYER_RG2RGB_VNG = 62
    COLOR_BGR2BGR555 = 22
    COLOR_BGR2BGR565 = 12
    COLOR_BGR2BGRA = 0
    COLOR_BGR2GRAY = 6
    COLOR_BGR2HLS = 52
    COLOR_BGR2HLS_FULL = 68
    COLOR_BGR2HSV = 40
    COLOR_BGR2HSV_FULL = 66
    COLOR_BGR2LAB = 44
    COLOR_BGR2LUV = 50
    COLOR_BGR2Lab = 44
    COLOR_BGR2Luv = 50
    COLOR_BGR2RGB = 4
    COLOR_BGR2RGBA = 2
    COLOR_BGR2XYZ = 32
    COLOR_BGR2YCR_CB = 36
    COLOR_BGR2YCrCb = 36
    COLOR_BGR2YUV = 82
    COLOR_BGR2YUV_I420 = 128
    COLOR_BGR2YUV_IYUV = 128
    COLOR_BGR2YUV_YV12 = 132
    COLOR_BGR5552BGR = 24
    COLOR_BGR5552BGRA = 28
    COLOR_BGR5552GRAY = 31
    COLOR_BGR5552RGB = 25
    COLOR_BGR5552RGBA = 29
    COLOR_BGR5652BGR = 14
    COLOR_BGR5652BGRA = 18
    COLOR_BGR5652GRAY = 21
    COLOR_BGR5652RGB = 15
    COLOR_BGR5652RGBA = 19
    COLOR_BGRA2BGR = 1
    COLOR_BGRA2BGR555 = 26
    COLOR_BGRA2BGR565 = 16
    COLOR_BGRA2GRAY = 10
    COLOR_BGRA2RGB = 3
    COLOR_BGRA2RGBA = 5
    COLOR_BGRA2YUV_I420 = 130
    COLOR_BGRA2YUV_IYUV = 130
    COLOR_BGRA2YUV_YV12 = 134
    COLOR_BayerBG2BGR = 46
    COLOR_BayerBG2BGRA = 139
    COLOR_BayerBG2BGR_EA = 135
    COLOR_BayerBG2BGR_VNG = 62
    COLOR_BayerBG2GRAY = 86
    COLOR_BayerBG2RGB = 48
    COLOR_BayerBG2RGBA = 141
    COLOR_BayerBG2RGB_EA = 137
    COLOR_BayerBG2RGB_VNG = 64
    COLOR_BayerGB2BGR = 47
    COLOR_BayerGB2BGRA = 140
    COLOR_BayerGB2BGR_EA = 136
    COLOR_BayerGB2BGR_VNG = 63
    COLOR_BayerGB2GRAY = 87
    COLOR_BayerGB2RGB = 49
    COLOR_BayerGB2RGBA = 142
    COLOR_BayerGB2RGB_EA = 138
    COLOR_BayerGB2RGB_VNG = 65
    COLOR_BayerGR2BGR = 49
    COLOR_BayerGR2BGRA = 142
    COLOR_BayerGR2BGR_EA = 138
    COLOR_BayerGR2BGR_VNG = 65
    COLOR_BayerGR2GRAY = 89
    COLOR_BayerGR2RGB = 47
    COLOR_BayerGR2RGBA = 140
    COLOR_BayerGR2RGB_EA = 136
    COLOR_BayerGR2RGB_VNG = 63
    COLOR_BayerRG2BGR = 48
    COLOR_BayerRG2BGRA = 141
    COLOR_BayerRG2BGR_EA = 137
    COLOR_BayerRG2BGR_VNG = 64
    COLOR_BayerRG2GRAY = 88
    COLOR_BayerRG2RGB = 46
    COLOR_BayerRG2RGBA = 139
    COLOR_BayerRG2RGB_EA = 135
    COLOR_BayerRG2RGB_VNG = 62'''
