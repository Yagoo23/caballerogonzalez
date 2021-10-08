'''
Funciones gestión clientes
'''
import var
from window import *

class Clientes():
    def validarDNI():
        try:
            dni=var.ui.txtDNI.text()
            var.ui.txtDNI.setText(dni.upper())
            tabla='TRWAGMYFPDXBNJZSQVHLCKE' #Letras DNI
            dig_ext='XYZ' #Dígitos extranjero
            reemp_dig_ext={ 'X': '0','Y': '1','Z':'2'}
            numeros = '1234567890'
            dni= dni.upper() #Convertir la letra en mayúscula
            if len(dni)==9:
                dig_control=dni[8]
                dni=dni[:8]
                if dni[0] in dig_ext:
                    dni=dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni)==len([n for n in dni if n in numeros]) and tabla[int(dni)%23]== dig_control:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color:green;}')
                    var.ui.lblValidoDNI.setText('V')

                else:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValidoDNI.setText('X')
                    var.ui.txtDNI.setStyleSheet('background-color:pink;')
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel {color:red;}')
                var.ui.lblValidoDNI.setText('X')
                var.ui.txtDNI.setStyleSheet('background-color:pink;')

        except Exception as error:
            print('Error en módulo validar DNI',error)

    def SelSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado femenino. ')
            if var.ui.rbtHom.isChecked():
                print('Marcado masculino. ')
        except Exception as error:
            print('Error en módulo seleccionar sexo. ',error)

    def SelPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Seleccionaste efectivo. ')
            if var.ui.chkTarjeta.isChecked():
                print('Seleccionaste tarjeta. ')
            if var.ui.chkCargocuenta.isChecked():
                print('Seleccionaste cargo en cuenta. ')
            if var.ui.chkTransfer.isChecked():
                print('Seleccionaste transferencia. ')
        except Exception as error:
            print('Error en módulo seleccionar forma de pago ',error)


























