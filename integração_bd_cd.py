#Importando biblioteca BD
import mysql.connector
from cadastro import dados_alunos,dados_turma,dados_endereco
import datetime


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

    #Crud inserindo os dados
    if len(dados_alunos) != 0:
     
     #Conversão de formato da data
     data_nascimento = datetime.datetime.strptime(dados_alunos[0][2],'%d/%m/%Y')

    # Inserindo dados tabela alunos
     insert_alunos = f"""
                    INSERT INTO alunos 
                    (NomeCompleto,CPF,DataNascimento,Sexo,Mae,Pai,Matricula,Telefone1,Telefone2,Naturalidade,UF,HipoteseDiagnostica)
                    VALUES 
                    ('{dados_alunos[0][0]}','{dados_alunos[0][1]}','{data_nascimento}','{dados_alunos[0][9]}','{dados_alunos[0][3]}','{dados_alunos[0][4]}','{dados_alunos[0][8]}',
                    '{dados_alunos[0][5]}','{dados_alunos[0][6]}','{dados_alunos[0][7]}','{dados_alunos[0][11]}','{dados_alunos[0][13]}')"""
     cursor.execute(insert_alunos)
     con.commit()
     print("Dados inseridos com sucesso na tabela alunos .")
    
    #Crud Inserindo dados tabela turma
    if len(dados_turma) != 0:
     insert_turma = f"""
                    INSERT INTO Turma
                    (NomeTurma,Turno,Professor)
                    VALUES
                    ('{dados_turma[0][1]}','{dados_turma[0][0]}','{dados_turma[0][2]}')"""
     cursor.execute(insert_turma)
     con.commit()
     print("Dados inseridos com sucesso na tabela turma.")
    
    #Crud Inserindo dados tabela endereco
    if len(dados_endereco) != 0:
     insert_endereco = f"""
                    INSERT INTO endereco
                    (Cidade,Numero,UF,Endereco,CEP)
                    VALUES
                    ('{dados_endereco[0][0]}','{dados_endereco[0][1]}','{dados_endereco[0][2]}','{dados_endereco[0][3]}','{dados_endereco[0][4]}')
                    """
     cursor.execute(insert_endereco)
     con.commit()
     print("Dados inseridos com sucesso na tabela endereco.")
    

#Aviso erro
except mysql.connector.Error as erro: 
 print("Falha ao inserir os dados: {}".format(erro))

#Fechando servidor SQL
finally:
 if (con.is_connected()):
    cursor = con.cursor()
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")