'''
Funciones gestión clientes
'''
import conexion
import eventos
import var
from window import *
from PyQt5 import QtSql,QtWidgets

class Clientes():
    def validarDNI():
        try:
            global dnivalido
            dnivalido=False
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
                    var.ui.txtDNI.setStyleSheet('background-color:white;')
                    dnivalido=True
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

    #def SelSexo(self):
        #try:
            #if var.ui.rbtFem.isChecked():
                #print('Marcado femenino. ')
            #if var.ui.rbtHom.isChecked():
                #print('Marcado masculino. ')
        #except Exception as error:
            #print('Error en módulo seleccionar sexo. ',error)

    # def SelPago(self):
    #     try:
    #         if var.ui.chkEfectivo.isChecked():
    #             print('Seleccionaste efectivo. ')
    #         if var.ui.chkTarjeta.isChecked():
    #             print('Seleccionaste tarjeta. ')
    #         if var.ui.chkCargocuenta.isChecked():
    #             print('Seleccionaste cargo en cuenta. ')
    #         if var.ui.chkTransfer.isChecked():
    #             print('Seleccionaste transferencia. ')
    #     except Exception as error:
    #         print('Error en módulo seleccionar forma de pago ',error)

    # def selProv(prov):
    #      try:
    #         print('Seleccionaste la provincia de',prov)
    #         return prov
    #      except Exception as error:
    #          print('Error en módulo seleccionar provincia',error)

    # def cargaProv_(self):
    #     try:
    #         var.ui.cmbProv.clear()
    #          prov=[""];
    #         for i in prov:
    #              var.ui.cmbProv.addItem(i)
    #
    #
    #     except Exception as error:
    #         print('Error en módulo cargar provincias,error')

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
            newcli=[]#Base de datos
            cliente=[var.ui.txtDNI, var.ui.txtAltaCli,var.ui.txtApel, var.ui.txtNome,var.ui.txtDir] #para la base de datos
            tabCli=[] #para la tableWidget
            client = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            for i in cliente:
                newcli.append(i.text())
            for i in client:
                tabCli.append(i.text())
            newcli.append(var.ui.cmbProv.currentText())
            newcli.append(var.ui.cmbMun.currentText())
          #codigo para cargar la tabla
            if var.ui.rbtHom.isChecked():
                newcli.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                newcli.append('Mujer')
            pagos=[]
            if var.ui.chkCargocuenta.isChecked():
                pagos.append('Cargo cuenta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTransfer.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            pagos=set(pagos) #evita duplicados
            newcli.append(', '.join(pagos))
            tabCli.append(', '.join(pagos))
            print(newcli)

            # cargamos en la tabla
            if dnivalido:
            #     row = 0
            #     column = 0
            #     var.ui.tabClientes.insertRow(row)
            #     for campo in tabCli:
            #         cell=QtWidgets.QTableWidgetItem(str(campo))
            #         var.ui.tabClientes.setItem(row,column,cell)
            #         column +=1
                conexion.Conexion.altaCli(newcli) #graba en la tabla de la base de datos
                conexion.Conexion.cargarTabCli(self) #recarga la tabla
            else:
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('DNI no válido')
                msg.exec()
            #codigo para grabar la base de datos
        except Exception as error:
            print('Error en guardar clientes ', error)

    def bajaCli(self):
        try:
            dni=var.ui.txtDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargarTabCli(self)
        except Exception as error:
            print('Error en dar de baja al cliente. ', error)

    def cargaCli(self):
        '''
        Carga los datos del cliente al seleccionar en tabla
        '''
        try:
            eventos.Eventos.limpiaFormCLi(self)
            fila=var.ui.tabClientes.selectedItems()
            datos=[var.ui.txtDNI,var.ui.txtApel,var.ui.txtNome,var.ui.txtAltaCli]
            if fila:
                row=[dato.text() for dato in fila]
            for i,dato in enumerate(datos):
                dato.setText(row[i]) #Cargamos en la caja de texto los datos
            #Ahora cargamos los métodos de pago
            if 'Efectivo' in row [4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in row[4]:
                var.ui.chkTransfer.setChecked(True)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Cargo' in row[4]:
                var.ui.chkCargocuenta.setChecked(True)
            #row 0 es el dni
            registro=conexion.Conexion.oneClie(row[0])
            var.ui.txtDir.setText(registro[0])
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMun.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            elif str(registro[3]) == 'Mujer':
                var.ui.rbtFem.setChecked(True)
        except Exception as error:
            print('Error en cargar datos de un cliente. ',error)



















