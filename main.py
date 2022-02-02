import sys, var, eventos, clients, locale, invoice, conexion, productos, informes

from datetime import *
from window import *
from windowaviso import *
from windowcal import *

locale.setlocale(locale.LC_ALL, 'es-ES')


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''
        Ventana abrir explorador windows
        '''
        super(FileDialogAbrir, self).__init__()


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)


class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_window()
        var.ui.setupUi(self)


        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.letracapital)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.letracapital)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.letracapital)
        var.txtCantidad = QtWidgets.QLineEdit()
        var.txtCantidad.returnPressed.connect(invoice.Facturas.totalLineaVenta)

        '''
        Eventos de boton
        '''
        # var.ui.btnSalir.clicked.connect(eventos.Eventos.Salir)
        # var.ui.btnSalir2.clicked.connect(eventos.Eventos.Salir)
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        # var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrircal)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnRecarga.clicked.connect(eventos.Eventos.limpiaFormCLi)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnGrabaPro.clicked.connect(productos.Productos.guardaPro)
        var.ui.btnRecarga2.clicked.connect(eventos.Eventos.limpiaFormPro)
        var.ui.btnBajaPro.clicked.connect(productos.Productos.bajaPro)
        var.ui.btnModifPro.clicked.connect(productos.Productos.modifPro)
        var.ui.btnBuscaClifac.clicked.connect(invoice.Facturas.buscaCli)
        var.ui.btnFechaFac.clicked.connect(eventos.Eventos.abrircal)
        var.ui.btnFacturar.clicked.connect(invoice.Facturas.facturar)
        var.ui.btnPDFCli.clicked.connect(informes.Informes.listadoClientes)
        var.ui.btnPDFArt.clicked.connect(informes.Informes.listadoArticulos)
        var.ui.btnReportCli.clicked.connect(eventos.Eventos.Imprimir)
        var.ui.btnImprimirFactura.clicked.connect(informes.Informes.factura)
        var.ui.btnEliminarVenta.clicked.connect(conexion.Conexion.eliminarVenta)
        '''
        Eventos de la barra del menú
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(eventos.Eventos.Abrir)
        var.ui.actionCrear_Backup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar_base_de_datos.triggered.connect(eventos.Eventos.restaurarBD)
        var.ui.actionImprimir.triggered.connect(eventos.Eventos.Imprimir)
        var.ui.actionImportar_Datos.triggered.connect(clients.Clientes.importarDatos)
        var.ui.actionExportar_Datos.triggered.connect(clients.Clientes.exportarDatos)

        '''
        Eventos de SpinBox
        '''
        var.ui.spinEnvio.valueChanged.connect(clients.Clientes.selEnvio)
        '''
        Eventos de QTabWidget
        '''
        eventos.Eventos.ResizeTabClientes(self)
        eventos.Eventos.ResizeTabFacturas(self)
        eventos.Eventos.ResizeTabVentas(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabArticulos.clicked.connect(productos.Productos.cargaPro)
        var.ui.tabArticulos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFacturas.clicked.connect(invoice.Facturas.cargaFac)
        var.ui.tabVentas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        invoice.Facturas.cargaLineaVenta(self)
        var.ui.tabClientes.clicked.connect(invoice.Facturas.cargaCliFac)
        # invoice.Facturas.prepararTabFac(self)
        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        day = datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d de %B de %Y').capitalize())
        '''
        Eventos menú herramientas
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.Salir)
        var.ui.actionbarAbrir.triggered.connect(eventos.Eventos.Abrir)
        var.ui.actionbarBackup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionbarRestaurarBackup.triggered.connect(eventos.Eventos.restaurarBD)
        var.ui.actionbarImprimir.triggered.connect(eventos.Eventos.Imprimir)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)



        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTabCli(self)
        conexion.Conexion.cargarProv(self)
        conexion.Conexion.cargarMuni(self)
        conexion.Conexion.cargarTabPro(self)
        conexion.Conexion.cargaTabfacturas(self)

        '''
        Eventos de comboBox 
        '''
        # clients.Clientes.cargaProv_(self)

        # var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.cargarMuni)

        conexion.Conexion.cargarCmbProducto(self)
        var.cmbProducto.currentIndexChanged.connect(invoice.Facturas.proceso_venta)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
