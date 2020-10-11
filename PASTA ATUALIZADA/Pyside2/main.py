import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QMessageBox
from Ui_funcionarios import Ui_Dialog
from metodos import Metodos
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QValidator


class funcionarios (QDialog):
    def __init__(self):
        super(funcionarios, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Mtos = Metodos()
       
        self.headerUsuarios = self.Mtos.generate_Header_labels('Usuarios')
        self.update_tb()
        self.ui.Btn_Salvar.clicked.connect(self.save)
        

    

    def update_tb(self):
        resultado = self.Mtos.run_query('select * from Usuarios')
        self.Mtos.print_in_TableWidget(
            self.ui.Tw_Registros,
            self.headerUsuarios,
            resultado)


    def save(self):
        pass

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = funcionarios()
    myapp.show()
    sys.exit(app.exec_())
