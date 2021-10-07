import sys,var, eventos,clients

from window import *
from windowaviso import *

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso,self).__init__()
        var.dlgaviso=Ui_windowaviso()
        var.dlgaviso.setupUi(self)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        var.ui=Ui_window()
        var.ui.setupUi(self)

        '''
        Eventos de botón
        '''
        var.ui.btnSalir.clicked.connect(eventos.Eventos.Salir)
        '''
        Eventos de la barra del menú
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)

        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    var.dlgaviso=DialogAviso()
    window.show()
    sys.exit(app.exec())
