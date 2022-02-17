import conexion,eventos,var,locale



locale.setlocale(locale.LC_ALL, '')


class Productos():

    def guardaPro(self):
        """

        Módulo para guardar los productos.
        :rtype: object

        """
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
        """

        Módulo para cargar los datos de los productos.
        :rtype: object

        """
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
        """

        Módulo para eliminar los productos.
        :rtype: object

        """
        try:
            codigo = var.ui.lblCod.text()
            conexion.Conexion.bajaPro(codigo)
            conexion.Conexion.cargarTabPro(self)
        except Exception as error:
            print('Error en dar de baja al artículo. ', error)

    def modifPro(self):
        """

        Módulo para modificar los productos.
        :rtype: object

        """
        try:
            modproducto = []
            producto = [var.ui.lblCod, var.ui.txtNombre, var.ui.txtPrecio]
            for i in producto:
                modproducto.append(i.text())
            conexion.Conexion.modifPro(modproducto)
            conexion.Conexion.cargarTabPro(self)
        except Exception as error:
            print('Error en modificar el artículo. ', error)
