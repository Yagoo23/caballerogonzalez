from PyQt5 import QtSql,QtWidgets

import var



class Conexion():
    def db_connect(filedb):
        try:
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,'No se puede abrir la base de datos. \n' 'Haz click para continuar ',QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida. ')
                return True
        except Exception as error:
            print('Problemas en conexión. ',error)
    '''
    Módulos gestión de base de datos cliente
    '''
    def altaCli(newcli):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni,Alta,apellidos,nombre,direccion,provincia,municipio,sexo,pago) '
                          'VALUES(:dni,:Alta,:apellidos,:nombre,:direccion,:provincia,:municipio,:sexo,:pago)')
            query.bindValue(':dni',str(newcli[0]))
            query.bindValue(':Alta', str(newcli[1]))
            query.bindValue(':apellidos',str(newcli[2]))
            query.bindValue(':nombre',str(newcli[3]))
            query.bindValue(':direccion', str(newcli[4]))
            query.bindValue(':provincia', str(newcli[5]))
            query.bindValue(':municipio', str(newcli[6]))
            query.bindValue(':sexo', str(newcli[7]))
            query.bindValue(':pago', str(newcli[8]))
            if query.exec_():
                print('Inserción correcta. ')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Inserción correcta')
                msg.exec()
            else:
                print('Error. ',query.lastError().text())
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Problemas en alta de cliente. ',error)

    def cargarTabCli(self):
        try:
            index=0
            query=QtSql.QSqlQuery()
            query.prepare('select dni,apellidos,nombre,Alta,pago,direccion from clientes')
            if query.exec_():
                while query.next():
                    dni=query.value(0)
                    apellidos=query.value(1)
                    nombre=query.value(2)
                    Alta = query.value(3)
                    pago=query.value(4)

                    var.ui.tabClientes.setRowCount(index+1) #Creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(Alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index+=1


        except Exception as error:
            print('Problemas en mostrar tabla de cliente. ', error)

    def oneClie(dni):
        try:
            direccion='a'
            query=QtSql.QSqlQuery()
            query.prepare('select direccion,provincia,municipio,sexo from clientes where dni= :dni')
            query.bindValue(':dni',dni)
            if query.exec_():
                while query.next():
                    direccion=query.value(0)
            print(direccion)
        except Exception as error:
            print('Problemas en mostrar otros datos. ', error)