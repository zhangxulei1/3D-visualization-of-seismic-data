# Form implementation generated from reading ui file '.\display_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AppMainWindow(object):
    def setupUi(self, AppMainWindow):
        AppMainWindow.setObjectName("AppMainWindow")
        AppMainWindow.resize(200, 677)
        self.centralwidget = QtWidgets.QWidget(parent=AppMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        AppMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AppMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setObjectName("menu_4")
        AppMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AppMainWindow)
        self.statusbar.setObjectName("statusbar")
        AppMainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(parent=AppMainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(170, 39))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.fileMode_groupBox = QtWidgets.QGroupBox(parent=self.dockWidgetContents)
        self.fileMode_groupBox.setGeometry(QtCore.QRect(0, 0, 171, 141))
        self.fileMode_groupBox.setObjectName("fileMode_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fileMode_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.fileMode_groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.fileName_lineEdit = QtWidgets.QLineEdit(parent=self.fileMode_groupBox)
        self.fileName_lineEdit.setObjectName("fileName_lineEdit")
        self.horizontalLayout_4.addWidget(self.fileName_lineEdit)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.fileMode_groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.z_lineEdit = QtWidgets.QLineEdit(parent=self.fileMode_groupBox)
        self.z_lineEdit.setObjectName("z_lineEdit")
        self.horizontalLayout_5.addWidget(self.z_lineEdit)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.fileMode_groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.x_lineEdit = QtWidgets.QLineEdit(parent=self.fileMode_groupBox)
        self.x_lineEdit.setObjectName("x_lineEdit")
        self.horizontalLayout_6.addWidget(self.x_lineEdit)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.fileMode_groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.y_lineEdit = QtWidgets.QLineEdit(parent=self.fileMode_groupBox)
        self.y_lineEdit.setObjectName("y_lineEdit")
        self.horizontalLayout_7.addWidget(self.y_lineEdit)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.bodyDisplay_groupBox = QtWidgets.QGroupBox(parent=self.dockWidgetContents)
        self.bodyDisplay_groupBox.setGeometry(QtCore.QRect(10, 140, 91, 61))
        self.bodyDisplay_groupBox.setTitle("")
        self.bodyDisplay_groupBox.setObjectName("bodyDisplay_groupBox")
        self.bodyDisplay_checkBox = QtWidgets.QCheckBox(parent=self.bodyDisplay_groupBox)
        self.bodyDisplay_checkBox.setGeometry(QtCore.QRect(10, 20, 80, 20))
        self.bodyDisplay_checkBox.setObjectName("bodyDisplay_checkBox")
        self.slice_groupBox = QtWidgets.QGroupBox(parent=self.dockWidgetContents)
        self.slice_groupBox.setGeometry(QtCore.QRect(0, 210, 171, 151))
        self.slice_groupBox.setTitle("")
        self.slice_groupBox.setObjectName("slice_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.slice_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.slice_checkBox = QtWidgets.QCheckBox(parent=self.slice_groupBox)
        self.slice_checkBox.setObjectName("slice_checkBox")
        self.verticalLayout.addWidget(self.slice_checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.slice_groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.slicex_horizontalSlider = QtWidgets.QSlider(parent=self.slice_groupBox)
        self.slicex_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slicex_horizontalSlider.setObjectName("slicex_horizontalSlider")
        self.horizontalLayout.addWidget(self.slicex_horizontalSlider)
        self.slicex_lineEdit = QtWidgets.QLineEdit(parent=self.slice_groupBox)
        self.slicex_lineEdit.setObjectName("slicex_lineEdit")
        self.horizontalLayout.addWidget(self.slicex_lineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.slice_groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.slicey_horizontalSlider = QtWidgets.QSlider(parent=self.slice_groupBox)
        self.slicey_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slicey_horizontalSlider.setObjectName("slicey_horizontalSlider")
        self.horizontalLayout_2.addWidget(self.slicey_horizontalSlider)
        self.slicey_lineEdit = QtWidgets.QLineEdit(parent=self.slice_groupBox)
        self.slicey_lineEdit.setObjectName("slicey_lineEdit")
        self.horizontalLayout_2.addWidget(self.slicey_lineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.slice_groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.slicez_horizontalSlider = QtWidgets.QSlider(parent=self.slice_groupBox)
        self.slicez_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slicez_horizontalSlider.setObjectName("slicez_horizontalSlider")
        self.horizontalLayout_3.addWidget(self.slicez_horizontalSlider)
        self.slicez_lineEdit = QtWidgets.QLineEdit(parent=self.slice_groupBox)
        self.slicez_lineEdit.setObjectName("slicez_lineEdit")
        self.horizontalLayout_3.addWidget(self.slicez_lineEdit)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.isosurface_groupBox = QtWidgets.QGroupBox(parent=self.dockWidgetContents)
        self.isosurface_groupBox.setGeometry(QtCore.QRect(0, 380, 161, 141))
        self.isosurface_groupBox.setTitle("")
        self.isosurface_groupBox.setObjectName("isosurface_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.isosurface_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.isosurface_checkBox = QtWidgets.QCheckBox(parent=self.isosurface_groupBox)
        self.isosurface_checkBox.setObjectName("isosurface_checkBox")
        self.verticalLayout_3.addWidget(self.isosurface_checkBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(parent=self.isosurface_groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.isosurface_horizontalSlider = QtWidgets.QSlider(parent=self.isosurface_groupBox)
        self.isosurface_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.isosurface_horizontalSlider.setObjectName("isosurface_horizontalSlider")
        self.horizontalLayout_8.addWidget(self.isosurface_horizontalSlider)
        self.isosurface_lineEdit = QtWidgets.QLineEdit(parent=self.isosurface_groupBox)
        self.isosurface_lineEdit.setObjectName("isosurface_lineEdit")
        self.horizontalLayout_8.addWidget(self.isosurface_lineEdit)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(parent=self.isosurface_groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.transparency_horizontalSlider = QtWidgets.QSlider(parent=self.isosurface_groupBox)
        self.transparency_horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.transparency_horizontalSlider.setObjectName("transparency_horizontalSlider")
        self.horizontalLayout_9.addWidget(self.transparency_horizontalSlider)
        self.transparency_lineEdit = QtWidgets.QLineEdit(parent=self.isosurface_groupBox)
        self.transparency_lineEdit.setObjectName("transparency_lineEdit")
        self.horizontalLayout_9.addWidget(self.transparency_lineEdit)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.horizontalLayout_9.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.fault_go_Display_groupBox = QtWidgets.QGroupBox(parent=self.dockWidgetContents)
        self.fault_go_Display_groupBox.setGeometry(QtCore.QRect(10, 530, 91, 61))
        self.fault_go_Display_groupBox.setTitle("")
        self.fault_go_Display_groupBox.setObjectName("fault_go_Display_groupBox")
        self.fault_go_Display_checkBox = QtWidgets.QCheckBox(parent=self.fault_go_Display_groupBox)
        self.fault_go_Display_checkBox.setGeometry(QtCore.QRect(10, 20, 80, 20))
        self.fault_go_Display_checkBox.setObjectName("fault_go_Display_checkBox")
        self.dockWidget.setWidget(self.dockWidgetContents)
        AppMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.file_open = QtGui.QAction(parent=AppMainWindow)
        self.file_open.setObjectName("file_open")
        self.body_display = QtGui.QAction(parent=AppMainWindow)
        self.body_display.setObjectName("body_display")
        self.sclie_display = QtGui.QAction(parent=AppMainWindow)
        self.sclie_display.setObjectName("sclie_display")
        self.isosurface_display = QtGui.QAction(parent=AppMainWindow)
        self.isosurface_display.setObjectName("isosurface_display")
        self.menu.addAction(self.file_open)
        self.menu_2.addAction(self.body_display)
        self.menu_3.addAction(self.sclie_display)
        self.menu_4.addAction(self.isosurface_display)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(AppMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AppMainWindow)

    def retranslateUi(self, AppMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AppMainWindow.setWindowTitle(_translate("AppMainWindow", "MainWindow"))
        self.menu.setTitle(_translate("AppMainWindow", "文件"))
        self.menu_2.setTitle(_translate("AppMainWindow", "体绘制"))
        self.menu_3.setTitle(_translate("AppMainWindow", "切片显示"))
        self.menu_4.setTitle(_translate("AppMainWindow", "等值面绘制"))
        self.fileMode_groupBox.setTitle(_translate("AppMainWindow", "模型类型"))
        self.label.setText(_translate("AppMainWindow", "文件类型:"))
        self.label_3.setText(_translate("AppMainWindow", "Z维度:"))
        self.label_2.setText(_translate("AppMainWindow", "X维度:"))
        self.label_4.setText(_translate("AppMainWindow", "Y维度:"))
        self.bodyDisplay_checkBox.setText(_translate("AppMainWindow", "体绘制"))
        self.slice_checkBox.setText(_translate("AppMainWindow", "切片"))
        self.label_5.setText(_translate("AppMainWindow", "x轴:"))
        self.label_6.setText(_translate("AppMainWindow", "y轴:"))
        self.label_7.setText(_translate("AppMainWindow", "z轴:"))
        self.isosurface_checkBox.setText(_translate("AppMainWindow", "等值面"))
        self.label_8.setText(_translate("AppMainWindow", "值:"))
        self.label_9.setText(_translate("AppMainWindow", "透明度:"))
        self.fault_go_Display_checkBox.setText(_translate("AppMainWindow", "断层识别"))
        self.file_open.setText(_translate("AppMainWindow", "open"))
        self.body_display.setText(_translate("AppMainWindow", "display"))
        self.sclie_display.setText(_translate("AppMainWindow", "display"))
        self.isosurface_display.setText(_translate("AppMainWindow", "display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AppMainWindow()
    ui.setupUi(AppMainWindow)
    AppMainWindow.show()
    sys.exit(app.exec())