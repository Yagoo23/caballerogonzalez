import sys

from window import *
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui=Ui_window()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())
