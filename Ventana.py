from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
import os.path
import codecs
import Lexico
import Sintax
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 600)
        MainWindow.setStyleSheet("*{background-color:#8f8f8f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        '''
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 40, 861, 301))
        self.textEdit.setStyleSheet("*{\n"
"background-color:white;\n"
"color:black;\n"
"}")'''
        self.rutaArchivo=""
        self.tipoArchivo=""'''
        self.textEdit.setObjectName("textEdit")'''
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 40, 861, 321))
        self.plainTextEdit.setStyleSheet("*{\n"
"    background-color:white;\n"
"    color:black\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.menuNuevo = QtWidgets.QMenu(self.menuArchivo)
        self.menuNuevo.setObjectName("menuNuevo")
        self.menuAnalizar = QtWidgets.QMenu(self.menubar)
        self.menuAnalizar.setStyleSheet("QMenu{\n"
"background-color:black;\n"
"color:white;\n"
"}\n"
"QMenu::item:selected{\n"
"background-color:#940000;\n"
"}")
        self.menuAnalizar.setObjectName("menuAnalizar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionInciar_Analisis = QtWidgets.QAction(MainWindow)
        self.actionInciar_Analisis.setObjectName("actionInciar_Analisis")
        self.actionArchivo_HTML = QtWidgets.QAction(MainWindow)
        self.actionArchivo_HTML.setObjectName("actionArchivo_HTML")
        self.actionArchivo_CSS = QtWidgets.QAction(MainWindow)
        self.actionArchivo_CSS.setObjectName("actionArchivo_CSS")
        self.actionArchivo_JS = QtWidgets.QAction(MainWindow)
        self.actionArchivo_JS.setObjectName("actionArchivo_JS")
        self.actionArchivo_RMT = QtWidgets.QAction(MainWindow)
        self.actionArchivo_RMT.setObjectName("actionArchivo_RMT")
        self.menuNuevo.addAction(self.actionArchivo_HTML)
        self.menuNuevo.addAction(self.actionArchivo_CSS)
        self.menuNuevo.addAction(self.actionArchivo_JS)
        self.menuNuevo.addAction(self.actionArchivo_RMT)
        self.menuArchivo.addAction(self.menuNuevo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAnalizar.addAction(self.actionInciar_Analisis)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAnalizar.menuAction())

        self.retranslateUi(MainWindow)
        self.addActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML WEB - 201800457"))
        self.label.setText(_translate("MainWindow", "Entrada:"))
        self.label_2.setText(_translate("MainWindow", "Resultado:"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuNuevo.setTitle(_translate("MainWindow", "Nuevo"))
        self.menuAnalizar.setTitle(_translate("MainWindow", "Analizar"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como..."))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionInciar_Analisis.setText(_translate("MainWindow", "Inciar Analisis"))
        self.actionArchivo_HTML.setText(_translate("MainWindow", "Archivo HTML"))
        self.actionArchivo_CSS.setText(_translate("MainWindow", "Archivo CSS"))
        self.actionArchivo_JS.setText(_translate("MainWindow", "Archivo JS"))
        self.actionArchivo_RMT.setText(_translate("MainWindow", "Archivo RMT"))
    def addActions(self):
        self.actionAbrir.triggered.connect(self.abrirArchivo)
        self.actionInciar_Analisis.triggered.connect(self.analizar)
        self.actionArchivo_HTML.triggered.connect(self.extHTML)
        self.actionArchivo_CSS.triggered.connect(self.extCSS)
        self.actionArchivo_JS.triggered.connect(self.extJS)
        self.actionArchivo_RMT.triggered.connect(self.extRMT)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardar_como.triggered.connect(self.guardarComo)
    def extHTML(self):
        self.tipoArchivo=".html"
        self.plainTextEdit.setPlainText("")
        self.textEdit_2.setText("")
        self.rutaArchivo=""
    def extCSS(self):
        self.tipoArchivo=".css"
        self.plainTextEdit.setPlainText("")
        self.textEdit_2.setText("")
        self.rutaArchivo=""
    def extJS(self):
        self.tipoArchivo=".js"
        self.plainTextEdit.setPlainText("")
        self.textEdit_2.setText("")
        self.rutaArchivo=""
    def extRMT(self):
        self.tipoArchivo=".rmt"
        self.plainTextEdit.setPlainText("")
        self.textEdit_2.setText("")
        self.rutaArchivo=""
    def guardar(self):
            if self.tipoArchivo!="":
                if self.rutaArchivo!="":
                        aGuardar=open(self.rutaArchivo,"w",encoding='utf-8')
                        aGuardar.write(self.plainTextEdit.toPlainText())
                        aGuardar.close()
                        msgBox=QMessageBox()
                        msgBox.setText("Los cambios se han guardado.")
                        msgBox.exec()
                else:
                        self.guardarComo()
            else:
                msgBox=QMessageBox()
                msgBox.setText("Debe tener un archivo abierto o crear uno nuevo para poder continuar.")
                msgBox.exec()
    def guardarComo(self):
            try:
                if self.tipoArchivo!="":
                        nuevoArchivo = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar como...',None,"Archivos HTML, CSS, JavaScript o RMT (*"+self.tipoArchivo+")")
                        file = open(nuevoArchivo[0], 'w',encoding='utf-8')
                        file.write(self.plainTextEdit.toPlainText())
                        file.close()
                        self.rutaArchivo=nuevoArchivo[0]
                else:
                        msgBox=QMessageBox()
                        msgBox.setText("Debe tener un archivo abierto o crear uno nuevo para poder continuar.")
                        msgBox.exec()
            except FileNotFoundError:
                msgBox=QMessageBox()
                msgBox.setText("No se ha seleccionado ningún archivo.")
                msgBox.exec()
    def abrirArchivo(self):
        try:
                archivo=QFileDialog.getOpenFileName(None,'Abrir Archivo',None,"Archivos HTML, CSS, JavaScript o RMT (*.html *.css *.js *.rmt)")
                print("Cargando el archivo ubicado en:"+archivo[0])
                self.rutaArchivo=archivo[0]
                archivoAbierto=open(archivo[0],"r",encoding="utf-8")
                contenido=archivoAbierto.read()
                archivoAbierto.close()
                self.plainTextEdit.setPlainText(str(contenido))
                nombre,extension=os.path.splitext(archivo[0])
                if(extension==".html"):
                        print("Se analizará un archivo HTML.")
                        self.tipoArchivo=extension
                        #self.analizar()
                elif (extension==".css"):
                        print("Se analizará un archivo CSS.")
                        self.tipoArchivo=extension
                        #self.analizar()
                elif (extension==".js"):
                        print("Se analizará un archivo JS.")
                        self.tipoArchivo=extension
                        #self.analizar()
                elif (extension==".rmt"):
                        print("Se realizará un análisis sintáctico.")
                        self.tipoArchivo=extension
                        #self.analizar()
                else:
                        self.plainTextEdit.setPlainText("")
                        msgBoxE=QMessageBox()
                        msgBoxE.setText("El formato del archivo abierto no está soportado.")
                        msgBoxE.exec()
        except FileNotFoundError:
                msgBox=QMessageBox()
                msgBox.setText("No se ha seleccionado ningún archivo.")
                msgBox.exec()
    def analizar(self):
            if self.tipoArchivo==".html": Lexico.lexHTML(self.plainTextEdit.toPlainText())
            elif self.tipoArchivo==".js": Lexico.lexJS(self.plainTextEdit.toPlainText())
            elif self.tipoArchivo==".css": self.textEdit_2.setText(Lexico.lexCSS(self.plainTextEdit.toPlainText()))
            elif self.tipoArchivo==".rmt":self.textEdit_2.setText(Sintax.sintaxParentesis(self.plainTextEdit.toPlainText()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
