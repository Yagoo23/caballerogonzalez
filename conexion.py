from PyQt5 import QtSql,QtWidgets

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
