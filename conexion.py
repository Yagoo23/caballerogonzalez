from PyQt5 import QtSql, QtWidgets, QtCore, QtGui
import sqlite3, invoice, var, locale, os, csv

locale.setlocale(locale.LC_ALL, '')


class Conexion():
    def create_BD(filename):
        """

        Recibe el nombre de la base de datos.
        Módulo que se ejecuta al principio del programa.
        Crea las tablas y carga municipios y provincias.
        Crea los directorios necesarios.
        :rtype: Object

        """
        try:
            con = sqlite3.connect(database=filename)
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS clientes (dni TEXT NOT NULL,alta TEXT,apellidos	TEXT NOT NULL,'
                        ' nombre TEXT,direccion TEXT,provincia TEXT,municipio TEXT,sexo TEXT,pago TEXT,'
                        ' envio INTEGER,PRIMARY KEY(dni))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS ventas(codven INTEGER NOT NULL,'
                        ' codfac INTEGER NOT NULL,codpro INTEGER NOT NULL,'
                        ' precio REAL NOT NULL,cantidad REAL NOT NULL,PRIMARY KEY(codven AUTOINCREMENT),'
                        ' FOREIGN KEY(codpro) REFERENCES articulos(codigo),'
                        ' FOREIGN KEY(codfac) REFERENCES facturas(codfac))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS articulos (codigo INTEGER NOT NULL,'
                        ' nombre TEXT NOT NULL,precio REAL,PRIMARY KEY(codigo AUTOINCREMENT))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS facturas (codfac INTEGER NOT NULL,dni TEXT,'
                        ' fechafac	TEXT,PRIMARY KEY(codfac AUTOINCREMENT))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS provincias (id	INTEGER NOT NULL,'
                        ' provincia VARCHAR(255) NOT NULL,PRIMARY KEY(id))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS municipios (provincia_id INTEGER NOT NULL,'
                        ' municipio	VARCHAR(255) NOT NULL,id INTEGER NOT NULL,PRIMARY KEY(id))')
            con.commit()
            cur.execute('select count() from provincias')
            numero = cur.fetchone()[0]
            print(numero)
            con.commit()
            if int(numero) == 0:
                print('entró')
                with open('provincias.csv', 'r', encoding="utf-8") as fin:
                    dr = csv.DictReader(fin)
                    to_db = [(i['id'], i['provincia']) for i in dr]
                cur.executemany('insert into provincias (id, provincia) VALUES (?,?);', to_db)
                con.commit()
            con.close()

            '''creación de directorios'''

            if not os.path.exists('.\\informes'):
                os.mkdir('.\\informes')
            if not os.path.exists('.\\img'):
                os.mkdir('.\\img')
            #     shutil.
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('error', error)
            msg.exec()

    def existeDNI(dni):
        try:
            # signal=True
            # query=QtSql.QSqlQuery()
            # query.prepare('select dni from clientes')
            pass
        except Exception as error:
            print('Problemas con DNI repetido', error)

    def db_connect(filedb):
        """

        Realiza la conexión con la base de datos al ejecutar el programa.
        :return: Boolean, True si es correcto,False si hay un error
        :rtype: Boolean

        """
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

    def altaCli(newcli):
        """

        Módulo que da de alta a los clientes.
        :rtype: object

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni,Alta,apellidos,nombre,direccion,provincia,municipio,sexo,pago,envio) '
                'VALUES(:dni,:Alta,:apellidos,:nombre,:direccion,:provincia,:municipio,:sexo,:pago,:envio)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':Alta', str(newcli[1]))
            query.bindValue(':apellidos', str(newcli[2]))
            query.bindValue(':nombre', str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            query.bindValue(':envio', str(newcli[9]))
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
        """

        Módulo que recibe datos del producto y los carga en la base de datos.
        :rtype: object

        """
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
        """

        Módulo que recibe el dni del cliente y lo da de baja de la base de datos.
        :rtype: object

        """
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
        """

        Módulo que recibe el código de un producto y lo elimina de la base de datos.
        :rtype: object

        """
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
        """

        Módulo que toma datos de los clientes y los carga en la tabla de la interfaz gráfica.
        :rtype: object

        """
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
        """

        Módulo que recarga la tabla del panel de productos siempre que se dé de alta,baja o modificar un producto.
        :rtype: object

        """
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
        """

        Módulo que selecciona un cliente según su DNI y lo devuelve a la función CargaCli del fichero cliente.
        :return: Devuelve una lista
        :rtype: object - lista

        """
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('select direccion,provincia,municipio,sexo,envio from clientes where dni= :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(6):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas mostrar tablas clientes. ', error)

    def cargarProv(self):
        """

        Módulo que carga las provincias en el combo de la interfaz gráfica del panel Clientes.
        :rtype: object

        """
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
        """

        Módulo que selecciona los municipios dada una provincia y los carga en el combo municipios del panel Clientes.
        :rtype: object

        """
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
        """

        Módulo que recibe los cambios del cliente a modificar y lo modifica en la base de datos.
        :rtype: object

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'UPDATE clientes SET Alta = :Alta,apellidos = :apellidos,nombre = :nombre,direccion = :direccion,provincia= :provincia,municipio = :municipio, sexo = :sexo,pago = :pago,envio = :envio where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':Alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            query.bindValue(':envio',str(modcliente[9]))

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
        """

        Módulo que recibe el código de un producto y lo modifica en la base de datos.
        :rtype: object

        """
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

    def buscaClifac(dni):
        """

        Módulo que busca los datos del cliente a facturar a partir de su DNI.
        :return: Devuelve datos del cliente a facturar.
        :rtype: object

        """
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
        """

        Dado el cliente a facturar se dá de alta una factura en la base de datos a nombre de ese cliente(DNI).
        :rtype: object

        """
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
        """

        Módulo que se ejecuta cada vez que se dá de alta,baja o modifica una factura recargando en el panel
        de gestión de facturación de la tabla facturas.
        :rtype: object

        """
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
        """

        Módulo que busca el DNI de la tabla facturas en la base de datos.
        :return: Devuelve un DNI
        :rtype: String

        """
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
        """

        Módulo que dado el código de la factura dará de baja. Además llama al módulo borrar ventas para que elimine
        todas las ventas asociadas a esa factura de la tabla ventas de la base de datos.
        :rtype: object

        """
        try:
            numfac = var.ui.lblNumFac.text()
            Conexion.delVentaFac(numfac)
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
        """

        Módulo que toma los datos de los nombre de los productos existentes de la base de datos y los carga
        en el panel de facturación de la tabla ventas.
        :rtype: object

        """
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
        """

        Módulo que dado el nombre del producto obtenemos su precio para realizar los cálculos necesarios en la venta.
        :return: Devuelve el precio
        :rtype: object - Array

        """
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
        """

        Módulo que carga el registro de una venta realizada en la tabla ventas de la base de datos.
        :rtype: object

        """
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
        """

        Módulo que selecciona el código de la factura con número más alto o la última en dar de alta.
        :return: Devuelve el número/código factura
        :rtype: Int

        """
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
        """

        Módulo que busca el nombre de un artículo para usarlo en las ventas a partir de su código.
        :return: Devuelve el nombre del artículo
        :rtype: String

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from articulos where codigo= :codpro')
            query.bindValue(':codpro', int(codigo))
            if query.exec_():
                while query.next():
                    return (query.value(0))
        except Exception as error:
            print('Error al buscar articulo ', error)

    def cargarLineasVenta(codfac):
        """

        Módulo que carga todos las ventas asociadas a una factura en la tabla ventas del panel de facturación.
        Además realiza los cálculos necesarios para el subtotal,total e iva de la factura.
        Este módulo se le llama cada vez que se realiza una venta.
        :rtype: object

        """
        try:
            suma = 0.0
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
                    articulo = Conexion.buscarArt(int(query.value(3)))
                    suma = suma + (round(float(precio) * float(cantidad), 2))
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
            iva = suma * 0.21
            total = suma + iva
            var.ui.lblSubtotal.setText(str(round(suma, 2)) + ' €')
            var.ui.lblIva.setText(str(round(iva, 2)) + ' €')
            var.ui.lblTotal.setText(str(round(total, 2)) + ' €')
            invoice.Facturas.cargaLineaVenta(index)
            var.ui.tabVentas.scrollToBottom()
        except Exception as error:
            print('Error en cargar linea de venta', error)

    def eliminarVenta(self):
        """

        Módulo que elimina una venta de una factura.
        :rtype: object

        """
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
            print('Error en eliminar venta ', error)

    def delVentaFac(numfac):
        """

        :param: numfac valor de la factura
        :type: numfac: int
        Módulo que se llama cuándo se dá de baja una factura en la base de datos para que elimine todas las ventas asociadas a esa factura.
        Recibe el número de factura a borrar.A partir de ese código, primero selecciona todos los códigos de venta asociados a la factura
        y los guarda en una lista. A continuación a medida que recorre esa lista leyendo los códigos de venta los dá de baja de la tabla
        ventas de la base de datos. Finalmente, recarga la tabla de ventas del panel de facturación y limpia datos.

        """
        try:
            ventas = []
            query = QtSql.QSqlQuery()
            query.prepare('select codven from ventas where codfac = :numfac')
            query.bindValue(':numfac', int(numfac))
            if query.exec_():
                while query.next():
                    ventas.append(query.value(0))
            for dato in ventas:
                query1 = QtSql.QSqlQuery()
                query1.prepare('delete from ventas where codven = :dato')
                query1.bindValue(':dato', int(dato))
                if query1.exec_():
                    pass
                var.ui.tabVentas.clearContents()
                invoice.Facturas.cargaLineaVenta(0)
                var.ui.lblIva.setText('')
                var.ui.lblSubtotal.setText('')
                var.ui.lblTotal.setText('')
        except Exception as error:
            print('Error en eliminar lineas de venta en delVenFac ', error)

    def buscaArt(self):
        try:
            nomart = var.ui.txtNombre.text().title()
            query = QtSql.QSqlQuery()
            index = 0
            query.prepare('SELECT codigo,nombre,precio FROM articulos WHERE nombre=:nombre ORDER BY codigo')
            query.bindValue(':nombre', str(nomart))
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)

                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))

                    index += 1
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("El articulo no ha sido encontrado en la BD")
                msgBox.exec()
        except Exception as error:
            print('Problemas buscar articulo ', error)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setIcon((QtWidgets.QMessageBox.Warning))
            msgBox.setText("Error al buscar articulo")
            msgBox.exec()
