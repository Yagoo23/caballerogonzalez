import os,var

from reportlab.pdfgen import canvas
class Informes():
    def listadoClientes(self):
        try:
            var.cv=canvas.Canvas('informes/listadoclientes.pdf')
            Informes.cabecera(self)
            rootPath='.\\informes'
            var.cv.setFont('Helvetica',8)
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de Administración')
            var.cv.save()
            cont= 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' %(rootPath,file))
                cont=cont+1

        except Exception as error:
            print('Error en informe clientes.',error)

    def cabecera(self):
        try:
            logo= '.\\img\logo-empresa.jpg'
            var.cv.line(40,800,500,800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica',10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.line(40,710,500,710)
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia,101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'e-mail: micorreo@mail-com')
            var.cv.drawImage(logo,400,715)
        except Exception as error:
            print('Error en la cabecera informe. ',error)