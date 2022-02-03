import locale

from PyQt5 import QtSql, QtWidgets, QtCore, QtGui
from reportlab.pdfgen import canvas

import conexion
import invoice
import var
import locale

locale.setlocale(locale.LC_ALL, '')


class Conexion():
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,
                                               'No se puede abrir la base de datos. \n' 'Haz click para continuar ',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida. ')
                return True
        except Exception as error:
            print('Problemas en conexión. ', error)

    '''
    Módulos gestión de base de datos cliente
    '''

    def altaCli(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni,Alta,apellidos,nombre,direccion,provincia,municipio,sexo,pago) '
                'VALUES(:dni,:Alta,:apellidos,:nombre,:direccion,:provincia,:municipio,:sexo,:pago)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':Alta', str(newcli[1]))
            query.bindValue(':apellidos', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            # query.bindValue(':envio', int(newcli[9]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de alta')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas en alta de cliente. ', error)

    def altaPro(newpro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into articulos (codigo,nombre,precio) VALUES (:codigo,:nombre,:precio)')

            query.bindValue(':nombre', str(newpro[0]))
            query.bindValue(':precio', str(newpro[1]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Artículo dado de alta')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()


        except Exception as error:
            print('Problemas en alta de producto.', error)

    def bajaCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja cliente en conexión. ', error)

    def bajaPro(codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from articulos where codigo = :codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Artículo dado de baja')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja artículo en conexión. ', error)

    def cargarTabCli(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni,apellidos,nombre,Alta,pago,direccion from clientes order by apellidos,nombre')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    Alta = query.value(3)
                    pago = query.value(4)

                    var.ui.tabClientes.setRowCount(index + 1)  # Creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(Alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1


        except Exception as error:
            print('Problemas en mostrar tabla de cliente. ', error)

    def cargarTabPro(self):
        try:
            var.ui.tabArticulos.clear()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo,nombre,precio from articulos')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)

                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio)))
                    index += 1

        except Exception as error:
            print('Problemas en mostrar tabla de productos. ', error)

    def oneClie(dni):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select direccion,provincia,municipio,sexo from clientes where dni= :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(5):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas mostrar tablas clientes. ', error)

    # def onePro(codigo):
    #     try:
    #         record=[]
    #         query = QtSql.QSqlQuery()
    #         query.prepare('select nombre,precio from articulos where codigo= :codigo')
    #         query.bindValue(':codigo', int(codigo))
    #         if query.exec_():
    #             while query.next():
    #                 for i in range(3):
    #                     record.append(query.value(i))
    #         return record
    #     except Exception as error:
    #         print('Problemas mostrar tabla productos. ',error)
    #
    # def oneFac(codfac):
    #     try:
    #         record=[]
    #         query = QtSql.QSqlQuery()
    #         query.prepare('select dni,fechafac from articulos where codfac= :codfac')
    #         query.bindValue(':codigo', int(codfac))
    #         if query.exec_():
    #             while query.next():
    #                 for i in range(3):
    #                     record.append(query.value(i))
    #         return record
    #     except Exception as error:
    #         print('Problemas mostrar tabla facturas. ', error)

    def cargarProv(self):
        try:
            prov = [""]
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec_():
                while query.next():
                    prov.append(query.value(0))
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Problemas al mostrar provincias. ', error)

    def cargarMuni(self):
        try:
            id = 0
            var.ui.cmbMun.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select id from provincias where provincia = :prov')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where provincia_id = :id')
            query1.bindValue(':id', int(id))
            if query1.exec_():
                var.ui.cmbMun.addItem('')
                while query1.next():
                    var.ui.cmbMun.addItem(query1.value(0))
        except Exception as error:
            print('Problemas al mostrar municipios. ', error)

    def modifCli(modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'UPDATE clientes SET Alta = :Alta,apellidos = :apellidos,nombre = :nombre,direccion = :direccion,provincia= :provincia,municipio = :municipio, sexo = :sexo,pago = :pago where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':Alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))

            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de cliente')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas modificar clientes. ', error)

    def modifPro(modproducto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre = :nombre, precio = :precio where codigo = :codigo')
            query.bindValue(':codigo', int(modproducto[0]))
            query.bindValue(':nombre', str(modproducto[1]))
            modproducto[2] = modproducto[2].replace('€', '')
            modproducto[2] = modproducto[2].replace(',', '.')
            modproducto[2] = float(modproducto[2])
            modproducto[2] = round(modproducto[2], 2)
            modproducto[2] = str(modproducto[2])
            modproducto[2] = locale.currency(float(modproducto[2]))
            query.bindValue(':precio', str(modproducto[2]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de Producto')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error modificar producto en conexion: ', error)
        # try:
        #     query = QtSql.QSqlQuery()
        #     query.prepare('UPDATE articulos set nombre = :nombre, precio = :precio where codigo= :codigo')
        #     query.bindValue(':nombre', str(modproducto[1]))
        #     query.bindValue(':precio', str(modproducto[1]))
        #     if query.exec_():
        #         print('Inserción correcta. ')
        #         msg = QtWidgets.QMessageBox()
        #         msg.setWindowTitle('Información')
        #         msg.setIcon(QtWidgets.QMessageBox.Information)
        #         msg.setText('Datos modificados de artículo')
        #         msg.exec()
        #     else:
        #         print('Error. ', query.lastError().text())
        #         msg = QtWidgets.QMessageBox()
        #         msg.setWindowTitle('Aviso')
        #         msg.setIcon(QtWidgets.QMessageBox.Warning)
        #         msg.setText(query.lastError().text())
        #         msg.exec()
        # except Exception as error:
        #     print('Problemas modificar artículos. ', error)

    """
    Gestión Facturación
    """

    def buscaClifac(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select dni,apellidos,nombre from clientes where dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    registro.append(query.value(1))
                    registro.append(query.value(2))
            return registro
        except Exception as error:
            print('Error en conexión buscar cliente. ', error)

    def altaFac(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (dni,fechafac) VALUES (:dni,:fecha)')
            query.bindValue(':dni', str(registro[0]))
            query.bindValue(':fecha', str(registro[1]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de alta.')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en conexión alta factura. ', error)

    def cargaTabfacturas(self):
        try:
            var.ui.tabFacturas.clear()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfac,fechafac from facturas order by fechafac DESC')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    icopapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(24, 24)
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))
                    var.ui.tabFacturas.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.setContentsMargins(0, 0, 0, 0)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(invoice.Facturas.bajaFac)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tabFacturas.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print('Error al cargar listado facturas. ', error)

    def buscaDNIFac(numfac):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT dni from facturas where codfac =:numfac')
            query.bindValue(':numfac', int(numfac))
            if query.exec_():
                while query.next():
                    dni = query.value(0)
            return dni
        except Exception as error:
            print('Error al buscar dni', error)

    def bajaFac(codfac):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de baja')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error al dar de baja factura ', error)

    def cargarCmbProducto(self):
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')
            query.prepare('select nombre from articulos order by nombre')
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))
        except Exception as error:
            print('Error al cargar cmbProducto ', error)

    def obtenerCodPrecio(articulo):
        try:
            dato = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo,precio from articulos where nombre=:nombre')
            query.bindValue(':nombre', str(articulo))
            if query.exec_():
                while query.next():
                    dato.append(int(query.value(0)))
                    dato.append(str(query.value(1)))
            return dato
        except Exception as error:
            print('Error al cargar codigo precio en conexion ', error)

    def cargarVenta(venta):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into ventas(codfac,codpro,precio,cantidad) values(:codfac,:codpro,:precio,:cantidad)')
            query.bindValue(':codfac', int(venta[0]))
            query.bindValue(':codpro', int(venta[1]))
            query.bindValue(':cantidad', float(venta[2]))
            query.bindValue(':precio', float(venta[3]))
            if query.exec_():
                var.ui.lblVenta.setStyleSheet("QLabel{color: green}")
                var.ui.lblVenta.setText('Venta realizada.')
            else:
                var.ui.lblVenta.setStyleSheet("QLabel{color: red}")
                var.ui.lblVenta.setText('Error en venta.')
        except Exception as error:
            print('error al cargar venta ', error)

    def buscaCodfac(self):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codfac from facturas order by codfac desc limit 1')
            if query.exec_():
                while query.next():
                    dato = query.value(0)
            return dato
        except Exception as error:
            print('Error obtener codigo factura', error)

    def buscarArt(codigo):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('select nombre from articulos where codigo= :codpro')
            query.bindValue(':codpro',int(codigo))
            if query.exec_():
                while query.next():
                    return(query.value(0))
        except Exception as error:
            print('Error al buscar articulo ',error)

    def cargarLineasVenta(codfac):
        try:
            suma=0.0
            var.ui.tabVentas.clearContents()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codven,precio,cantidad,codpro from ventas where codfac= :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codven = query.value(0)
                    precio = str(query.value(1))
                    cantidad = query.value(2)
                    total_venta = round(float(precio) * float(cantidad), 2)
                    articulo=Conexion.buscarArt(int(query.value(3)))
                    suma= suma+(round(float(precio) * float(cantidad), 2))
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codven)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(articulo)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio) + ' €'))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tabVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(total_venta) + ' €'))
                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 4).setTextAlignment(QtCore.Qt.AlignRight)
                    index = index + 1
            iva=suma * 0.21
            total=suma+iva
            var.ui.lblSubtotal.setText(str(round(suma,2))+' €')
            var.ui.lblIva.setText(str(round(iva,2))+' €')
            var.ui.lblTotal.setText(str(round(total,2))+' €')
            invoice.Facturas.cargaLineaVenta(index)
            var.ui.tabVentas.scrollToBottom()
        except Exception as error:
            print('Error en cargar linea de venta', error)

    def eliminarVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            codventa = var.ui.tabVentas.item(row, 0).text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codven = :codven')
            query.bindValue(':codven', int(codventa))
            if query.exec_():
                msg1 = QtWidgets.QMessageBox()
                msg1.setWindowTitle('Aviso')
                msg1.setIcon(QtWidgets.QMessageBox.Information)
                msg1.setText('Venta eliminada')
                msg1.exec()
                codfac = var.ui.lblNumFac.text()
                Conexion.cargarLineasVenta(codfac)
        except Exception as error:
            print('Error en eliminar venta ',error)

