'''
Fichero de eventos generales
'''
import os.path,sys,zipfile,shutil,conexion,var
from window import *
from datetime import *
from PyQt5 import QtPrintSupport


class Eventos():
    def Abrir(self):
        """

        Abre una nueva pestaña para ver o abrir documentos.
        :rtype: object

        """
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir cuadro de diálogo', error)

    def Salir(self):
        """

        Módulo para salir del programa.
        :rtype: object

        """
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en módulo salir ', error)

    def abrircal(self):
        """

        Módulo para abrir el Dialog Calendar.
        :rtype: object

        """
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario ', error)

    def ResizeTabClientes(self):
        """

        Módulo para redimensionar la tabla Clientes.


        """
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al redimensionar la tabla Clientes. ', error)

    def ResizeTabFacturas(self):
        """

        Módulo para redimensionar la tabla Facturas.

        """
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        except Exception as error:
            print('Error al redimensionar la tabla facturas.', error)

    def ResizeTabVentas(self):
        """

        Módulo para redimensionar la tabla Ventas.

        """
        try:
            header = var.ui.tabVentas.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al redimensionar la tabla facturas. ', error)

    def ResizeTabArticulos(self):
        """

        Módulo para redimensionar la tabla Artículos.

        """
        try:
            header = var.ui.tabArticulos.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al redimensionar la tabla facturas. ', error)

    def limpiaFormCLi(self):
        """

        Módulo para limpiar el panel de Clientes y que aparezca vacío.
        :rtype: object

        """
        try:
            cajas = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli, var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransfer.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargocuenta.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMun.setCurrentIndex(0)
        except Exception as error:
            print('Error en limpiar clientes ', error)

    def limpiaFormPro(self):
        """

        Módulo para limpiar el panel de Productos y que aparezca vacío.
        :rtype: object

        """
        try:
            cajas=[var.ui.lblCod,var.ui.txtNombre,var.ui.txtPrecio]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error en limpiar artículos ', error)


    def crearBackup(self):
        """

        Módulo para crear un backup.
        :rtype: object

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar copia', var.copia, '.zip',
                                                                options=option)
            if (var.dlgabrir.Accepted and filename != ''):
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Información')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Copia de seguridad creada.')
                msg.exec()
        except Exception as error:
            print('Error en crear Backup ', error)

    def restaurarBD(self):
        """

        Módulo para restaurar la base de datos.
        :rtype: object

        """
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridad', '', '*.zip', options=option)
            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli(self)
            conexion.Conexion.cargarProv(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Información')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Copia de seguridad restaurada.')
            msg.exec()
        except Exception as error:
            print('Error en restaurar base de datos ', error)

    def Imprimir(self):
        """

        Módulo para abrir la ventana de imprimir.
        :rtype: object

        """
        try:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec():
                printDialog.show()
        except Exception as error:
            print('Error al imprimir. ', error)

