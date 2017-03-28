# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#===================================
# Criado por: Wolfterro
# Versão: 1.1 - Python 2.x
# Data: 26/03/2017
#===================================

from PyQt4 import QtCore, QtGui
import sys

# Imports do programa
# ===================
from WindowHandler import WindowHandler
from GlobalVars import GlobalVars

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Codificação do programa.
# ========================
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

# Classe principal do Programa gerado pelo Qt Designer.
# =====================================================
class Ui_MainWindow(object):
	def setupUi(self, MainWindow, Handler):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(700, 820)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		self.lineEdit = QtGui.QLineEdit(self.groupBox)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
		self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
		self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.textEdit = QtGui.QTextEdit(self.groupBox_3)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 1)
		self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
		self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.pushButton = QtGui.QPushButton(self.groupBox_4)
		self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    font-weight: bold;\n"
"}"))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
		self.pushButton_2 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"    font-style: italic;\n"
"}"))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"    text-decoration: underline;\n"
"}"))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 2)
		self.pushButton_4 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_4.setStyleSheet(_fromUtf8(""))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout.addWidget(self.pushButton_4, 0, 4, 1, 2)
		self.pushButton_5 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.gridLayout.addWidget(self.pushButton_5, 0, 6, 1, 1)
		self.pushButton_6 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.gridLayout.addWidget(self.pushButton_6, 0, 7, 1, 2)
		self.pushButton_7 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.gridLayout.addWidget(self.pushButton_7, 0, 9, 1, 1)
		self.pushButton_14 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
		self.gridLayout.addWidget(self.pushButton_14, 0, 10, 1, 1)
		self.pushButton_8 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)
		self.pushButton_9 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 2)
		self.pushButton_10 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 2)
		self.pushButton_11 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.gridLayout.addWidget(self.pushButton_11, 1, 5, 1, 2)
		self.pushButton_12 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.gridLayout.addWidget(self.pushButton_12, 1, 7, 1, 1)
		self.pushButton_13 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
		self.gridLayout.addWidget(self.pushButton_13, 1, 8, 1, 2)
		self.pushButton_15 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
		self.gridLayout.addWidget(self.pushButton_15, 1, 10, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_4, 3, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 20))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuArquivo = QtGui.QMenu(self.menubar)
		self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
		self.menuFormatar = QtGui.QMenu(self.menubar)
		self.menuFormatar.setObjectName(_fromUtf8("menuArquivo"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionSalvar = QtGui.QAction(MainWindow)
		self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
		self.actionNovo = QtGui.QAction(MainWindow)
		self.actionNovo.setObjectName(_fromUtf8("actionNovo"))
		self.actionSalvar_Como = QtGui.QAction(MainWindow)
		self.actionSalvar_Como.setObjectName(_fromUtf8("actionSalvar_Como"))
		self.actionSair = QtGui.QAction(MainWindow)
		self.actionSair.setObjectName(_fromUtf8("actionSair"))
		self.actionFonte = QtGui.QAction(MainWindow)
		self.actionFonte.setObjectName(_fromUtf8("actionFonte"))
		self.menuArquivo.addAction(self.actionNovo)
		self.menuArquivo.addAction(self.actionSalvar)
		self.menuArquivo.addAction(self.actionSalvar_Como)
		self.menuArquivo.addAction(self.actionSair)
		self.menuFormatar.addAction(self.actionFonte)
		self.menubar.addAction(self.menuArquivo.menuAction())
		self.menubar.addAction(self.menuFormatar.menuAction())

		# Adicionando evento 'clicked.connect' aos botões da janela
		# =========================================================
		self.pushButton.clicked.connect(lambda: Handler.InsertTag(u"<b></b>", True))
		self.pushButton_2.clicked.connect(lambda: Handler.InsertTag(u"<i></i>", True))
		self.pushButton_3.clicked.connect(lambda: Handler.InsertTag(u"<u></u>", True))
		self.pushButton_4.clicked.connect(lambda: Handler.InsertTag(u"<del></del>", True))
		self.pushButton_5.clicked.connect(lambda: Handler.InsertTag(u"<img class=\"img-responsive\" src=\"INSIRA O CAMINHO DA IMAGEM AQUI\" alt=\"NOME DA IMAGEM\"></img>", True))
		self.pushButton_6.clicked.connect(lambda: Handler.InsertTag(u"<a href=\"INSIRA O LINK AQUI\" target=\"_blank\"></a>", True))
		self.pushButton_7.clicked.connect(lambda: Handler.InsertTag(u"<p></p>", True))
		self.pushButton_8.clicked.connect(lambda: Handler.InsertTag(u"<h1></h1>", True))
		self.pushButton_9.clicked.connect(lambda: Handler.InsertTag(u"<h2></h2>", True))
		self.pushButton_10.clicked.connect(lambda: Handler.InsertTag(u"<h3></h3>", True))
		self.pushButton_11.clicked.connect(lambda: Handler.InsertTag(u"<center></center>", False))
		self.pushButton_12.clicked.connect(lambda: Handler.InsertTag(u"<video><source src=\"INSIRA O CAMINHO DO VÍDEO AQUI\" type=\"video/mp4\"></video>", True))
		self.pushButton_13.clicked.connect(lambda: Handler.InsertTag(u"<audio><source src=\"INSIRA O CAMINHO DO ÁUDIO AQUI\" type=\"audio/mpeg\"></audio>", True))
		self.pushButton_14.clicked.connect(lambda: Handler.InsertTag(u"<br>", True))
		self.pushButton_15.clicked.connect(lambda: Handler.InsertTag(u"<hr>", True))

		# Adicionando evento 'triggered.connect' aos menus da janela
		# ==========================================================
		self.actionNovo.triggered.connect(Handler.Clear)
		self.actionSair.triggered.connect(Handler.ExitProgram)
		self.actionSalvar.triggered.connect(Handler.Save)
		self.actionSalvar_Como.triggered.connect(Handler.SaveAs)
		self.actionFonte.triggered.connect(Handler.ChangeFont)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Criador de Postagens - v%s" % (GlobalVars.Version), None))
		self.groupBox.setTitle(_translate("MainWindow", "Título", None))
		self.groupBox_2.setTitle(_translate("MainWindow", "Subtítulo", None))
		self.groupBox_3.setTitle(_translate("MainWindow", "Postagem", None))
		self.groupBox_4.setTitle(_translate("MainWindow", "Ferramentas de Postagem", None))
		self.pushButton.setText(_translate("MainWindow", "B", None))
		self.pushButton_2.setText(_translate("MainWindow", "i", None))
		self.pushButton_3.setText(_translate("MainWindow", "u", None))
		self.pushButton_4.setText(_translate("MainWindow", "<del>", None))
		self.pushButton_5.setText(_translate("MainWindow", "<img>", None))
		self.pushButton_6.setText(_translate("MainWindow", "<a>", None))
		self.pushButton_7.setText(_translate("MainWindow", "<p>", None))
		self.pushButton_14.setText(_translate("MainWindow", "<br>", None))
		self.pushButton_8.setText(_translate("MainWindow", "<h1>", None))
		self.pushButton_9.setText(_translate("MainWindow", "<h2>", None))
		self.pushButton_10.setText(_translate("MainWindow", "<h3>", None))
		self.pushButton_11.setText(_translate("MainWindow", "<center>", None))
		self.pushButton_12.setText(_translate("MainWindow", "<video>", None))
		self.pushButton_13.setText(_translate("MainWindow", "<audio>", None))
		self.pushButton_15.setText(_translate("MainWindow", "<hr>", None))
		self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
		self.menuFormatar.setTitle(_translate("MainWindow", "Formatar", None))
		self.actionNovo.setText(_translate("MainWindow", "Novo", None))
		self.actionSalvar.setText(_translate("MainWindow", "Salvar", None))
		self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como...", None))
		self.actionSair.setText(_translate("MainWindow", "Sair", None))
		self.actionFonte.setText(_translate("MainWindow", "Fonte...", None))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	
	# Os métodos do programa serão definidos pelo Handler
	# ---------------------------------------------------
	Handler = WindowHandler(ui, MainWindow)

	# Definindo locale do programa
	# ----------------------------
	translator = QtCore.QTranslator()
	locale = QtCore.QLocale.system().name()
	translator.load('qt_%s' % locale, 
		QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
	app.installTranslator(translator)
	
	ui.setupUi(MainWindow, Handler)
	MainWindow.show()
	sys.exit(app.exec_())