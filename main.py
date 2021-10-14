import sys,var, eventos,clients

from datetime import *
from window import *
from windowaviso import *
from windowcal import *


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar,self).__init__()
        var.dlgcalendar=Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual=datetime.now().day
        mesactual=datetime.now().month
        anoactual=datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        #var.dlgcalendar.Calendar.clicked.connect((clients.Clientes.cargarFecha))



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
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrircal)
        '''
        Eventos de la barra del menú
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)

        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)

        '''
        Eventos de comboBox 
        '''
        clients.Clientes.cargaProv_(self)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    var.dlgaviso=DialogAviso()
    var.dlgcalendar=DialogCalendar()
    window.show()
    sys.exit(app.exec())
