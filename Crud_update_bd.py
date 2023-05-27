#Importando biblioteca BD
import mysql.connector
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


try: #Try para gerenciamento de erro

    #conectando ao banco de dados
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Estimulacao_Precoce"
)
    #Criando cursor e executando SQL no banco de dados
    cursor = con.cursor()

#Crud alteração de dados
    def update():
     alteracao_bd_alunos = f"""UPDATE alunos
                       SET NomeCompleto = '{NewName}',
                       CPF = '{}',
                       DataNascimento =  '{}',
                       Sexo = '{}',
                       Mae = '{}',
                       Pai = '{}',
                       Matricula = '{}',
                       Telefone1 = '{}',
                       Telefone2 = '{}',
                       Naturalidade = '{}',
                       UF = '{}',
                       HipoteseDiagnostica = '{}',
                       WHERE IdAluno = '{}'"""
     
     alteracao_bd_endereco = f"""UPDATE endereco
                            SET Cidade = '{}',
                            Numero = '{}',
                            UF = '{}',
                            Endereco = '{}',
                            CEP = '{}'
                            WHERE IdEndereco = {} """
     
     alteracao_bd_turma = f"""UPDATE Turma
                        SET NomeTurma = '{}',
                        Turno = '{}',
                        Professor = '{}',
                        WHERE NomeTurma = {} """
    


#Aviso erro
except mysql.connector.Error as erro: 
 print("Falha ao atualizar os dados: {}".format(erro))

#Fechando servidor SQL
finally:
 if (con.is_connected()):
    cursor = con.cursor()
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")

# Executador da interface
app = QtWidgets.QApplication([])
janela = uic.loadUi('interface.ui')
janela.pushButton_ler.clicked.connect(editar_dados)  # Botão para ler os dados
janela.show()
app.exec()