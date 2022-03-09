import unittest, clients, conexion, var
from PyQt5 import QtSql


class MyTestCase(unittest.TestCase):

    def test_dni(self):
        dni = '53610914H'
        value = clients.Clientes.validarDNI(dni)
        msg = 'Error DNI'
        self.assertTrue(value, msg)
    def test_conexion(self):
        value = conexion.Conexion.db_connect(var.filedb)
        msg = 'Conexión establecida'
        self.assertTrue(value, msg)
    def test_fac(self):
        valor = 40.03
        codfac = 38
        total=0
        try:
            msg = 'Cálculos incorrectos'
            query = QtSql.QSqlQuery()
            query1 = QtSql.QSqlQuery()
            query.prepare('select codven,codpro,cantidad from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codpro = query.value(1)
                    cantidad = query.value(2)
                    query1.prepare('select nombre,precio from articulos where codigo = :codpro')
                    query1.bindValue(':codpro', int(codpro))
                    if query1.exec_():
                        while query1.next():
                            precio = query1.value(1)
                            subtotal = round(float(cantidad) * float(precio), 2)
                    total = round(float(subtotal) + float(total), 2)
            iva = round(float(total) * 0.21, 2)
            total = round(float(iva) + float(total), 2)
        except Exception as error:
            print('Error listado de la tabla de ventas: %s ' %str(error))
        self.assertEqual(round(float(valor),2),round(float(total),2),msg)


if __name__ == '__main__':
    unittest.main()
