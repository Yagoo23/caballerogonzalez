# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowcal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowcal(object):
    def setupUi(self, windowcal):
        """

        Código obtenido a partir del fichero xml generado por QtDesigner correspondiente a la interfaz gráfica de calendario.
        :param: windowcal: interfaz gráfica
        :type: windowcal: object

        """
        windowcal.setObjectName("windowcal")
        windowcal.setWindowModality(QtCore.Qt.WindowModal)
        windowcal.setEnabled(True)
        windowcal.resize(315, 182)
        windowcal.setModal(False)
        self.Calendar = QtWidgets.QCalendarWidget(windowcal)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 312, 183))
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(windowcal)
        QtCore.QMetaObject.connectSlotsByName(windowcal)

    def retranslateUi(self, windowcal):
        _translate = QtCore.QCoreApplication.translate
        windowcal.setWindowTitle(_translate("windowcal", "Pulse fecha"))
