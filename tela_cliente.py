# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from form_cliente import *



#Libs diversas
import pandas as pd
import controleBD



class Ui_clientes(object):
    def setupUi(self, clientes):
        clientes.setObjectName("clientes")
        clientes.resize(597, 377)
        clientes.setMinimumSize(QtCore.QSize(597, 377))
        clientes.setMaximumSize(QtCore.QSize(597, 377))
        clientes.setWindowModality(QtCore.Qt.ApplicationModal)
        self.bt_excluir = QtWidgets.QPushButton(clientes)
        self.bt_excluir.setGeometry(QtCore.QRect(330, 0, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_excluir.setFont(font)
        self.bt_excluir.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/adicionar/icons/excluir user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_excluir.setIcon(icon)
        self.bt_excluir.setIconSize(QtCore.QSize(32, 32))
        self.bt_excluir.setObjectName("bt_excluir")
        self.bt_consultar = QtWidgets.QPushButton(clientes)
        self.bt_consultar.setGeometry(QtCore.QRect(220, 0, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_consultar.setFont(font)
        self.bt_consultar.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/adicionar/icons/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_consultar.setIcon(icon1)
        self.bt_consultar.setIconSize(QtCore.QSize(32, 32))
        self.bt_consultar.setObjectName("bt_consultar")
        self.bt_alterar = QtWidgets.QPushButton(clientes)
        self.bt_alterar.setGeometry(QtCore.QRect(110, 0, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_alterar.setFont(font)
        self.bt_alterar.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/adicionar/icons/alterar_usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_alterar.setIcon(icon2)
        self.bt_alterar.setIconSize(QtCore.QSize(32, 32))
        self.bt_alterar.setObjectName("bt_alterar")
        self.bt_adicionaCliente = QtWidgets.QPushButton(clientes)
        self.bt_adicionaCliente.setGeometry(QtCore.QRect(0, 0, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.bt_adicionaCliente.setFont(font)
        self.bt_adicionaCliente.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bt_adicionaCliente.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/adicionar/icons/adicioar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_adicionaCliente.setIcon(icon3)
        self.bt_adicionaCliente.setIconSize(QtCore.QSize(32, 32))
        self.bt_adicionaCliente.setDefault(False)
        self.bt_adicionaCliente.setFlat(False)
        self.bt_adicionaCliente.setObjectName("bt_adicionaCliente")
        self.bt_sair = QtWidgets.QPushButton(clientes)
        self.bt_sair.setGeometry(QtCore.QRect(480, 0, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_sair.setFont(font)
        self.bt_sair.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/adicionar/icons/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_sair.setIcon(icon4)
        self.bt_sair.setIconSize(QtCore.QSize(32, 32))
        self.bt_sair.setObjectName("bt_sair")
        self.txt_cliente = QtWidgets.QLineEdit(clientes)
        self.txt_cliente.setGeometry(QtCore.QRect(70, 80, 381, 21))
        self.txt_cliente.setMinimumSize(QtCore.QSize(381, 0))
        self.txt_cliente.setObjectName("txt_cliente")
        self.bt_pesquisar = QtWidgets.QPushButton(clientes)
        self.bt_pesquisar.setGeometry(QtCore.QRect(460, 70, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_pesquisar.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/adicionar/icons/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_pesquisar.setIcon(icon5)
        self.bt_pesquisar.setIconSize(QtCore.QSize(32, 32))
        self.bt_pesquisar.setObjectName("bt_pesquisar")
        self.label = QtWidgets.QLabel(clientes)
        self.label.setGeometry(QtCore.QRect(20, 80, 47, 21))
        self.label.setObjectName("label")
        self.tb_dados_cliente = QtWidgets.QTableWidget(clientes)
        self.tb_dados_cliente.setGeometry(QtCore.QRect(10, 130, 581, 241))
        self.tb_dados_cliente.setMinimumSize(QtCore.QSize(581, 241))
        self.tb_dados_cliente.setMaximumSize(QtCore.QSize(581, 241))
        self.tb_dados_cliente.setObjectName("tb_dados_cliente")
        self.tb_dados_cliente.setColumnCount(4)
        self.tb_dados_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_dados_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_dados_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_dados_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_dados_cliente.setHorizontalHeaderItem(3, item)

        self.retranslateUi(clientes)
        QtCore.QMetaObject.connectSlotsByName(clientes)


        ### AÇÕES DOS BOTÕES ###
        self.bt_sair.clicked.connect(lambda: self.sairCliente(clientes)) #botão sair
        self.bt_pesquisar.clicked.connect(self.consultarCliente)
        self.bt_adicionaCliente.clicked.connect(self.cadastrarCliente)
        self.bt_consultar.clicked.connect(self.consultaClienteID)

    

    #### funções do sistema
    def cadastrarCliente(self):
        self.Cliente = QtWidgets.QWidget()
        self.ui = Ui_Cliente()
        self.ui.setupUi(self.Cliente)
        self.Cliente.show()

    def sairCliente(self, clientes):
       clientes.close()
    

    def consultarCliente(self):
        bd = controleBD.connectaDB()
        myCursor = bd.cursor()
        

        if len(self.txt_cliente.text()) >= 1:
            nome = self.txt_cliente.text()
            sql = "SELECT idCliente, nome, cpf, endereco FROM tb_clientes WHERE nome LIKE  '%{}%'".format(nome)
            
            myCursor.execute(sql, nome)
            result = myCursor.fetchall()
            #print(result)
        else:
            myCursor.execute('SELECT * FROM tb_clientes')
            result = myCursor.fetchall()
            #print(result)

        
        df = pd.DataFrame(result, columns = ['ID', 'NOME DO CLIENTE', 'CPF', 'ENDERECO'])
        self.all_data = df
        numRows = len(self.all_data.index)
        self.tb_dados_cliente.setColumnCount(len(self.all_data.columns))
        self.tb_dados_cliente.setRowCount(numRows)
        self.tb_dados_cliente.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_dados_cliente.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()

        myCursor.close()

    def consultaClienteID(self):
        print("Cliquei..")
        linha = self.tb_dados_cliente.currentRow()
        item = self.tb_dados_cliente.item(linha, 0)
        print(item.text())
        '''self.Cliente = QtWidgets.QWidget()
        self.ui = Ui_Cliente()
        self.ui.setupUi(self.Cliente)
        self.Cliente.show()
        self.Cliente.txt_id.setText("")'''

        


    def retranslateUi(self, clientes):
        _translate = QtCore.QCoreApplication.translate
        clientes.setWindowTitle(_translate("clientes", "Clientes"))
        self.bt_excluir.setText(_translate("clientes", "Excluir"))
        self.bt_consultar.setText(_translate("clientes", "Consultar"))
        self.bt_alterar.setText(_translate("clientes", "Alterar"))
        self.bt_adicionaCliente.setToolTip(_translate("clientes", "Adicionar Cliente"))
        self.bt_adicionaCliente.setText(_translate("clientes", "Adicionar"))
        self.bt_sair.setText(_translate("clientes", "Sair"))
        self.bt_pesquisar.setText(_translate("clientes", " Pesquisar"))
        self.label.setText(_translate("clientes", "Cliente:"))
        item = self.tb_dados_cliente.horizontalHeaderItem(0)
        item.setText(_translate("clientes", "ID"))
        item = self.tb_dados_cliente.horizontalHeaderItem(1)
        item.setText(_translate("clientes", "NOME DO CLIENTE"))
        item = self.tb_dados_cliente.horizontalHeaderItem(2)
        item.setText(_translate("clientes", "CPF"))
        item = self.tb_dados_cliente.horizontalHeaderItem(3)
        item.setText(_translate("clientes", "ENDEREÇO"))

import telas

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clientes = QtWidgets.QWidget()
    ui = Ui_clientes()
    ui.setupUi(clientes)
    clientes.show()
    sys.exit(app.exec_())

