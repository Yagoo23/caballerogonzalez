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


    def cargaProv_(self):
        try:
            var.ui.cmbProv.clear()
            prov=['','A Coruña','Lugo','Ourense','Pontevedra','Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)


        except Exception as error:
            print('Error en módulo cargar provincias,error')

    def selProv(prov):
        try:
            print('Seleccionaste la provincia de',prov)
            return prov
        except Exception as error:
            print('Error en módulo seleccionar provincia',error)

    def cargarFecha(qDate):
        try:
            data= ('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtAltaCli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha ',error)

    def letracapital():
        try:
            nome = var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.title())
            apelido = var.ui.txtApel.text()
            var.ui.txtApel.setText(apelido.title())
            direccion = var.ui.txtDir.text()
            var.ui.txtDir.setText(direccion.title())

        except Exception as error:
            print('Error en módulo dirección ', error)

    def guardaCli(self):
        try:
            #preparamos el registro
            newcli=[]
            client =[var.ui.txtApel,var.ui.txtNome,var.ui.txtAltaCli]
            for i in client:
                newcli.append(i.text())
            #cargamos en la tabla
            row=0
            column=0
            var.ui.tabClientes.insertRow(row)
            for campo in newcli:
                cell=QtWidgets.QTableWidgetItem(campo)
                var.ui.tabClientes.setItem(row,column,cell)
                column +=1
        except Exception as error:
            print('Error en guardar clientes ', error)

    def limpiaFormCLi(self):
        try:
            cajas=[var.ui.txtDNI,var.ui.txtApel,var.ui.txtNome,var.ui.txtAltaCli,var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransfer.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargocuenta.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMun.setCurrentIndex(0)
        except Exception as error:
            print('Error en limpiar clientes ',error)




















