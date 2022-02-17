"""
Facturación
"""
from PyQt5 import QtWidgets, QtCore,QtSql
import conexion,locale,var
locale.setlocale(locale.LC_ALL, '')


class Facturas():
    def buscaCli(self):
        """

        Módulo que se ejecuta con el botón búsqueda. Devuelve datos del cliente para el panel de facturación.
        :rtype: String

        """
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
        """

        Módulo que a partir del DNI da de alta una factura con su número,fecha y DNI. Recarga la tabla facturas y busca y muestra
        en el label el número de la factura general.
        :rtype: object

        """
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
        """

        Módulo que al elegir una factura de la tabla Facturas carga sus datos en el panel de facturación.
        Los datos son : DNI del cliente,fecha factura y nombre del cliente.
        :rtype: object

        """
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
        """

        Módulo para dar de baja la factura.
        :rtype: object

        """
        try:
            codfac = var.ui.lblNumFac.text()
            conexion.Conexion.bajaFac(codfac)
            conexion.Conexion.cargaTabfacturas(self)
        except Exception as error:
            print('Error en dar de baja la factura. ', error)


    def cargaLineaVenta(index):
        """

        Módulo para cargar una línea de venta en la fila de la tabla indicada por index correspondiente a una factura dada.
        :param: index : la última línea de la tabla que carga las ventas de una factura
        :type: index : int
        :rtype: object

        """
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.currentIndexChanged.connect(Facturas.proceso_venta)
            conexion.Conexion.cargarCmbProducto(self=None)
            var.cmbProducto.setFixedSize(160, 25)
            var.txtCantidad=QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta)
            var.txtCantidad.setFixedSize(70, 25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error en cargar linea venta', error)

    def proceso_venta(self):
        """

        Módulo que carga el precio de un artículo al seleccionarlo en el combo de artículos.

        """
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
        """

        Módulo que al anotar la cantidad de producto indica el total del precio de la venta realizada.
        Al mismo tiempo recarga la tabla de líneas de venta incluyendo las anteriores y la realizada.
        :rtype: object

        """
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
            conexion.Conexion.cargarLineasVenta(codfac)
        except Exception as error:
            print('Error en total linea de venta ',error)

    def cargaCliFac(self):
        """

        Módulo para cargar datos de cliente en Facturación al seleccionar en tabla Clientes.
        :rtype: object

        """
        try:
            fila = var.ui.tabClientes.selectedItems()  # seleccionamos fila en tab clientes
            datos = [var.ui.txtDNIfac, var.ui.lblNomFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])  # cargamos los datos en las cajas de texto
            '''carga el dni y los apellidos, falta nombre'''

        except Exception as error:
            print("Error en cargar datos de un cliente en Facturación", error)