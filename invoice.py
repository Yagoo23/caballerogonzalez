"""
Facturación
"""
from PyQt5 import QtWidgets

import conexion
import invoice
import var
import window

class Facturas():
    def buscaCli(self):
        try:
            dni=var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro=conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre=registro[0] + ','+registro[1]
                var.ui.lblNomFac.setText(nombre)
            else:
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec()
            #var.ui.txtClienteFac.setText(nombre)
        except Exception as error:
            print('Error al buscar cliente en facturas. ',error)

    def facturar(self):
        try:
            registro=[]
            dni=var.ui.txtDNIfac.text().upper()
            registro.append(str(dni))
            var.ui.txtDNIfac.setText(dni)
            fechafac=var.ui.txtFechaFac.text()
            registro.append(str(fechafac))
            conexion.Conexion.buscaClifac(dni)
            conexion.Conexion.altaFac(registro)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('Error en alta facturas. ',error)

    def cargaFac(self):
        try:
            fila=var.ui.tabFacturas.selectedItems()
            datos=[var.ui.lblNumFac,var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            #Aquí cargamos el dni y nombre del cliente
            dni=conexion.Conexion.buscaDNIFac(row[0])
            var.ui.txtDNIfac.setText(str(dni))
            registro=conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ',' + registro[1]
                var.ui.lblNomFac.setText(nombre)
        except Exception as error:
            print('Error al cargar factura. ',error)

    def bajaFac(self):
        try:
            codfac = var.ui.lblNumFac.text()
            print(codfac)
            conexion.Conexion.bajaFac(codfac)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('Error en dar de baja al artículo. ', error)