"""
Facturación
"""
import conexion
import var
import window

class Facturas():
    def buscaCli(self):
        try:
            dni=var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro=conexion.Conexion.buscaClifac(dni)
            nombre=registro[0] + ','+registro[1]
            var.ui.txtClienteFac.setText(nombre)
        except Exception as error:
            print('Error al buscar cliente en facturas. ',error)
