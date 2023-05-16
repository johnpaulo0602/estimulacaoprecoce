#Importando biblioteca BD
import mysql.connector
from cadastro import dados_alunos,dados_turma

try: #Try para gerenciamento de erro

    #conectando ao banco de dados
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Estimulacao_Precoce"
)
    cursor = con.cursor()
    # crud 
    insert_data = """
                    INSERT INTO alunos 
                    (NomeCompleto,CPF,DataNascimento,Sexo,Naturalidade,UF,HipoteseDiagnostica)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)"""
#Criando cursor e executando SQL no banco de dados
    comando = ''
    con.commit()
    




 
except mysql.connector.Error as erro: 
 print("Falha ao : {}".format(erro))


finally:

 if (con.is_connected()):
    cursor.close()
    con.close()
    print ("A conexão ao MySQL foi encerrada.")