# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 600)
        MainWindow.setStyleSheet("*{background-color:#8f8f8f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 40, 861, 301))
        self.textEdit.setStyleSheet("*{\n"
"background-color:white;\n"
"color:black;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 390, 861, 161))
        self.textEdit_2.setMouseTracking(True)
        self.textEdit_2.setStyleSheet("*{\n"
"    background-color:rgb(0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 370, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 21))
        self.menubar.setStyleSheet("QMenuBar{background-color:black;\n"
"color:white;\n"
"}\n"
"QMenuBar::item:selected{background-color:#940000;}\n"
"QMenuBar::item:pressed{background-color:#b00000;}")
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setStyleSheet("QMenu{\n"
"background-color:black;\n"
"color:white;\n"
"}\n"
"QMenu::item:selected{\n"
"background-color:#940000;\n"
"}")
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAnalizar = QtWidgets.QMenu(self.menubar)
        self.menuAnalizar.setObjectName("menuAnalizar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAnalizar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML WEB - 201800457"))
        self.label.setText(_translate("MainWindow", "Entrada:"))
        self.label_2.setText(_translate("MainWindow", "Resultado:"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAnalizar.setTitle(_translate("MainWindow", "Analizar"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como..."))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
