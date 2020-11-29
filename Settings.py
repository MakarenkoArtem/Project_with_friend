# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(664, 589)
        self.label_7 = QtWidgets.QLabel(QWidget)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 632, 312))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(QWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(QWidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 562, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider_3 = QtWidgets.QSlider(QWidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(80, 90, 521, 19))
        self.horizontalSlider_3.setStyleSheet("background-color: rgb(150, 150, 255);")
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_4 = QtWidgets.QLabel(QWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 51, 16))
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalSlider_4 = QtWidgets.QSlider(QWidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(80, 130, 521, 19))
        self.horizontalSlider_4.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                              "background-color: rgb(255, 150, 150);\n"
                                              "alternate-background-color: rgb(255, 0, 0);\n"
                                              "color: rgb(255, 0, 0);\n"
                                              "gridline-color: rgb(255, 0, 0);\n"
                                              "selection-color: rgb(255, 0, 0);\n"
                                              "selection-background-color: rgb(255, 0, 0);")
        self.horizontalSlider_4.setMaximum(255)
        self.horizontalSlider_4.setSingleStep(1)
        self.horizontalSlider_4.setPageStep(10)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_2 = QtWidgets.QSlider(QWidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(80, 50, 521, 19))
        self.horizontalSlider_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider_2.setStyleSheet("background-color: rgb(150, 255, 150);")
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setPageStep(10)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.spinBox = QtWidgets.QSpinBox(QWidget)
        self.spinBox.setGeometry(QtCore.QRect(620, 10, 42, 22))
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_2 = QtWidgets.QPushButton(QWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 562, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(QWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(QWidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.spinBox_4 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_4.setGeometry(QtCore.QRect(620, 130, 42, 22))
        self.spinBox_4.setMaximum(255)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_2 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_2.setGeometry(QtCore.QRect(620, 50, 42, 22))
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(QWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalSlider_5 = QtWidgets.QSlider(QWidget)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(80, 170, 521, 19))
        self.horizontalSlider_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider_5.setStyleSheet("background-color: rgb(150, 255, 150);")
        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setSingleStep(1)
        self.horizontalSlider_5.setPageStep(10)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_6")
        self.spinBox_6 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_6.setGeometry(QtCore.QRect(620, 210, 42, 22))
        self.spinBox_6.setMaximum(255)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalSlider_6 = QtWidgets.QSlider(QWidget)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(80, 210, 521, 19))
        self.horizontalSlider_6.setStyleSheet("background-color: rgb(150, 150, 255);")
        self.horizontalSlider_6.setMaximum(255)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_5")
        self.spinBox_5 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_5.setGeometry(QtCore.QRect(620, 170, 42, 22))
        self.spinBox_5.setMaximum(255)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_3 = QtWidgets.QSpinBox(QWidget)
        self.spinBox_3.setGeometry(QtCore.QRect(620, 90, 42, 22))
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalSlider = QtWidgets.QSlider(QWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 10, 521, 19))
        self.horizontalSlider.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                                            "background-color: rgb(255, 150, 150);\n"
                                            "alternate-background-color: rgb(255, 0, 0);\n"
                                            "color: rgb(255, 0, 0);\n"
                                            "gridline-color: rgb(255, 0, 0);\n"
                                            "selection-color: rgb(255, 0, 0);\n"
                                            "selection-background-color: rgb(255, 0, 0);")
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QtWidgets.QLabel(QWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 61, 16))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 255, 0);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "QWidget"))
        self.label_7.setText(_translate("QWidget", "TextLabel"))
        self.label_2.setText(_translate("QWidget", "min_green"))
        self.pushButton.setText(_translate("QWidget", "Сохранить"))
        self.label_4.setText(_translate("QWidget", "max_red"))
        self.pushButton_2.setText(_translate("QWidget", "Отмена"))
        self.label_6.setText(_translate("QWidget", "max_blue"))
        self.label.setText(_translate("QWidget", "min_red"))
        self.label_3.setText(_translate("QWidget", "min_blue"))
        self.label_5.setText(_translate("QWidget", "max_green"))
