# Form implementation generated from reading ui file 'c:\wamp64\www\Projetos\Python\estimulacaoprecoce\interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 633)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setStyleSheet("background-color: #272944")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_main = QtWidgets.QFrame(parent=self.widget)
        self.frame_main.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(True)
        self.frame_main.setFont(font)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_title = QtWidgets.QLabel(parent=self.frame_main)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.horizontalLayout.addWidget(self.main_title)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.frame_content = QtWidgets.QFrame(parent=self.widget)
        self.frame_content.setStyleSheet("QFrame {\n"
"    background-color: #363853;\n"
"    border-radius: 24px;\n"
"    padding: 24px\n"
"}")
        self.frame_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame_content)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setStyleSheet("QWidget {\n"
"    background-color: #363853;\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"    padding:0.5em 1.8em;\n"
"    margin-right: 0.5em;\n"
"    color: #f9f9fa;\n"
"    border:0;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QTabBar:tab:hover {\n"
"    background-color: #272944;\n"
"    color: #f9f9fa;\n"
"    border-bottom: 4px solid #404bda;\n"
"}\n"
"\n"
"QTabBar:tab:selected {\n"
"    background-color: #272944;\n"
"    color: #f9f9fa;\n"
"    border-bottom: 4px solid #404bda;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setMinimumSize(QtCore.QSize(753, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.home.setFont(font)
        self.home.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.home.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.home.setStyleSheet("")
        self.home.setObjectName("home")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.home)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_search = QtWidgets.QLineEdit(parent=self.home)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.line_search.setFont(font)
        self.line_search.setStyleSheet("QLineEdit {\n"
"    \n"
"    background-color: #ffffff;\n"
"    width: 80px;\n"
"    padding: 0.5em 1em;\n"
"    color: #272944;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 8px;\n"
"}")
        self.line_search.setObjectName("line_search")
        self.verticalLayout_4.addWidget(self.line_search)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.home)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    background-color: #f9f9fa;\n"
