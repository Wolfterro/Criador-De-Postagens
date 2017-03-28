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

from __future__ import print_function
from PyQt4 import QtCore, QtGui
from os.path import expanduser

import os
import sys
import cgi
import ctypes
import hashlib
import datetime
import platform

# Imports do programa
# ===================
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

# Determinando a pasta 'home' do usuário.
# !!! NÃO-IMPLEMENTADO AINDA !!!
# =======================================
if platform.system() == "Windows":
	buf = ctypes.create_unicode_buffer(1024)
	ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
	home_dir = buf.value
else:
	home_dir = expanduser("~")

# Classe de métodos da janela principal do programa
# =================================================
class WindowHandler(object):
	# Obtendo o objeto da janela principal do programa
	# ================================================
	def __init__(self, ui, MainWindow):
		self.ui = ui
		self.MainWindow = MainWindow
		self.Filename = ""
		self.CheckModelFile()

	# Adicionando tags ao texto principal
	# ===================================
	def InsertTag(self, Tag, isNewLine):
		if isNewLine:
			self.ui.textEdit.insertPlainText("%s\n" % (Tag))
		else:
			self.ui.textEdit.insertPlainText(Tag)

	# Limpando todos os campos e zerando nome de arquivo para um novo post
	# ====================================================================
	def Clear(self):
		self.ui.textEdit.clear()
		self.ui.lineEdit.clear()
		self.ui.lineEdit_2.clear()
		self.Filename = ""
		self.ShowOpenedFilename(False)

	# Gerando texto automático para inserir como identificador no arquivo .html
	# =========================================================================
	def GenerateAutoText(self):
		return u"Página HTML gerada pelo Criador de Postagens - v%s -#-#- Timestamp: %s - %s" % (GlobalVars.Version,
			datetime.datetime.now().strftime("%d/%m/%Y"),
			datetime.datetime.now().strftime("%H:%M:%S"))

	# Gerando data formatada para inserir no arquivo .html
	# ====================================================
	def GenerateFormattedData(self):
		return "%s" % (datetime.datetime.now().strftime("%d/%m/%Y"))

	# Mostrando o arquivo aberto no título da janela
	# ==============================================
	def ShowOpenedFilename(self, isOpened):
		if isOpened:
			self.MainWindow.setWindowTitle(_translate("MainWindow", "Criador de Postagens - v%s - %s" % (GlobalVars.Version,
				self.Filename), None))
		else:
			self.MainWindow.setWindowTitle(_translate("MainWindow", "Criador de Postagens - v%s" % (GlobalVars.Version), None))

	# Salvando em um novo arquivo .html
	# =================================
	def SaveAs(self):
		Title, SubTitle, GeneratedText, FormattedData, MainPost = self.GetValues()
		
		self.ChosenFilename = QtGui.QFileDialog.getSaveFileName(None, "Salvar como", "", u"Página da Web (*.html)")

		if self.ChosenFilename != "":
			self.Filename = self.ChosenFilename
			self.SaveMethod(Title, SubTitle, GeneratedText, FormattedData, MainPost)
			self.ShowOpenedFilename(True)

	# Salvando arquivo .html aberto no programa
	# =========================================
	def Save(self):
		if self.Filename != "":
			Title, SubTitle, GeneratedText, FormattedData, MainPost = self.GetValues()
			self.SaveMethod(Title, SubTitle, GeneratedText, FormattedData, MainPost)
		else:
			self.SaveAs()

	# Método comum para salvamento de arquivo
	# =======================================
	def SaveMethod(self, Title, SubTitle, GeneratedText, FormattedData, MainPost):
		FileModel = open("model.html", "r")
		ModelText = FileModel.read()
		FileModel.close()

		ModelText = ModelText.replace("[####TÍTULO####]", Title)				# Inserindo título
		ModelText = ModelText.replace("[####TEXTO-GERADO####]", GeneratedText)	# Inserindo texto gerado
		ModelText = ModelText.replace("[####DATAFORMATADA####]", FormattedData)	# Inserindo data formatada
		ModelText = ModelText.replace("[####SUBTÍTULO####]", SubTitle)			# Inserindo subtítulo
		ModelText = ModelText.replace("[####POSTAGEM-PRINCIPAL####]", MainPost)	# Inserindo post principal

		SavedFile = open(unicode(self.Filename), "w")
		SavedFile.write(ModelText)
		SavedFile.close()

	# Resgatando os valores do programa
	# =================================
	def GetValues(self):
		Title = cgi.escape(self.ui.lineEdit.text())
		SubTitle = cgi.escape(self.ui.lineEdit_2.text())
		GeneratedText = self.GenerateAutoText()
		FormattedData = self.GenerateFormattedData()
		MainPost = self.ui.textEdit.toPlainText().replace("\n", "\n\t\t\t\t\t")

		return [Title, SubTitle, GeneratedText, FormattedData, MainPost]

	# Saindo do programa
	# ==================
	def ExitProgram(self):
		sys.exit(0)

	# Diálogo para alterar a fonte do campo de postagem (self.ui.textEdit)
	# ====================================================================
	def ChangeFont(self):
		FontDialog = QtGui.QFontDialog()
		FontDialog.setWindowIcon(QtGui.QIcon("Icon.ico"))
		SelectedFont, isOK = FontDialog.getFont(self.ui.textEdit)

		if isOK:
			self.ui.textEdit.setFont(SelectedFont)

	# Verificando o arquivo modelo para criar a postagem
	# ==================================================
	def CheckModelFile(self):
		if os.path.isfile("model.html"):
			fileMD5 = hashlib.md5(open("model.html", 'rb').read()).hexdigest()
			
			if fileMD5 != GlobalVars.ModelFileMD5:
				self.ShowMessageBox(u"Erro!", 
					QtGui.QMessageBox.Critical, 
					u"Erro de checksum MD5 no arquivo modelo!", 
					u"O programa não poderá funcionar se o arquivo modelo 'model.html' estiver alterado ou corrompido!",
					QtGui.QMessageBox.Ok,
					5)
		else:
			self.ShowMessageBox(u"Erro!", 
					QtGui.QMessageBox.Critical, 
					u"Arquivo modelo não existe!", 
					u"O programa não poderá funcionar se o arquivo modelo 'model.html' não estiver presente!",
					QtGui.QMessageBox.Ok,
					4)

	# Mostrando uma janela de aviso para o usuário apenas com o botão OK.
	# Caso o valor de fechamento seja diferente de zero, o programa irá encerrar!
	# ===========================================================================
	def ShowMessageBox(self, WindowTitle, IconType, Text, InfoText, CloseType, CloseVal):
		msg = QtGui.QMessageBox()
		msg.setIcon(IconType)
		msg.setWindowIcon(QtGui.QIcon("Icon.ico"))

		msg.setText(Text)
		msg.setInformativeText(InfoText)
		msg.setWindowTitle(WindowTitle)
		msg.setStandardButtons(CloseType)
		msg.exec_()
		
		if CloseVal != 0:
			sys.exit(CloseVal)