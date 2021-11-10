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
        window.resize(900, 702)
        window.setSizeIncrement(QtCore.QSize(0, 0))
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
        self.lblClientes.setGeometry(QtCore.QRect(310, 0, 195, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblClientes.sizePolicy().hasHeightForWidth())
        self.lblClientes.setSizePolicy(sizePolicy)
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 811, 601))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 791, 311))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 40, 271, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblDNI = QtWidgets.QLabel(self.layoutWidget)
        self.lblDNI.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout_2.addWidget(self.lblDNI)
        spacerItem = QtWidgets.QSpacerItem(12, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.txtDNI = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDNI.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDNI.sizePolicy().hasHeightForWidth())
        self.txtDNI.setSizePolicy(sizePolicy)
        self.txtDNI.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtDNI.setFont(font)
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout_2.addWidget(self.txtDNI)
        self.lblValidoDNI = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidoDNI.sizePolicy().hasHeightForWidth())
        self.lblValidoDNI.setSizePolicy(sizePolicy)
        self.lblValidoDNI.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblValidoDNI.setFont(font)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.horizontalLayout_2.addWidget(self.lblValidoDNI)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 200, 311, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.GroupSex = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.GroupSex.setContentsMargins(0, 0, 0, 0)
        self.GroupSex.setObjectName("GroupSex")
        self.lblSexo = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.GroupSex.addWidget(self.lblSexo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GroupSex.addItem(spacerItem1)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtFem.sizePolicy().hasHeightForWidth())
        self.rbtFem.setSizePolicy(sizePolicy)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(window)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.GroupSex.addWidget(self.rbtFem)
        self.rbtHom = QtWidgets.QRadioButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtHom.sizePolicy().hasHeightForWidth())
        self.rbtHom.setSizePolicy(sizePolicy)
        self.rbtHom.setObjectName("rbtHom")
        self.rbtGroupSex.addButton(self.rbtHom)
        self.GroupSex.addWidget(self.rbtHom)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 40, 291, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblFecAlta = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFecAlta.sizePolicy().hasHeightForWidth())
        self.lblFecAlta.setSizePolicy(sizePolicy)
        self.lblFecAlta.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblFecAlta.setFont(font)
        self.lblFecAlta.setObjectName("lblFecAlta")
        self.horizontalLayout_7.addWidget(self.lblFecAlta)
        self.txtAltaCli = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAltaCli.sizePolicy().hasHeightForWidth())
        self.txtAltaCli.setSizePolicy(sizePolicy)
        self.txtAltaCli.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtAltaCli.setFont(font)
        self.txtAltaCli.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtAltaCli.setObjectName("txtAltaCli")
        self.horizontalLayout_7.addWidget(self.txtAltaCli)
        self.btnCalendar = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnCalendar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/img/calendar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/calendar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(30, 20))
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_7.addWidget(self.btnCalendar)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 80, 641, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblApel = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApel.sizePolicy().hasHeightForWidth())
        self.lblApel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtApel.sizePolicy().hasHeightForWidth())
        self.txtApel.setSizePolicy(sizePolicy)
        self.txtApel.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtApel.setFont(font)
        self.txtApel.setMaxLength(32767)
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout.addWidget(self.txtApel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lblNome = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNome.sizePolicy().hasHeightForWidth())
        self.lblNome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.horizontalLayout.addWidget(self.lblNome)
        self.txtNome = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtNome.setFont(font)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout.addWidget(self.txtNome)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(70, 120, 641, 27))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDir = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDir.sizePolicy().hasHeightForWidth())
        self.lblDir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_3.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDir.sizePolicy().hasHeightForWidth())
        self.txtDir.setSizePolicy(sizePolicy)
        self.txtDir.setSizeIncrement(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.txtDir.setFont(font)
        self.txtDir.setMaxLength(32767)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_3.addWidget(self.txtDir)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(70, 230, 698, 25))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblFormaPago = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblFormaPago.setFont(font)
        self.lblFormaPago.setObjectName("lblFormaPago")
        self.horizontalLayout_5.addWidget(self.lblFormaPago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEfectivo.sizePolicy().hasHeightForWidth())
        self.chkEfectivo.setSizePolicy(sizePolicy)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(window)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.setExclusive(False)
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_5.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTarjeta.sizePolicy().hasHeightForWidth())
        self.chkTarjeta.setSizePolicy(sizePolicy)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_5.addWidget(self.chkTarjeta)
        self.chkCargocuenta = QtWidgets.QCheckBox(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkCargocuenta.sizePolicy().hasHeightForWidth())
        self.chkCargocuenta.setSizePolicy(sizePolicy)
        self.chkCargocuenta.setObjectName("chkCargocuenta")
        self.chkGroupPago.addButton(self.chkCargocuenta)
        self.horizontalLayout_5.addWidget(self.chkCargocuenta)
        self.chkTransfer = QtWidgets.QCheckBox(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTransfer.sizePolicy().hasHeightForWidth())
        self.chkTransfer.setSizePolicy(sizePolicy)
        self.chkTransfer.setObjectName("chkTransfer")
        self.chkGroupPago.addButton(self.chkTransfer)
        self.horizontalLayout_5.addWidget(self.chkTransfer)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 20, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 781, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnRecarga = QtWidgets.QPushButton(self.groupBox)
        self.btnRecarga.setGeometry(QtCore.QRect(360, 40, 41, 31))
        self.btnRecarga.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../.designer/backup/img/recarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("img/recarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnRecarga.setIcon(icon1)
        self.btnRecarga.setObjectName("btnRecarga")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget6.setGeometry(QtCore.QRect(200, 280, 328, 29))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnGrabaCli = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnGrabaCli.setObjectName("btnGrabaCli")
        self.horizontalLayout_4.addWidget(self.btnGrabaCli)
        self.btnModifCli = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnModifCli.setObjectName("btnModifCli")
        self.horizontalLayout_4.addWidget(self.btnModifCli)
        self.btnBajaCli = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.horizontalLayout_4.addWidget(self.btnBajaCli)
        self.btnSalir = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout_4.addWidget(self.btnSalir)
        self.layoutWidget7 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget7.setGeometry(QtCore.QRect(70, 160, 641, 27))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblPro = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblPro.setFont(font)
        self.lblPro.setObjectName("lblPro")
        self.horizontalLayout_6.addWidget(self.lblPro)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget7)
        self.cmbProv.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setIconSize(QtCore.QSize(25, 16))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_6.addWidget(self.cmbProv)
        spacerItem3 = QtWidgets.QSpacerItem(48, 22, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.lblMun = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.lblMun.setFont(font)
        self.lblMun.setObjectName("lblMun")
        self.horizontalLayout_6.addWidget(self.lblMun)
        self.cmbMun = QtWidgets.QComboBox(self.layoutWidget7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMun.sizePolicy().hasHeightForWidth())
        self.cmbMun.setSizePolicy(sizePolicy)
        self.cmbMun.setIconSize(QtCore.QSize(30, 16))
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_6.addWidget(self.cmbMun)
        self.tabClientes = QtWidgets.QTableWidget(self.tab)
        self.tabClientes.setGeometry(QtCore.QRect(10, 320, 791, 251))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.tabClientes.setFont(font)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(5)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lblEnConstruccion = QtWidgets.QLabel(self.tab_2)
        self.lblEnConstruccion.setGeometry(QtCore.QRect(240, 250, 301, 16))
        self.lblEnConstruccion.setObjectName("lblEnConstruccion")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lblEnConstruccion2 = QtWidgets.QLabel(self.tab_3)
        self.lblEnConstruccion2.setGeometry(QtCore.QRect(240, 240, 281, 16))
        self.lblEnConstruccion2.setObjectName("lblEnConstruccion2")
        self.tabWidget.addTab(self.tab_3, "")
        self.lblFecha = QtWidgets.QLabel(self.centralwidget)
        self.lblFecha.setGeometry(QtCore.QRect(30, 640, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.lblFecha.setFont(font)
        self.lblFecha.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblFecha.setObjectName("lblFecha")
        self.lblHora = QtWidgets.QLabel(self.centralwidget)
        self.lblHora.setGeometry(QtCore.QRect(780, 640, 91, 16))
        self.lblHora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblHora.setObjectName("lblHora")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
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
        self.actionAbrir = QtWidgets.QAction(window)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "IMPORT-EXPORT TEIS"))
        self.lblClientes.setText(_translate("window", "IMPORT EXPORT VIGO"))
        self.groupBox.setTitle(_translate("window", "Datos personales"))
        self.lblDNI.setText(_translate("window", "DNI:       "))
        self.lblSexo.setText(_translate("window", "Sexo:"))
        self.rbtFem.setText(_translate("window", "Mujer"))
        self.rbtHom.setText(_translate("window", "Hombre"))
        self.lblFecAlta.setText(_translate("window", "Fecha de alta:"))
        self.lblApel.setText(_translate("window", "Apellidos:"))
        self.lblNome.setText(_translate("window", "Nombre:"))
        self.lblDir.setText(_translate("window", "Dirección:"))
        self.lblFormaPago.setText(_translate("window", "Formas de Pago: "))
        self.chkEfectivo.setText(_translate("window", "Efectivo"))
        self.chkTarjeta.setText(_translate("window", "Tarjeta"))
        self.chkCargocuenta.setText(_translate("window", "Cargo en cuenta"))
        self.chkTransfer.setText(_translate("window", "Transferencia"))
        self.btnGrabaCli.setText(_translate("window", "Guardar"))
        self.btnModifCli.setText(_translate("window", "Modificar"))
        self.btnBajaCli.setText(_translate("window", "Eliminar"))
        self.btnSalir.setText(_translate("window", "Salir"))
        self.lblPro.setText(_translate("window", "Provincia:"))
        self.lblMun.setText(_translate("window", "Municipio:"))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("window", "DNI"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("window", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("window", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("window", "Fecha Alta"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("window", "Formas de pago"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("window", "Clientes"))
        self.lblEnConstruccion.setText(_translate("window", "EN CONSTRUCCIÓN PANEL FACTURACIÓN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("window", "Facturación"))
        self.lblEnConstruccion2.setText(_translate("window", "EN CONSTRUCCIÓN PANEL ARTÍCULOS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("window", "Artículos"))
        self.lblFecha.setText(_translate("window", "TextLabel"))
        self.lblHora.setText(_translate("window", "TextLabel"))
        self.menuArchivo.setTitle(_translate("window", "Archivo"))
        self.actionSalir.setText(_translate("window", "Salir"))
        self.actionSalir.setShortcut(_translate("window", "Alt+S"))
        self.actionAbrir.setText(_translate("window", "Abrir"))
