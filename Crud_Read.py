import mysql.connector
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# ...

# Função responsável por realizar a leitura dos dados cadastrados no banco de dados
def ler_dados_cadastrados():
    try:
        #conectando ao banco de dados
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="Estimulacao_Precoce"
        ) 
    #Criando cursor e executando SQL no banco de dados
        cursor = con.cursor()

        # Consulta para obter os dados cadastrados das turmas
        dados_turma = "SELECT * FROM Turma"
        cursor.execute(dados_turma)
        dados_turmas = cursor.fetchall()

        # Consulta para obter os dados cadastrados dos endereços
        dados_endereco = "SELECT * FROM endereco"
        cursor.execute(dados_endereco)
        dados_enderecos = cursor.fetchall()

        # Consulta para obter os dados cadastrados dos alunos
        dados_alunos = "SELECT * FROM alunos"
        cursor.execute(dados_alunos)
        dados_alunos = cursor.fetchall()

        # Fechar cursor e conexão
        cursor.close()
        con.close()

        # Mapeamento dos campos do banco de dados com as caixas de texto na interface
        mapeamento = {
    'NomeCompleto':'line_nome',
    'CPF': 'line_cpf',
    'DataNascimento': 'Line_Edit_Dt',
    'Mae': 'line_mae',
    'Pai': 'line_pai',
    'Telefone1': 'line_telefone1',
    'Telefone2': 'line_telefone2',
    'Naturalidade': 'line_naturalidade',
    'Matricula': 'line_matricula'
}

        # Exibir os dados na interface ou realizar outras operações necessárias
        print("Dados dos Alunos:")
        for dados in dados_alunos:
            for campo, nome_objeto in mapeamento.items():
                if hasattr(janela, nome_objeto):
                    objeto = getattr(janela, nome_objeto)
                    indice = cursor.description.index((campo))
                    valor = dados[indice]
                    objeto.setText(str(valor))
                
    except mysql.connector.Error as erro: 
        print("Falha ao consultar o banco de dados: {}".format(erro))


         #Fechando servidor SQL
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print ("A conexão ao MySQL foi encerrada.")


 # Executador da interface
app = QtWidgets.QApplication([])
janela = uic.loadUi('estimulacaoprecoce/interface.ui')
janela.pushButton_salvar.clicked.connect(ler_dados_cadastrados)  # Botão para ler os dados
janela.show()
app.exec()