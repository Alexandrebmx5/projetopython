from PyQt5 import uic,QtWidgets
import sqlite3
import time

def cad_form_cli():
    inicial.close()
    for_cli.show()

def cad_form_serv():
    inicial.close()
    for_serv.show()

def voltar_cli():
    for_cli.close()
    inicial.show()

def voltar_serv():
    for_serv.close()
    inicial.show()

def voltar_agend():
    agendamento.close()
    inicial.show()

def voltar_agend_table():
    table_agendamentos.close()
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
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                codigo INT NOT NULL, 
                nome TEXT NOT NULL, 
                telefone INT NOT NULL, 
                email TEXT NOT NULL);''')
            cursor.execute(f'''INSERT INTO cliente VALUES({codigo}, '{nome}', {telefone}, '{email}');''')
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
            cursor.execute('''CREATE TABLE IF NOT EXISTS servico (
                codigo INT, 
                descricao TEXT,
                preco FLOAT);''')
            cursor.execute(f'''INSERT INTO servico VALUES({codigo}, '{descricao}', {preco});''')
            banco.commit() 
            banco.close()
            for_serv.label.setText("Serviço cadastrado com sucesso")


        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else: 
        for_serv.label.setText("Insira todos os dados")

def agend():
    inicial.close()
    agendamento.show()

    banco = sqlite3.connect('banco_cadastro_cli.db')
    c = banco.cursor()
    c.execute('''SELECT * FROM cliente;''')
    dados_lidos = c.fetchall()
        
    agendamento.tableWidget.setRowCount(len(dados_lidos))
    agendamento.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            agendamento.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco = sqlite3.connect('banco_cadastro_serv.db')
    c = banco.cursor()
    c.execute('''SELECT * FROM servico;''')
    dados_lidos = c.fetchall()
        
    agendamento.tableWidget_2.setRowCount(len(dados_lidos))
    agendamento.tableWidget_2.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            agendamento.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def fazer_agend():
    codigo = agendamento.lineEdit.text()
    nome = agendamento.lineEdit_2.text()
    dataehora = agendamento.lineEdit_3.text()
    servico = agendamento.lineEdit_4.text()

    if (codigo != '' and nome != '' and dataehora != ''):
        try:
            banco = sqlite3.connect('banco_agendamento.db')
            cursor = banco.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS agendamento (
                codigo INT NOT NULL, 
                nome TEXT NOT NULL, 
                dataehora DATETIME NOT NULL,
                servico TEXT NOT NULL);''')
            cursor.execute(f'''INSERT INTO agendamento VALUES({codigo}, '{nome}', '{dataehora}', '{servico}');''')
            banco.commit() 
            banco.close()
            agendamento.label.setText("agendamento cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else: 
        agendamento.label.setText("Insira todos os dados")

def table_agend():
    inicial.close()
    table_agendamentos.show()

    banco = sqlite3.connect('banco_agendamento.db')
    c = banco.cursor()
    c.execute('''SELECT * FROM agendamento;''')
    dados_lidos = c.fetchall()
        
    table_agendamentos.tableWidget.setRowCount(len(dados_lidos))
    table_agendamentos.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            table_agendamentos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

app=QtWidgets.QApplication([])
inicial=uic.loadUi("inicial.ui")
for_cli=uic.loadUi("formulario_cliente.ui")
for_serv=uic.loadUi("formulario_serviços.ui")
agendamento=uic.loadUi("agendamento.ui")
table_agendamentos=uic.loadUi("table_agendamentos.ui")
inicial.pushButton.clicked.connect(cad_form_cli)
inicial.pushButton_2.clicked.connect(cad_form_serv)
inicial.pushButton_4.clicked.connect(agend)
inicial.pushButton_5.clicked.connect(table_agend)
agendamento.pushButton.clicked.connect(fazer_agend)
agendamento.pushButton_2.clicked.connect(voltar_agend)
table_agendamentos.pushButton.clicked.connect(voltar_agend_table)
for_cli.pushButton.clicked.connect(cadastrar_cli)
for_cli.pushButton_2.clicked.connect(voltar_cli)
for_serv.pushButton_5.clicked.connect(cadastrar_serv)
for_serv.pushButton_2.clicked.connect(voltar_serv)


inicial.show()
app.exec()