import sys, argparse, time, signal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal

from graphicProxyScrape import Ui_MainWindow
from proxyScrapeAndCheck import proxyClass

#=############################################################=#
# ----------------------- WORKER SIGNAL ---------------------- #

class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.

    console
    	string console display

    progress
        int use of the progressBar
    end
    	int, int for an ending window

    '''
    progress = pyqtSignal(int)
    end = pyqtSignal(int, int)
    console = pyqtSignal(str)
    proxies = pyqtSignal(list)

#=############################################################=#
# ------------------------ WORKER CLASS ---------------------- #
# I followed https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
# This tutorial. To avoid pyqt5 freezes.
class Worker(QtCore.QRunnable):
	'''
	Worker thread
	'''
	def __init__(self, nProxiesThreads, website, timeout, getProxiesFromScraping, proxyList, outputFile):
		super(Worker, self).__init__()

		self.nProxiesThreads = nProxiesThreads
		self.website = website
		self.timeout = timeout
		self.getProxiesFromScraping = getProxiesFromScraping
		self.proxyList = proxyList
		self.outputFile = outputFile

		self.signals = WorkerSignals()

	def run(self):
		self.myProxyClass = proxyClass(self.nProxiesThreads, self.website, self.timeout, self.getProxiesFromScraping, self.proxyList, signals=self.signals, output=self.outputFile)
		self.myProxyClass.checkProxies()
		self.signals.progress.emit(-4)

	def terminate(self):
		self.myProxyClass.terminate()
		
			

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, arguments, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)

		self.consoleArguments = arguments
		# self.readArguments()

		self.nThreads = 0
		self.nProxy = 0
		self.nProxiesThreads = 0
		self.outputFolderPath = ''
		self.outputFile = ""
		self.proxycraping = True
		self.threadpool = QtCore.QThreadPool()

		self.loadProxiesBtn.clicked.connect(self.inputFileDialog)
		self.outputFileBtn.clicked.connect(self.outputFileDialog)
		self.toggleProxyScrape.clicked.connect(self.toggleScraping)
		self.runButton.clicked.connect(self.run)
		self.cancelButton.clicked.connect(self.cancel)

		self.DEBUG = False

	def readArguments(self):
		'''
		ap.add_argument("-i", "--input", required=False, nargs='+', type=str, help="file containing http/https proxies to check (one or more arguments)")
		ap.add_argument("-l", "--logfile", required=False, default=False, nargs='?', type=bool, help="Set the output to a logfile (default = False)")
		ap.add_argument("-nc", "--nocheck", required=False, action="store_true", help="De-Activate proxies checking")
		ap.add_argument("-ns", "--noscrape", required=False, action="store_true", help="De-Activate proxies scraping")
		ap.add_argument("-o", "--output", required=False, nargs='?', type=str, help="select an output file for working proxies")
		ap.add_argument("-te", "--terminal", required=False, action="store_true", help="launch the terminal version")
		ap.add_argument("-th", "--threads", required=False, default=50, nargs='?', type=int, help="number of threads (default = 50)")
		ap.add_argument("-ti", "--timeout", required=False, default=10, nargs='?', type=int, help="timeout (default = 10)")
		ap.add_argument("-w", "--website", required=False, default="https://www.google.com", nargs='?', type=str, help="website used for checking (default = 'https://www.google.com)'")

		'''
		self.ConsolenThreads = self.consoleArguments.threads
		self.ConsoletimeoutValue = self.consoleArguments.timeout
		self.Consolewebsite = self.consoleArguments.website
		self.Consoleinputs=self.consoleArguments.input
		self.ConsoleLogfile = consoleArguments.logfile
		self.ConsoleNoCheck = consoleArguments.nocheck
		if self.consoleArguments.noscrape :
			self.ConsoleNoScrape = True

	def cancel(self):
		try:
			self.worker.terminate()
			self.statusWindow.setPlainText("Execution cancelled.")
		except:
			self.statusWindow.setPlainText("Error while cancelling. Has it started ?")
			
		self.unlockAll()
		self.progressBar.setValue(0)
		
	def toggleScraping(self):
		if self.proxycraping == True:
			self.proxycraping = False
			self.toggleProxyScrape.setStyleSheet("background-color: rgb(204, 0, 0);")
			self.toggleProxyScrape.setText("Scraped Proxies OFF")
		else : 
			self.proxycraping = True
			self.toggleProxyScrape.setStyleSheet("background-color: rgb(115, 210, 22);")
			self.toggleProxyScrape.setText("Scraped Proxies ON")

	def inputFileDialog(self):
		self.fileDialog = QFileDialog()
		options = self.fileDialog.Options()
		options |= self.fileDialog.DontUseNativeDialog
		#options |= self.fileDialog.setDefaultSuffix(self.fileDialog, "csv")
		#filename, _ = self.fileDialog.getOpenFileName(self, 'Open File', '.')
		fileName, _ = self.fileDialog.getOpenFileName(self,"Chose desired input file",".","", options=options)
		if fileName:
			with open(fileName, 'r') as f:
				currentText = self.proxyListWindow.toPlainText().split("\n")
				lines = [line.rstrip() for line in f]
				currentText.extend(lines)
				currentText = sorted(set(currentText))

				self.proxyListWindow.setPlainText("\n".join(currentText))

	def outputFileDialog(self):
		self.fileDialog = QFileDialog()
		options = self.fileDialog.Options()
		options |= self.fileDialog.DontUseNativeDialog
		#options |= self.fileDialog.setDefaultSuffix(self.fileDialog, "csv")
		#filename, _ = self.fileDialog.getOpenFileName(self, 'Open File', '.')
		fileName, _ = self.fileDialog.getSaveFileName(self,"Chose or create desired output file",self.outputFolderPath,"", options=options)
		if fileName:
			# print(fileName)
			self.outputFile = fileName

	def update_progress(self,n):
		if n == -1:
			# Proxies !
			self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid rgb(19, 148, 195);\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(56, 188, 236);\n"
"    width: 10px;\n"
"}")
		elif n == -2:
			# Scraper !
			self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid rgb(139, 28, 59);\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(172, 35, 72);\n"
"    width: 10px;\n"
"}")
		elif n == -3:
			self.proxyListWindow.setPlainText("")
		elif n == -4:
			self.unlockAll()
		else:
			self.progressBar.setValue(n)

	def update_console(self,toPrint):
		self.statusWindow.setPlainText(toPrint)
		if self.DEBUG == True:
			print(toPrint)
		QtWidgets.QApplication.processEvents()

	def updateProxyList(self, proxyList):
		currentText = self.proxyListWindow.toPlainText()
		if currentText != "":
			currentText=currentText+"\n"
		for elem in proxyList:
			currentText = currentText+elem+"\n"
		self.proxyListWindow.setText(currentText)
		QtWidgets.QApplication.processEvents()

	def endQMessageBox(self, worked, total):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setInformativeText("Successfully scraped {} out of {} links.".format(worked, total))
		msg.setWindowTitle("CMScrape - Info")
		msg.exec_()

	def lock(self, obj):
		obj.setReadOnly(True)
		obj.setStyleSheet("background-color: rgb(186, 189, 182);")
	def unlock(self, obj):
		obj.setReadOnly(False)
		obj.setStyleSheet("background-color: rgb(255, 255, 255);")

	def lockAll(self):
		self.lock(self.timeout)
		self.lock(self.websiteTxt)
		self.lock(self.numberOfThreads)
	def unlockAll(self):
		self.unlock(self.timeout)
		self.unlock(self.websiteTxt)
		self.unlock(self.numberOfThreads)

	def printRunDetail(self):
		print("Starting ProxyScrape with parameters :")
		print("--- Threads : {}\n--- Website : {}\n--- Timeout : {}\n".format(self.numberOfThreads.value(), self.websiteTxt.toPlainText(), self.timeout.value()))

	def run(self):
		self.lockAll()
		self.printRunDetail()
		self.proxieList = self.proxyListWindow.toPlainText().split("\n")
		self.worker = Worker(self.numberOfThreads.value(), self.websiteTxt.toPlainText(), self.timeout.value(), self.proxycraping, self.proxieList, self.outputFile)
		self.threadpool.start(self.worker)
		self.worker.signals.progress.connect(self.update_progress)
		self.worker.signals.console.connect(self.update_console)
		self.worker.signals.end.connect(self.endQMessageBox)
		self.worker.signals.proxies.connect(self.updateProxyList)

#=############################################################=#
# ------------------------- GRAPHIC -------------------------- #

# Print with the [ctime] - {str}
def printT(string):
	print("[{}] - {}.".format(time.ctime(), string))

def terminal(args):
	def executionInterrupted(sig, frame):
		printT("Interrupting execution ...")
		myProxyClass.terminate()
		sys.exit(0)

	printT("Starting terminal version of ProxyScrape.")
	signal.signal(signal.SIGINT, executionInterrupted)
	signal.signal(signal.SIGTERM, executionInterrupted)


	initialProxies = []
	# If there are some inputs
	if args.input != [] and args.input != None :
		for files in args.input :
			with open(files, 'r') as f :
				lines = [line.rstrip() for line in f]
				initialProxies.extend(lines)

	if args.output :
		myProxyClass = proxyClass(int(args.threads), args.website, int(args.timeout), bool(not args.noscrape), initialProxies, gui=False, output=args.output)
	else :
		myProxyClass = proxyClass(int(args.threads), args.website, int(args.timeout), bool(not args.noscrape), initialProxies, gui=False)

	# not done args : input, logfile, output
	if not args.nocheck :
		printT("Cheking proxies")
		myProxyClass.checkProxies()

def arguments():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input", required=False, nargs='+', type=str, help="file containing http/https proxies to check (one or more arguments)")
	ap.add_argument("-l", "--logfile", required=False, default=False, nargs='?', type=bool, help="Set the output to a logfile (default = False)")
	ap.add_argument("-nc", "--nocheck", required=False, action="store_true", help="De-Activate proxies checking")
	ap.add_argument("-ns", "--noscrape", required=False, action="store_true", help="De-Activate proxies scraping")
	ap.add_argument("-o", "--output", required=False, nargs='?', type=str, help="select an output file for working proxies")
	ap.add_argument("-te", "--terminal", required=False, action="store_true", help="launch the terminal version")
	ap.add_argument("-th", "--threads", required=False, default=50, nargs='?', type=int, help="number of threads (default = 50)")
	ap.add_argument("-ti", "--timeout", required=False, default=10, nargs='?', type=int, help="timeout (default = 10)")
	ap.add_argument("-w", "--website", required=False, default="https://www.google.com", nargs='?', type=str, help="website used for checking (default = 'https://www.google.com)'")
	args = ap.parse_args()
	return args

def graphic(args):
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow(args)
	main.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	args = arguments()
	if args.terminal :
		# print("Open the damn terminal version!")
		# print("input file(s) : {}".format(args.input))
		terminal(args)
	else :
		print("Graphical Version")
		graphic(args)
    # graphic()