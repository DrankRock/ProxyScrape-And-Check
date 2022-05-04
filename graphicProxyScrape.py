# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toggleProxyScrape = QtWidgets.QPushButton(self.centralwidget)
        self.toggleProxyScrape.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.toggleProxyScrape.setObjectName("toggleProxyScrape")
        self.gridLayout_2.addWidget(self.toggleProxyScrape, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ThreadsLabel = QtWidgets.QLabel(self.centralwidget)
        self.ThreadsLabel.setMinimumSize(QtCore.QSize(71, 17))
        font = QtGui.QFont()
        font.setFamily("Manjari Bold")
        self.ThreadsLabel.setFont(font)
        self.ThreadsLabel.setObjectName("ThreadsLabel")
        self.horizontalLayout_3.addWidget(self.ThreadsLabel)
        self.numberOfThreads = QtWidgets.QSpinBox(self.centralwidget)
        self.numberOfThreads.setMinimumSize(QtCore.QSize(351, 31))
        self.numberOfThreads.setMinimum(1)
        self.numberOfThreads.setMaximum(10000)
        self.numberOfThreads.setProperty("value", 50)
        self.numberOfThreads.setObjectName("numberOfThreads")
        self.horizontalLayout_3.addWidget(self.numberOfThreads)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TimeoutLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeoutLabel.setMinimumSize(QtCore.QSize(71, 17))
        font = QtGui.QFont()
        font.setFamily("Manjari Bold")
        self.TimeoutLabel.setFont(font)
        self.TimeoutLabel.setObjectName("TimeoutLabel")
        self.horizontalLayout_2.addWidget(self.TimeoutLabel)
        self.timeout = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timeout.setMinimumSize(QtCore.QSize(350, 31))
        self.timeout.setMaximum(1000.0)
        self.timeout.setProperty("value", 10.0)
        self.timeout.setObjectName("timeout")
        self.horizontalLayout_2.addWidget(self.timeout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.TestingWebsiteLabel = QtWidgets.QLabel(self.centralwidget)
        self.TestingWebsiteLabel.setMinimumSize(QtCore.QSize(400, 17))
        font = QtGui.QFont()
        font.setFamily("Manjari Bold")
        self.TestingWebsiteLabel.setFont(font)
        self.TestingWebsiteLabel.setObjectName("TestingWebsiteLabel")
        self.gridLayout_2.addWidget(self.TestingWebsiteLabel, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.websiteTxt = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.websiteTxt.sizePolicy().hasHeightForWidth())
        self.websiteTxt.setSizePolicy(sizePolicy)
        self.websiteTxt.setMinimumSize(QtCore.QSize(441, 31))
        font = QtGui.QFont()
        font.setFamily("Manjari Bold")
        self.websiteTxt.setFont(font)
        self.websiteTxt.setObjectName("websiteTxt")
        self.gridLayout.addWidget(self.websiteTxt, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(441, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.statusWindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusWindow.sizePolicy().hasHeightForWidth())
        self.statusWindow.setSizePolicy(sizePolicy)
        self.statusWindow.setMinimumSize(QtCore.QSize(441, 31))
        self.statusWindow.setStyleSheet("color: rgb(211, 215, 207);\n"
"background-color: rgb(46, 52, 54);")
        self.statusWindow.setReadOnly(True)
        self.statusWindow.setObjectName("statusWindow")
        self.gridLayout.addWidget(self.statusWindow, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.proxyListWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.proxyListWindow.setMinimumSize(QtCore.QSize(310, 231))
        self.proxyListWindow.setReadOnly(False)
        self.proxyListWindow.setObjectName("proxyListWindow")
        self.horizontalLayout.addWidget(self.proxyListWindow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(120, 25))
        self.cancelButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout_2.addWidget(self.cancelButton)
        self.loadProxiesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadProxiesBtn.setMinimumSize(QtCore.QSize(120, 25))
        self.loadProxiesBtn.setObjectName("loadProxiesBtn")
        self.verticalLayout_2.addWidget(self.loadProxiesBtn)
        self.outputFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.outputFileBtn.setMinimumSize(QtCore.QSize(120, 25))
        self.outputFileBtn.setObjectName("outputFileBtn")
        self.verticalLayout_2.addWidget(self.outputFileBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setMinimumSize(QtCore.QSize(120, 25))
        self.runButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.runButton.setObjectName("runButton")
        self.verticalLayout_2.addWidget(self.runButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSources = QtWidgets.QAction(MainWindow)
        self.actionSources.setObjectName("actionSources")
        self.actionScraping = QtWidgets.QAction(MainWindow)
        self.actionScraping.setObjectName("actionScraping")
        self.actionChecking = QtWidgets.QAction(MainWindow)
        self.actionChecking.setObjectName("actionChecking")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuSettings.addAction(self.actionScraping)
        self.menuSettings.addAction(self.actionChecking)
        self.menuSettings.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProxyScrape - v0.1"))
        self.toggleProxyScrape.setText(_translate("MainWindow", "Scraped Proxies ON"))
        self.ThreadsLabel.setText(_translate("MainWindow", "Threads"))
        self.TimeoutLabel.setText(_translate("MainWindow", "Timeout"))
        self.TestingWebsiteLabel.setText(_translate("MainWindow", "Testing Website :"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.loadProxiesBtn.setText(_translate("MainWindow", "Load Proxies"))
        self.outputFileBtn.setText(_translate("MainWindow", "Output File"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.menuSettings.setTitle(_translate("MainWindow", "Preferences"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSources.setText(_translate("MainWindow", "Preferences"))
        self.actionScraping.setText(_translate("MainWindow", "Scraping"))
        self.actionChecking.setText(_translate("MainWindow", "Checking"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.statusWindow.setPlainText(_translate("MainWindow", "Please chose parameters before running ..."))
        self.websiteTxt.setPlainText(_translate("MainWindow", "https://www.google.com/"))