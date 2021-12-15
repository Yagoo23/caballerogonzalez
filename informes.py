import os,var
from datetime import datetime

from PyQt5 import QtSql
from reportlab.pdfgen import canvas
class Informes():
    def listadoClientes(self):
        try:
            var.cv=canvas.Canvas('informes/listadoclientes.pdf')
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de Administración')
            Informes.cabecera(self)
            rootPath='.\\informes'
            var.cv.setFont('Helvetica-Bold',size=10)
            textotitulo='LISTADO CLIENTES'
            var.cv.drawString(235,690,textotitulo)
            var.cv.line(40,685,530,685)
            items=['DNI','Nombre','Formas de pago']
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(220,675,items[1])
            var.cv.drawString(370, 675, items[2])
            var.cv.line(40,670,530,670)
            query=QtSql.QSqlQuery('select dni,apellidos,nombre,pago from clientes order by apellidos,nombre')
            var.cv.setFont('Helvetica',size=8)
            if query.exec_():
                i=50
                j=655
                while query.next():
                    if j<=80:
                        var.cv.drawString(460,30,'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.setFont('Helvetica-Bold', size=10)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(220, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i,j,str(query.value(0)))
                    var.cv.drawString(i+140,j,str(query.value(1) + ', '+query.value(2)))
                    var.cv.drawString(i+310,j,str(query.value(3)))
                    j=j-20
            Informes.pie(textotitulo)
            var.cv.save()
            cont= 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' %(rootPath,file))
                cont=cont+1

        except Exception as error:
            print('Error en informe clientes.',error)

    def listadoArticulos(self):
        try:
            var.cv = canvas.Canvas('informes/listadoarticulos.pdf')
            var.cv.setTitle('Listado Artículos')
            var.cv.setAuthor('Departamento de Administración')
            Informes.cabecera(self)
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=10)
            textotitulo = 'LISTADO ARTÍCULOS'
            var.cv.drawString(235, 690, textotitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['Código', 'Nombre', 'Precio']
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(220, 675, items[1])
            var.cv.drawString(390, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery('select codigo,nombre,precio from articulos order by nombre')
            var.cv.setFont('Helvetica', size=8)
            if query.exec_():
                i=50
                j=655
                while query.next():
                    if j<=80:
                        var.cv.drawString(460,30,'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.setFont('Helvetica-Bold', size=10)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['Código', 'Nombre', 'Precio']
                        var.cv.drawString(170, 675, items[0])
                        var.cv.drawString(220, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i+30,j,str(query.value(0)))
                    var.cv.drawString(i+170,j,str(query.value(1)))
                    var.cv.drawString(i+340,j,str(query.value(2)))
                    j=j-20
            Informes.pie(textotitulo)
            var.cv.save()
            cont= 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' %(rootPath,file))
                cont=cont+1
        except Exception as error:
            print('Error en informe artículos.', error)

    def cabecera(self):
        try:
            logo= '.\\img\logo-empresa.jpg'
            var.cv.line(40,800,530,800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica',10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.line(40,710,530,710)
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia,101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'e-mail: micorreo@mail.com')
            var.cv.drawImage(logo,400,715)
        except Exception as error:
            print('Error en la cabecera informe. ',error)

    def pie(texto):
        try:
            var.cv.line(50,50,530,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y   %H.%M.%S')
            var.cv.setFont('Helvetica-Bold',size=6)
            var.cv.drawString(70,40,str(fecha))
            var.cv.drawString(255,40,str(texto))
            var.cv.drawString(510,40,str('Página %s ' %var.cv.getPageNumber()))

        except Exception as error:
            print('Error creación de pie de informe clientes. ', error)