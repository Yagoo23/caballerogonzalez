"""
Facturación
"""
from PyQt5 import QtWidgets, QtCore,QtSql
import conexion
import locale
import var
locale.setlocale(locale.LC_ALL, '')


class Facturas():
    def buscaCli(self):
        try:
            dni = var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ',' + registro[1]
                var.ui.lblNomFac.setText(nombre)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.exec()
            # var.ui.txtClienteFac.setText(nombre)
        except Exception as error:
            print('Error al buscar cliente en facturas. ', error)

    def facturar(self):
        try:
            registro = []
            dni = var.ui.txtDNIfac.text().upper()
            registro.append(str(dni))
            var.ui.txtDNIfac.setText(dni)
            fechafac = var.ui.txtFechaFac.text()
            registro.append(str(fechafac))
            conexion.Conexion.buscaClifac(dni)
            conexion.Conexion.altaFac(registro)
            conexion.Conexion.cargaTabfacturas(self)
            codfac=conexion.Conexion.buscaCodfac(self)
            var.ui.lblNumFac.setText(str(codfac))
        except Exception as error:
            print('Error en alta facturas. ', error)

    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblNumFac, var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            # Aquí cargamos el dni y nombre del cliente
            dni = conexion.Conexion.buscaDNIFac(row[0])
            var.ui.txtDNIfac.setText(str(dni))
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ',' + registro[1]
                var.ui.lblNomFac.setText(nombre)
            conexion.Conexion.cargarLineasVenta(str(var.ui.lblNumFac.text()))
        except Exception as error:
            print('Error al cargar factura. ', error)

    def bajaFac(self):
        try:
            codfac = var.ui.lblNumFac.text()
            conexion.Conexion.bajaFac(codfac)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('Error en dar de baja al artículo. ', error)

    def prepararTabFac(self):
        try:
            pass
        except Exception as error:
            print('Error en preparar TabFac', error)

    def cargaLineaVenta(self):
        try:
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(160, 25)
            conexion.Conexion.cargarCmbProducto(self)
            var.txtCantidad.setFixedSize(70, 25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error en cargar linea venta', error)

    def proceso_venta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            var.codpro=dato[0]
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            precio=dato[1].replace('€','')
            var.precio=precio.replace(',','.')
        except Exception as error:
            print('Error en proceso venta,', error)

    def totalLineaVenta(self = None):
        try:
            venta=[]
            row=var.ui.tabVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total_linea = round(float(var.precio) * float(cantidad), 2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_linea) + ' € '))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            codfac=var.ui.lblNumFac.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(cantidad))
            venta.append(float(var.precio))
            conexion.Conexion.cargarVenta(venta)
        except Exception as error:
            print('Error en total linea de venta ',error)













