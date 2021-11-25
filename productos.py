import conexion
import eventos
import var
from PyQt5 import QtSql, QtWidgets


class Productos():

    def guardaPro(self):
        try:
            newpro=[]
            producto=[var.ui.txtNombre, var.ui.txtPrecio]
            tabPro=[]
            product=[var.ui.txtNombre, var.ui.txtPrecio]
            for i in producto:
                newpro.append(i.text())
            for i in product:
                tabPro.append(i.text())
            conexion.Conexion.altaPro(newpro)
            conexion.Conexion.cargarTabPro(self)

        except Exception as error:
            print('Error en guardar artículo ', error)

    def cargaPro(self):
        try:
            eventos.Eventos.limpiaFormPro(self)
            fila = var.ui.tabArticulos.selectedItems()
            datos = [var.ui.txtNombre, var.ui.txtPrecio]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

        except Exception as error:
            print('Error en cargar datos de un artículo. ', error)

    def bajaPro(self):
        try:
            nombre = var.ui.txtNombre.text()
            conexion.Conexion.bajaPro(nombre)
            conexion.Conexion.cargarTabPro(self)
            print(nombre)
        except Exception as error:
            print('Error en dar de baja al artículo. ', error)


    def modifPro(self):
        try:
            modproducto = []
            producto = [var.ui.txtNombre, var.ui.txtPrecio]
            for i in producto:
                modproducto.append(i.text())
            conexion.Conexion.modifPro(modproducto)
            conexion.Conexion.cargarTabPro(self)
        except Exception as error:
            print('Error en modificar el artículo. ', error)
