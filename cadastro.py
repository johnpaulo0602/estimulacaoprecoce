from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# Função responsável por coletar os dados cadastrados dos alunos.

dados_endereco = []
dados_alunos = []
dados_turma = []

def cadastrar_dados_alunos():
    
    campos_line_edit = ['line_nome','line_cpf','Line_Edit_Dt','line_mae',
                        'line_pai','line_telefone1','line_telefone2','line_naturalidade',
                        'line_matricula'] 

    dados_line_edit = [janela.findChild(QtWidgets.QLineEdit, campo).text() for campo in campos_line_edit]

    campos_combo_box = ['combo_sexo', 'combo_turma', 'combo_uf', 'combo_professora']

    dados_combo_box = [janela.findChild(QtWidgets.QComboBox, campo).currentText() for campo in campos_combo_box]

    dados_text_edit = janela.findChild(QtWidgets.QTextEdit,'line_hipotese').toPlainText()

    campos_line_edit_endereco = ['line_cidade','line_numero','line_uf','line_endereco','line_cep']

    dados_line_edit_endereco = [janela.findChild(QtWidgets.QLineEdit,campo).text() for campo in campos_line_edit_endereco]


    # Verificar se algum campo está vazio
    if '' in dados_line_edit or '' in dados_combo_box or dados_text_edit == '' or '' in dados_line_edit_endereco:
        QMessageBox.about(janela, 'Alerta', 'Algum campo está vazio')
        return  # Retorna sem adicionar os dados
    
    dados_endereco.append(dados_line_edit_endereco)

    dados = dados_line_edit + dados_combo_box + [dados_text_edit]

    dados_alunos.append(dados)
    for campo in campos_line_edit:
            janela.findChild(QtWidgets.QLineEdit, campo).setText('')

    for campo in campos_line_edit_endereco:
            janela.findChild(QtWidgets.QLineEdit, campo).setText('')

    for campo in campos_combo_box:
        janela.findChild(QtWidgets.QComboBox, campo).setCurrentIndex(0)
    janela.findChild(QtWidgets.QTextEdit, 'line_hipotese').clear()

    for campo in campos_line_edit:
        janela.findChild(QtWidgets.QLineEdit, campo).setText('')
    

#Função responsável por coletar os dados referente a turma
def cadastrar_turma():
        
    campos_line_edit = ['line_turma','line_professora']

    combo_box_turma = ['combo_turno']

    dados_line_edit = [janela.findChild(QtWidgets.QLineEdit, campo).text() for campo in campos_line_edit]

    turno_combo_box = [janela.findChild(QtWidgets.QComboBox, campo).currentText() for campo in combo_box_turma]

    dados = turno_combo_box + dados_line_edit
    dados_turma.append(dados)  

    if '' in dados:
        QMessageBox.about(janela, 'Aletar', 'Algum campo está vazio')
    else:
        for campo in campos_line_edit:
            janela.findChild(QtWidgets.QLineEdit, campo).setText('')
        for campo in combo_box_turma:
            janela.findChild(QtWidgets.QComboBox, campo).setCurrentIndex(0)

#deletar os dados
def deletar_dados():
    for line in janela.findChildren(QtWidgets.QLineEdit):
        line.clear()
    janela.findChild(QtWidgets.QTextEdit, 'line_hipotese').clear()
  
#executador da interface
app=QtWidgets.QApplication([])
janela=uic.loadUi('estimulacaoprecoce/interface.ui')
janela.pushButton_turma_salvar.clicked.connect(cadastrar_turma)
janela.pushButton_salvar.clicked.connect(cadastrar_dados_alunos)
janela.pushButton_excluir.clicked.connect(deletar_dados)
janela.show()
app.exec()


print (dados_turma)
print (dados_alunos)
print (dados_endereco)