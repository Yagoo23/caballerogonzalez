import locale

import conexion
import eventos
import var
import locale
from PyQt5 import QtSql, QtWidgets

locale.setlocale(locale.LC_ALL, '')


class Productos():

    def guardaPro(self):
        try:
            # newpro = []
            # producto = [var.ui.txtNombre, var.ui.txtPrecio]
            # tabPro = []
            # product = [var.ui.txtNombre, var.ui.txtPrecio]
            # for i in producto:
            #     newpro.append(i.text())
            # for i in product:
            #     tabPro.append(i.text())
            newpro = []
            producto = var.ui.txtNombre.text()
            producto = producto.title()
            newpro.append(producto)
            precio = var.ui.txtPrecio.text()
            precio = precio.replace(',', '.')  # necesita estar con punto como en américa
            precio = locale.currency(float(precio))
            newpro.append(precio)
            conexion.Conexion.altaPro(newpro)
            conexion.Conexion.cargarTabPro(self)


        except Exception as error:
            print('Error en guardar artículo ', error)

    def cargaPro(self):
        try:
            eventos.Eventos.limpiaFormPro(self)
            fila = var.ui.tabArticulos.selectedItems()
            datos = [var.ui.lblCod, var.ui.txtNombre, var.ui.txtPrecio]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
        except Exception as error:
            print('Error en cargar datos de un artículo. ', error)

    def bajaPro(self):
        try:
            codigo = var.ui.lblCod.text()
            conexion.Conexion.bajaPro(codigo)
            conexion.Conexion.cargarTabPro(self)
        except Exception as error:
            print('Error en dar de baja al artículo. ', error)

    def modifPro(self):
        try:
            modproducto = []
            producto = [var.ui.lblCod, var.ui.txtNombre, var.ui.txtPrecio]
            for i in producto:
                modproducto.append(i.text())
            conexion.Conexion.modifPro(modproducto)
            conexion.Conexion.cargarTabPro(self)
        except Exception as error:
            print('Error en modificar el artículo. ', error)