"    margin-top: 2em;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f9f9fa;\n"
"    margin: 0;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.frame = QtWidgets.QFrame(parent=self.home)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_visualizar = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_visualizar.setStyleSheet("QPushButton {\n"
"    background-color: #404bda;\n"
"    padding: 0.5em 2em;\n"
"    color: #f9f9fa;\n"
"    font-weight: 700;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #272944;\n"
"    color: #f9f9fa;\n"
"    border: 2px solid #404bda;\n"
"}")
        self.pushButton_visualizar.setObjectName("pushButton_visualizar")
        self.horizontalLayout_2.addWidget(self.pushButton_visualizar)
        self.pushButton_editar = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_editar.setStyleSheet("QPushButton {\n"
"    background-color: #f9f9fa;\n"
"    padding: 0.5em 2em;\n"
"    color: #272944;\n"
"    font-weight: 700;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #272944;\n"
"    color: #f9f9fa;\n"
"    border: 2px solid #f9f9fa;\n"
"}")
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_2.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_excluir.setStyleSheet("QPushButton {\n"
"    background-color: #ee0125;\n"
"    padding: 0.5em 2em;\n"
"    color: #f9f9fa;\n"
"    font-weight: 700;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #272944;\n"
"    color: #f9f9fa;\n"
"    border: 2px solid #ee0125;\n"
"}")
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_2.addWidget(self.pushButton_excluir)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 4)
        self.verticalLayout_4.addWidget(self.frame)
        self.tabWidget.addTab(self.home, "")
        self.Cadastro = QtWidgets.QWidget()
        self.Cadastro.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Cadastro.setStyleSheet("")
        self.Cadastro.setObjectName("Cadastro")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Cadastro)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.container_cadastro = QtWidgets.QFrame(parent=self.Cadastro)
        self.container_cadastro.setStyleSheet("")
        self.container_cadastro.setObjectName("container_cadastro")
        self.cadastroVertical_1 = QtWidgets.QVBoxLayout(self.container_cadastro)
        self.cadastroVertical_1.setContentsMargins(0, 0, 0, 0)
        self.cadastroVertical_1.setSpacing(0)
        self.cadastroVertical_1.setObjectName("cadastroVertical_1")
        self.container_line1 = QtWidgets.QFrame(parent=self.container_cadastro)
        self.container_line1.setStyleSheet("#container_line1{\n"
"    padding: 0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"    height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox {\n"
"    background-color: #272944;\n"
"    padding: 0 16px;\n"
"    border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"    height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox:on {\n"
"     border: 1px solid #f9f9fa;\n"
"     box-shadow: 0px 0px 0px 2px #242424;\n"
"     background-color: transparent;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox::drop-down {\n"
"    width: 16px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox  QAbstractItemView {\n"
"    padding: 0;\n"
"     background-color: transparent;\n"
"    color: #f9f9fa\n"
"}")
        self.container_line1.setObjectName("container_line1")
        self.cadastroHorizontal_1 = QtWidgets.QHBoxLayout(self.container_line1)
        self.cadastroHorizontal_1.setContentsMargins(0, 0, 0, 0)
        self.cadastroHorizontal_1.setSpacing(8)
        self.cadastroHorizontal_1.setObjectName("cadastroHorizontal_1")
        self.label = QtWidgets.QLabel(parent=self.container_line1)
        self.label.setObjectName("label")
        self.cadastroHorizontal_1.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.container_line1)
        self.lineEdit.setObjectName("lineEdit")
        self.cadastroHorizontal_1.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.container_line1)
        self.label_2.setObjectName("label_2")
        self.cadastroHorizontal_1.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.container_line1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.cadastroHorizontal_1.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(parent=self.container_line1)
        self.label_3.setObjectName("label_3")
        self.cadastroHorizontal_1.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.container_line1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.cadastroHorizontal_1.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(parent=self.container_line1)
        self.label_4.setObjectName("label_4")
        self.cadastroHorizontal_1.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(parent=self.container_line1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.cadastroHorizontal_1.addWidget(self.comboBox)
        self.cadastroHorizontal_1.setStretch(1, 4)
        self.cadastroHorizontal_1.setStretch(3, 3)
        self.cadastroHorizontal_1.setStretch(5, 2)
        self.cadastroHorizontal_1.setStretch(7, 1)
        self.cadastroVertical_1.addWidget(self.container_line1)
        self.container_line2 = QtWidgets.QFrame(parent=self.container_cadastro)
        self.container_line2.setStyleSheet("#container_line2{\n"
"    margin-top: 1.5em;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}")
        self.container_line2.setObjectName("container_line2")
        self.cadastroHorizontal_2 = QtWidgets.QHBoxLayout(self.container_line2)
        self.cadastroHorizontal_2.setContentsMargins(0, 0, 0, 0)
        self.cadastroHorizontal_2.setSpacing(8)
        self.cadastroHorizontal_2.setObjectName("cadastroHorizontal_2")
        self.label_5 = QtWidgets.QLabel(parent=self.container_line2)
        self.label_5.setObjectName("label_5")
        self.cadastroHorizontal_2.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.container_line2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.cadastroHorizontal_2.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(parent=self.container_line2)
        self.label_6.setObjectName("label_6")
        self.cadastroHorizontal_2.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.container_line2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.cadastroHorizontal_2.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(parent=self.container_line2)
        self.label_7.setObjectName("label_7")
        self.cadastroHorizontal_2.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.container_line2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.cadastroHorizontal_2.addWidget(self.lineEdit_6)
        self.cadastroHorizontal_2.setStretch(1, 4)
        self.cadastroHorizontal_2.setStretch(3, 4)
        self.cadastroHorizontal_2.setStretch(5, 4)
        self.cadastroVertical_1.addWidget(self.container_line2)
        self.container_line3 = QtWidgets.QFrame(parent=self.container_cadastro)
        self.container_line3.setStyleSheet("#container_line3{\n"
"    margin-top: 1.5em;\n"
"    padding: 0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QWidget > QFrame > QComboBox {\n"
"    background-color: #272944;\n"
"    padding: 0 16px;\n"
"    border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"    height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox:on {\n"
"     border: 1px solid #f9f9fa;\n"
"     box-shadow: 0px 0px 0px 2px #242424;\n"
"     background-color: transparent;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox::drop-down {\n"
"    width: 16px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox  QAbstractItemView {\n"
"    padding: 0;\n"
"     background-color: transparent;\n"
"    color: #f9f9fa\n"
"}")
        self.container_line3.setObjectName("container_line3")
        self.cadastroHorizontal_3 = QtWidgets.QHBoxLayout(self.container_line3)
        self.cadastroHorizontal_3.setContentsMargins(0, 0, 0, 0)
        self.cadastroHorizontal_3.setSpacing(8)
        self.cadastroHorizontal_3.setObjectName("cadastroHorizontal_3")
        self.label_8 = QtWidgets.QLabel(parent=self.container_line3)
        self.label_8.setObjectName("label_8")
        self.cadastroHorizontal_3.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.container_line3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.cadastroHorizontal_3.addWidget(self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(parent=self.container_line3)
        self.label_9.setObjectName("label_9")
        self.cadastroHorizontal_3.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.container_line3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.cadastroHorizontal_3.addWidget(self.lineEdit_8)
        self.label_10 = QtWidgets.QLabel(parent=self.container_line3)
        self.label_10.setObjectName("label_10")
        self.cadastroHorizontal_3.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.container_line3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.cadastroHorizontal_3.addWidget(self.lineEdit_9)
        self.label_11 = QtWidgets.QLabel(parent=self.container_line3)
        self.label_11.setObjectName("label_11")
        self.cadastroHorizontal_3.addWidget(self.label_11)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.container_line3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.cadastroHorizontal_3.addWidget(self.comboBox_2)
        self.cadastroHorizontal_3.setStretch(1, 4)
        self.cadastroHorizontal_3.setStretch(3, 4)
        self.cadastroHorizontal_3.setStretch(5, 3)
        self.cadastroHorizontal_3.setStretch(7, 1)
        self.cadastroVertical_1.addWidget(self.container_line3)
        self.container_line4 = QtWidgets.QFrame(parent=self.container_cadastro)
        self.container_line4.setStyleSheet("#container_line4{\n"
"    margin-top: 1.5em;\n"
"    padding: 0;\n"
"}\n"
"\n"
"#container_vertical1 {\n"
"    margin-left: 0.8em;\n"
"}\n"
"\n"
"#container_vertical1, #container_vertical2, #container_horizontal1, #container_horizontal2, #container_horizontal3{\n"
"    padding: 0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QWidget > QFrame > QComboBox {\n"
"    background-color: #272944;\n"
"    padding: 0 16px;\n"
"    border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"    height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox:on {\n"
"     border: 1px solid #f9f9fa;\n"
"     box-shadow: 0px 0px 0px 2px #242424;\n"
"     background-color: transparent;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox::drop-down {\n"
"    width: 16px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"}\n"
"\n"
"QWidget > QFrame > QComboBox  QAbstractItemView {\n"
"    padding: 0;\n"
"     background-color: transparent;\n"
"    color: #f9f9fa\n"
"}\n"
"\n"
"QWidget > QFrame > QTextEdit {\n"
"    background-color: #272944;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"    height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QTextEdit:focus {  \n"
"    border: 1px solid #f9f9fa;\n"
"     background-color: transparent;\n"
"}")
        self.container_line4.setObjectName("container_line4")
        self.cadastroHorizontal_4 = QtWidgets.QHBoxLayout(self.container_line4)
        self.cadastroHorizontal_4.setContentsMargins(0, 0, 0, 0)
        self.cadastroHorizontal_4.setSpacing(0)
        self.cadastroHorizontal_4.setObjectName("cadastroHorizontal_4")
        self.container_vertical2 = QtWidgets.QFrame(parent=self.container_line4)
        self.container_vertical2.setStyleSheet("")
        self.container_vertical2.setObjectName("container_vertical2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.container_vertical2)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(24)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.container_horizontal2 = QtWidgets.QFrame(parent=self.container_vertical2)
        self.container_horizontal2.setStyleSheet("QWidget > QFrame{\n"
"\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}")
        self.container_horizontal2.setObjectName("container_horizontal2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.container_horizontal2)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(parent=self.container_horizontal2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.container_horizontal2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_7.addWidget(self.lineEdit_10)
        self.label_16 = QtWidgets.QLabel(parent=self.container_horizontal2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.container_horizontal2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_7.addWidget(self.lineEdit_11)
        self.horizontalLayout_7.setStretch(1, 4)
        self.horizontalLayout_7.setStretch(3, 1)
        self.verticalLayout_8.addWidget(self.container_horizontal2)
        self.container_horizontal1 = QtWidgets.QFrame(parent=self.container_vertical2)
        self.container_horizontal1.setStyleSheet("QWidget > QFrame{\n"
"\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}")
        self.container_horizontal1.setObjectName("container_horizontal1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.container_horizontal1)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(parent=self.container_horizontal1)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.container_horizontal1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        self.label_14 = QtWidgets.QLabel(parent=self.container_horizontal1)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.container_horizontal1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_4)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(3, 2)
        self.verticalLayout_8.addWidget(self.container_horizontal1)
        self.container_horizontal3 = QtWidgets.QFrame(parent=self.container_vertical2)
        self.container_horizontal3.setStyleSheet("QWidget > QFrame{\n"
"\n"
"}\n"
"\n"
"QWidget > QFrame > QLabel {\n"
"    border: none;\n"
"    border-radius: none;\n"
"    color: #f9f9fa;\n"
"    font-size: 12px;\n"
"    padding:0;\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit {\n"
"    background-color: #272944;\n"
"     padding: 0 16px;\n"
"     border-radius: 8px;\n"
"    color: #f9f9fa;\n"
"height: 32px\n"
"}\n"
"\n"
"QWidget > QFrame > QLineEdit:focus {\n"
"  border: 1px solid #f9f9fa;\n"
"  box-shadow: 0px 0px 0px 2px #242424;\n"
"  background-color: transparent;\n"
"}")
        self.container_horizontal3.setObjectName("container_horizontal3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.container_horizontal3)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(parent=self.container_horizontal3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.container_horizontal3)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_8.addWidget(self.lineEdit_12)
        self.label_18 = QtWidgets.QLabel(parent=self.container_horizontal3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.container_horizontal3)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_8.addWidget(self.lineEdit_13)
        self.label_19 = QtWidgets.QLabel(parent=self.container_horizontal3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.container_horizontal3)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_8.addWidget(self.lineEdit_14)
        self.horizontalLayout_8.setStretch(1, 4)
        self.horizontalLayout_8.setStretch(3, 1)
        self.horizontalLayout_8.setStretch(5, 2)
        self.verticalLayout_8.addWidget(self.container_horizontal3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.cadastroHorizontal_4.addWidget(self.container_vertical2)
        self.container_vertical1 = QtWidgets.QFrame(parent=self.container_line4)
        self.container_vertical1.setStyleSheet("")
        self.container_vertical1.setObjectName("container_vertical1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.container_vertical1)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(parent=self.container_vertical1)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.textEdit = QtWidgets.QTextEdit(parent=self.container_vertical1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.cadastroHorizontal_4.addWidget(self.container_vertical1)
        self.cadastroHorizontal_4.setStretch(0, 6)
        self.cadastroHorizontal_4.setStretch(1, 4)
        self.cadastroVertical_1.addWidget(self.container_line4)
        self.verticalLayout.addWidget(self.container_cadastro)
        self.tabWidget.addTab(self.Cadastro, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_2.addWidget(self.frame_content)
        self.verticalLayout_10.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">Estimulação Precoce</span></p></body></html>"))
        self.line_search.setPlaceholderText(_translate("MainWindow", "Buscar"))
        self.pushButton_visualizar.setText(_translate("MainWindow", "Visualizar"))
        self.pushButton_editar.setText(_translate("MainWindow", "Editar"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "Nome Completo"))
        self.label_2.setText(_translate("MainWindow", "CPF"))
        self.lineEdit_2.setInputMask(_translate("MainWindow", "999.999.999-99"))
        self.label_3.setText(_translate("MainWindow", "Data de Nasc"))
        self.lineEdit_3.setInputMask(_translate("MainWindow", "99/99/9999"))
        self.label_4.setText(_translate("MainWindow", "Sexo"))
        self.comboBox.setItemText(0, _translate("MainWindow", "M"))
        self.comboBox.setItemText(1, _translate("MainWindow", "F"))
        self.label_5.setText(_translate("MainWindow", "Nome da Mãe"))
        self.label_6.setText(_translate("MainWindow", "Nome do Pai"))
        self.label_7.setText(_translate("MainWindow", "Matricula"))
        self.label_8.setText(_translate("MainWindow", "Telefone 01"))
        self.lineEdit_7.setInputMask(_translate("MainWindow", "(99) 99999-9999"))
        self.label_9.setText(_translate("MainWindow", "Telefone 02"))
        self.lineEdit_8.setInputMask(_translate("MainWindow", "(99) 99999-9999"))
        self.label_10.setText(_translate("MainWindow", "Naturalidade"))
        self.label_11.setText(_translate("MainWindow", "UF"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GO"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DF"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "MG"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "TO"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "SP"))
        self.label_15.setText(_translate("MainWindow", "Endereço"))
        self.label_16.setText(_translate("MainWindow", "Nº"))
        self.label_13.setText(_translate("MainWindow", "Professora"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Maria"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Lucia"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Ana Carolina"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Juliana"))
        self.label_14.setText(_translate("MainWindow", "Turma"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "D"))
        self.label_17.setText(_translate("MainWindow", "Cidade"))
        self.label_18.setText(_translate("MainWindow", "UF"))
        self.label_19.setText(_translate("MainWindow", "CEP"))
        self.label_12.setText(_translate("MainWindow", "Hipótese Diagnóstica"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), _translate("MainWindow", "Cadastro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Turmas"))