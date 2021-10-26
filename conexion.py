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
    #def altaCli(selfnewcli):
        #try:

        #except Exception as error:
            #print('Problemas en alta de cliente. ',error)
