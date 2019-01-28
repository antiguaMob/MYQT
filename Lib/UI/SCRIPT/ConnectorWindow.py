# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\ConnectorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connector(object):
    def setupUi(self, Connector):
        Connector.setObjectName("Connector")
        Connector.resize(338, 257)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Connector.setFont(font)
        Connector.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(Connector)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(3, 0, 331, 210))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.cnt = QtWidgets.QWidget()
        self.cnt.setObjectName("cnt")
        self.user_in = QtWidgets.QLineEdit(self.cnt)
        self.user_in.setGeometry(QtCore.QRect(10, 130, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_in.setFont(font)
        self.user_in.setClearButtonEnabled(False)
        self.user_in.setObjectName("user_in")
        self.pass_in = QtWidgets.QLineEdit(self.cnt)
        self.pass_in.setGeometry(QtCore.QRect(140, 130, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_in.setFont(font)
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pass_in.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pass_in.setClearButtonEnabled(False)
        self.pass_in.setObjectName("pass_in")
        self.port_in = QtWidgets.QLineEdit(self.cnt)
        self.port_in.setGeometry(QtCore.QRect(140, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.port_in.setFont(font)
        self.port_in.setFrame(True)
        self.port_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.port_in.setClearButtonEnabled(False)
        self.port_in.setObjectName("port_in")
        self.buffered = QtWidgets.QCheckBox(self.cnt)
        self.buffered.setEnabled(True)
        self.buffered.setGeometry(QtCore.QRect(230, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.buffered.setFont(font)
        self.buffered.setCheckable(True)
        self.buffered.setChecked(True)
        self.buffered.setAutoRepeat(False)
        self.buffered.setAutoExclusive(False)
        self.buffered.setTristate(False)
        self.buffered.setObjectName("buffered")
        self.host_in = QtWidgets.QLineEdit(self.cnt)
        self.host_in.setGeometry(QtCore.QRect(10, 90, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.host_in.setFont(font)
        self.host_in.setFrame(True)
        self.host_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.host_in.setClearButtonEnabled(False)
        self.host_in.setObjectName("host_in")
        self.comboBox = QtWidgets.QComboBox(self.cnt)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 310, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.trusted = QtWidgets.QCheckBox(self.cnt)
        self.trusted.setEnabled(False)
        self.trusted.setGeometry(QtCore.QRect(230, 130, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.trusted.setFont(font)
        self.trusted.setCheckable(True)
        self.trusted.setChecked(True)
        self.trusted.setAutoRepeat(False)
        self.trusted.setAutoExclusive(False)
        self.trusted.setTristate(False)
        self.trusted.setObjectName("trusted")
        self.driver = QtWidgets.QCheckBox(self.cnt)
        self.driver.setEnabled(False)
        self.driver.setGeometry(QtCore.QRect(230, 50, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.driver.setFont(font)
        self.driver.setCheckable(True)
        self.driver.setChecked(True)
        self.driver.setAutoRepeat(False)
        self.driver.setAutoExclusive(False)
        self.driver.setTristate(False)
        self.driver.setObjectName("driver")
        self.driver_in = QtWidgets.QLineEdit(self.cnt)
        self.driver_in.setEnabled(False)
        self.driver_in.setGeometry(QtCore.QRect(10, 50, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.driver_in.setFont(font)
        self.driver_in.setFrame(True)
        self.driver_in.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.driver_in.setClearButtonEnabled(False)
        self.driver_in.setObjectName("driver_in")
        self.tabWidget.addTab(self.cnt, "")
        self.adv = QtWidgets.QWidget()
        self.adv.setObjectName("adv")
        self.tabWidget.addTab(self.adv, "")
        self.buttons = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttons.setGeometry(QtCore.QRect(70, 210, 190, 47))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttons.setFont(font)
        self.buttons.setStyleSheet("    min-width: 80px;\n"
" min-height: 20px;")
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        Connector.setCentralWidget(self.centralwidget)

        self.retranslateUi(Connector)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Connector)
        Connector.setTabOrder(self.comboBox, self.host_in)
        Connector.setTabOrder(self.host_in, self.port_in)
        Connector.setTabOrder(self.port_in, self.user_in)
        Connector.setTabOrder(self.user_in, self.pass_in)
        Connector.setTabOrder(self.pass_in, self.buffered)

    def retranslateUi(self, Connector):
        _translate = QtCore.QCoreApplication.translate
        Connector.setWindowTitle(_translate("Connector", "SQL CONNECTOR"))
        self.user_in.setToolTip(_translate("Connector", "<html><head/><body><p>Username</p></body></html>"))
        self.user_in.setText(_translate("Connector", "root"))
        self.user_in.setPlaceholderText(_translate("Connector", "User:"))
        self.pass_in.setToolTip(_translate("Connector", "<html><head/><body><p>Password</p></body></html>"))
        self.pass_in.setText(_translate("Connector", "123456"))
        self.pass_in.setPlaceholderText(_translate("Connector", "Password:"))
        self.port_in.setToolTip(_translate("Connector", "<html><head/><body><p>Server PORT</p></body></html>"))
        self.port_in.setText(_translate("Connector", "3306"))
        self.port_in.setPlaceholderText(_translate("Connector", "Port:"))
        self.buffered.setToolTip(_translate("Connector", "<html><head/><body><p>Buffered Connection</p></body></html>"))
        self.buffered.setText(_translate("Connector", "Buffered"))
        self.host_in.setToolTip(_translate("Connector", "<html><head/><body><p>Server / IP</p></body></html>"))
        self.host_in.setText(_translate("Connector", "127.0.0.1"))
        self.host_in.setPlaceholderText(_translate("Connector", "Server/IP:"))
        self.comboBox.setItemText(0, _translate("Connector", "MYSQL (TCP/IP)"))
        self.comboBox.setItemText(1, _translate("Connector", "Microsoft Server (TCP/IP)"))
        self.comboBox.setItemText(2, _translate("Connector", "Postgre SQL (Experimental)"))
        self.trusted.setToolTip(_translate("Connector", "<html><head/><body><p>Trusted Connection</p></body></html>"))
        self.trusted.setText(_translate("Connector", "Trusted"))
        self.driver.setToolTip(_translate("Connector", "<html><head/><body><p>Use server Driver</p></body></html>"))
        self.driver.setText(_translate("Connector", "Use Driver"))
        self.driver_in.setToolTip(_translate("Connector", "<html><head/><body><p>Driver</p></body></html>"))
        self.driver_in.setText(_translate("Connector", "SQL Server Native Client 11.0"))
        self.driver_in.setPlaceholderText(_translate("Connector", "Driver:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cnt), _translate("Connector", "Connection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adv), _translate("Connector", "More"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connector = QtWidgets.QMainWindow()
    ui = Ui_Connector()
    ui.setupUi(Connector)
    Connector.show()
    sys.exit(app.exec_())

