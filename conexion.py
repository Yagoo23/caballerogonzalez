from PyQt5 import QtSql, QtWidgets

import var


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
            query.bindValue(':envio', int(newcli[9]))
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

    def bajaPro(nombre):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from articulos where nombre = :nombre')
            query.bindValue(':nombre', str(nombre))
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
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select nombre,precio from articulos')
            if query.exec_():
                while query.next():
                    nombre = query.value(0)
                    precio = query.value(1)

                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(precio))
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
            query.prepare('UPDATE articulos set nombre = :nombre, precio = :precio where nombre= :nombre')
            query.bindValue(':nombre', str(modproducto[0]))
            query.bindValue(':precio', str(modproducto[1]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de artículo')
                msg.exec()
            else:
                print('Error. ', query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Problemas modificar artículos. ', error)


    """
    Gestión Facturación
    """

    def buscaClifac(dni):
        try:
            registro=[]
            query=QtSql.QSqlQuery()
            query.prepare('select dni,apellidos,nombre from clientes where dni =:dni')
            query.bindValue(':dni',str(dni))
            if query.exec_():
                while query.next():
                    registro.append(query.value(1))
                    registro.append(query.value(2))
            return registro
        except Exception as error:
            print('Error en conexión buscar cliente. ',error)


























