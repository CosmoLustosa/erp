# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import controleBD
import time

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        Cliente.setObjectName("Cliente")
        Cliente.setWindowModality(QtCore.Qt.ApplicationModal)
        Cliente.resize(373, 237)
        Cliente.setMinimumSize(QtCore.QSize(373, 237))
        Cliente.setMaximumSize(QtCore.QSize(373, 237))
        self.label = QtWidgets.QLabel(Cliente)
        self.label.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.label.setObjectName("label")
        self.txt_id = QtWidgets.QLineEdit(Cliente)
        self.txt_id.setGeometry(QtCore.QRect(80, 20, 91, 21))
        self.txt_id.setObjectName("txt_id")
        self.txt_id.setEnabled(False) #desabilita o campo id
        self.label_2 = QtWidgets.QLabel(Cliente)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Cliente)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 23, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Cliente)
        self.label_4.setGeometry(QtCore.QRect(20, 124, 49, 16))
        self.label_4.setObjectName("label_4")
        self.bt_cancelar = QtWidgets.QPushButton(Cliente)
        self.bt_cancelar.setGeometry(QtCore.QRect(80, 170, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_cancelar.setFont(font)
        self.bt_cancelar.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cancelar/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cancelar.setIcon(icon)
        self.bt_cancelar.setIconSize(QtCore.QSize(32, 32))
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.bt_cadastrar = QtWidgets.QPushButton(Cliente)
        self.bt_cadastrar.setGeometry(QtCore.QRect(250, 170, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_cadastrar.setFont(font)
        self.bt_cadastrar.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cancelar/icons/verifica (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cadastrar.setIcon(icon1)
        self.bt_cadastrar.setIconSize(QtCore.QSize(32, 32))
        self.bt_cadastrar.setObjectName("bt_cadastrar")
        self.widget = QtWidgets.QWidget(Cliente)
        self.widget.setGeometry(QtCore.QRect(80, 60, 281, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_nome = QtWidgets.QLineEdit(self.widget)
        self.txt_nome.setObjectName("txt_nome")
        self.verticalLayout.addWidget(self.txt_nome)
        self.txt_cpf = QtWidgets.QLineEdit(self.widget)
        self.txt_cpf.setObjectName("txt_cpf")
        self.verticalLayout.addWidget(self.txt_cpf)
        self.txt_endereco = QtWidgets.QLineEdit(self.widget)
        self.txt_endereco.setObjectName("txt_endereco")
        self.verticalLayout.addWidget(self.txt_endereco)

        self.retranslateUi(Cliente)
        QtCore.QMetaObject.connectSlotsByName(Cliente)

    def retranslateUi(self, Cliente):
        _translate = QtCore.QCoreApplication.translate
        Cliente.setWindowTitle(_translate("Cliente", "Dados do Cliente"))
        self.label.setText(_translate("Cliente", "ID:"))
        self.label_2.setText(_translate("Cliente", "Nome:"))
        self.label_3.setText(_translate("Cliente", "CPF:"))
        self.label_4.setText(_translate("Cliente", "Endereço:"))
        self.bt_cancelar.setText(_translate("Cliente", "Cancelar "))
        self.bt_cadastrar.setText(_translate("Cliente", "Cadastrar "))

        ############# funções dos botoes #########################
        ## ação de cancelar cadastro de clientes
        self.bt_cancelar.clicked.connect(lambda: self.fecharTela(Cliente))

        ##cadastrar clientes para
        self.bt_cadastrar.clicked.connect(self.cadastrarCliente)
        

    ## fecha a tela de formulario de cadastro
    def fecharTela(self, Cliente):
        Cliente.close()
    

    ## cadastra Clientes para
    def cadastrarCliente(self):
        nome = self.txt_nome.text()
        cpf =  self.txt_cpf.text()
        endereco = self.txt_endereco.text()

        try:
            db = controleBD.connectaDB()
            myCursor = db.cursor()
            sql = "INSERT INTO tb_clientes (nome, cpf, endereco) VALUES (%s, %s, %s)"
            values = (nome, cpf, endereco)
            myCursor.execute(sql, values)

            db.commit()
            self.txt_id.setText(f"{myCursor.lastrowid}")
            print(myCursor.rowcount, ': linhas gravadas')
            myCursor.close()

            #pausa o sistema um segundo
            
            self.txt_nome.setText("")
            self.txt_cpf.setText("")
            self.txt_endereco.setText("")
            
        except Exception as e:
            print("Impossível gravar os Dados!")


import botoes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cliente = QtWidgets.QWidget()
    ui = Ui_Cliente()
    ui.setupUi(Cliente)
    Cliente.show()
    sys.exit(app.exec_())

