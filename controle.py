from PyQt6 import  uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas



banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)



def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO")
    
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""
    
    if formulario.radioButton.isChecked() :
        print("Categoria Informatica selecionada")
        categoria = "Alimentos"

    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos selecionada")
        categoria = "Eletronicos"

    else :
        print("Categoria Eletronicos selecionada")
        categoria = "Informatica"

    print("Codigo:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def chama_segunda_tela():
    segunda_tela.show()


    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0,len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))




app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)


formulario.show()
app.exec()


#Criando tabela

""" create table produtos (
id INT NOT NULL AUTO_INCREMENT,
codigo INT,
descricao VARCHAR(50),
preco DOUBLE,
categoria VARCHAR(20),
PRIMARY KEY (id)
); """



# inserindo registros na tabela

#INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (123,"impressora",500.00,"informatica");
