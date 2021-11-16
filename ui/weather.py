# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from ui import ico_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 568)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cloud_32/cloud_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(300, 40, 481, 251))
        self.widget.setObjectName("widget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 481, 251))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 296, 771, 241))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.resText = QtWidgets.QTextEdit(self.groupBox)
        self.resText.setEnabled(True)
        self.resText.setGeometry(QtCore.QRect(10, 45, 291, 245))
        self.resText.setObjectName("resText")
        self.queryBtn = QtWidgets.QPushButton(self.groupBox)
        self.queryBtn.setGeometry(QtCore.QRect(680, 10, 75, 23))
        self.queryBtn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.queryBtn.setObjectName("queryBtn")
        self.select_label = QtWidgets.QLabel(self.groupBox)
        self.select_label.setEnabled(True)
        self.select_label.setGeometry(QtCore.QRect(40, 10, 50, 21))
        self.select_label.setMinimumSize(QtCore.QSize(50, 0))
        self.select_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.select_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_label.setObjectName("select_label")
        self.city_box = QtWidgets.QComboBox(self.groupBox)
        self.city_box.setGeometry(QtCore.QRect(420, 10, 81, 20))
        self.city_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.city_box.setObjectName("city_box")
        self.province_box = QtWidgets.QComboBox(self.groupBox)
        self.province_box.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.province_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.province_box.setObjectName("province_box")
        self.country_box = QtWidgets.QComboBox(self.groupBox)
        self.country_box.setGeometry(QtCore.QRect(160, 10, 50, 20))
        self.country_box.setMaximumSize(QtCore.QSize(60, 16777215))
        self.country_box.setObjectName("country_box")
        self.country_box.addItem("")
        self.country_label = QtWidgets.QLabel(self.groupBox)
        self.country_label.setEnabled(True)
        self.country_label.setGeometry(QtCore.QRect(110, 10, 50, 21))
        self.country_label.setMinimumSize(QtCore.QSize(50, 0))
        self.country_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.country_label.setAlignment(QtCore.Qt.AlignCenter)
        self.country_label.setObjectName("country_label")
        self.province_label = QtWidgets.QLabel(self.groupBox)
        self.province_label.setEnabled(True)
        self.province_label.setGeometry(QtCore.QRect(229, 10, 61, 21))
        self.province_label.setMinimumSize(QtCore.QSize(50, 0))
        self.province_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.province_label.setAlignment(QtCore.Qt.AlignCenter)
        self.province_label.setObjectName("province_label")
        self.county_box = QtWidgets.QComboBox(self.groupBox)
        self.county_box.setGeometry(QtCore.QRect(570, 10, 81, 20))
        self.county_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.county_box.setObjectName("county_box")
        self.city_label = QtWidgets.QLabel(self.groupBox)
        self.city_label.setEnabled(True)
        self.city_label.setGeometry(QtCore.QRect(390, 10, 31, 21))
        self.city_label.setMinimumSize(QtCore.QSize(0, 0))
        self.city_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.county_label = QtWidgets.QLabel(self.groupBox)
        self.county_label.setEnabled(True)
        self.county_label.setGeometry(QtCore.QRect(520, 10, 41, 21))
        self.county_label.setMinimumSize(QtCore.QSize(0, 0))
        self.county_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.county_label.setAlignment(QtCore.Qt.AlignCenter)
        self.county_label.setObjectName("county_label")
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.queryBtn.clicked.connect(Dialog.query_weather)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "城市天气"))
        self.groupBox_2.setTitle(_translate("Dialog", "气温变化图"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "天气"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "高温"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "低温"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "日出"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "日落"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "AQI"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "风向"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "风力"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "注意事项"))
        self.queryBtn.setText(_translate("Dialog", "Query"))
        self.select_label.setText(_translate("Dialog", "选择城市"))
        self.country_box.setItemText(0, _translate("Dialog", "中国"))
        self.country_label.setText(_translate("Dialog", "国家:"))
        self.province_label.setText(_translate("Dialog", "省/直辖市:"))
        self.city_label.setText(_translate("Dialog", "市:"))
        self.county_label.setText(_translate("Dialog", "区/县:"))

