from PyQt5 import  uic,QtWidgets
import sqlite3
import time

def cad_form_cli():
    inicial.close()
    for_cli.show()

def cad_form_serv():
    inicial.close()
    for_serv.show()

def agend():
    inicial.close()
    agendamento.show()

def voltar_cli():
    for_cli.close()
    inicial.show()

def voltar_serv():
    for_serv.close()
    inicial.show()

def cadastrar_cli():
    codigo = for_cli.lineEdit.text()
    nome = for_cli.lineEdit_2.text()
    telefone = for_cli.lineEdit_3.text()
    email = for_cli.lineEdit_4.text()

    if (codigo != '' and nome != '' and telefone != '' and email != ''):
        try:
            banco = sqlite3.connect('banco_cadastro_cli.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, codigo INT, nome TEXT, telefone INT, email TEXT)")
            banco.commit() 
            banco.close()
            for_cli.label.setText("Cliente cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else: 
        for_cli.label.setText("Insira todos os dados") 

def cadastrar_serv():
    codigo = for_serv.lineEdit.text()
    descricao = for_serv.lineEdit_2.text()
    preco = for_serv.lineEdit_3.text()
    
    if (codigo != '' and descricao != '' and preco != ''):
        try:
            banco = sqlite3.connect('banco_cadastro_serv.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_servico (codigo INT, descricao TEXT,preco FLOAT)")
            banco.commit() 
            banco.close()
            for_serv.label.setText("Serviço cadastrado com sucesso")


        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else: 
        for_serv.label.setText("Insira todos os dados")


app=QtWidgets.QApplication([])
inicial=uic.loadUi("inicial.ui")
for_cli=uic.loadUi("formulario_cliente.ui")
for_serv=uic.loadUi("formulario_serviços.ui")
agendamento=uic.loadUi("agendamento.ui")
inicial.pushButton.clicked.connect(cad_form_cli)
inicial.pushButton_2.clicked.connect(cad_form_serv)
inicial.pushButton_4.clicked.connect(agend)
for_cli.pushButton.clicked.connect(cadastrar_cli)
for_cli.pushButton_2.clicked.connect(voltar_cli)
for_serv.pushButton_5.clicked.connect(cadastrar_serv)
for_serv.pushButton_2.clicked.connect(voltar_serv)


inicial.show()
app.exec()