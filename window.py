# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        window.setFont(font)
        window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(300, 30, 191, 20))
        font = QtGui.QFont()
        font.setFamily("13 Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblClientes.setFont(font)
        self.lblClientes.setStyleSheet("QLabel{\n"
"font: 75 14pt bold \"Calibri\";\n"
"background-color:\'blue\';\n"
"color:\'white\';\n"
"border:3px,solid,white;\n"
"align:center;\n"
"background:qlineargradient(spread:pad, x1:0.443, y1:0.0170455, x2:0.472, y2:1, stop:0 rgba(10, 62, 194, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.lblClientes.setObjectName("lblClientes")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(70, 150, 51, 31))
        self.lblDNI.setObjectName("lblDNI")
        self.lineEditDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDNI.setGeometry(QtCore.QRect(130, 160, 120, 20))
        self.lineEditDNI.setObjectName("lineEditDNI")
        self.lblValidoDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblValidoDNI.setGeometry(QtCore.QRect(270, 150, 121, 31))
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(410, 440, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(510, 440, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionSalir.setFont(font)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "IMPORT-EXPORT TEIS"))
        self.lblClientes.setText(_translate("window", "XESTIÓN CLIENTES"))
        self.lblDNI.setText(_translate("window", "DNI:"))
        self.lblValidoDNI.setText(_translate("window", "Valida DNI"))
        self.btnAceptar.setText(_translate("window", "Aceptar"))
        self.btnSalir.setText(_translate("window", "Salir"))
        self.menuArchivo.setTitle(_translate("window", "Archivo"))
        self.actionSalir.setText(_translate("window", "Salir"))
        self.actionSalir.setShortcut(_translate("window", "Alt+S"))
