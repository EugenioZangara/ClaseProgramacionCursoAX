# Form implementation generated from reading ui file 'c:\Users\Zangara\Documents\1-CURSO AX\8460 - TÉCNICAS AVANZADAS DE PROGRAMACIÓN\BBDD\.vscode\LaSegura\CapaVista\CRUDAccidentes.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CRUDAccidentes(object):
    def setupUi(self, CRUDAccidentes):
        CRUDAccidentes.setObjectName("CRUDAccidentes")
        CRUDAccidentes.resize(528, 517)
        self.centralwidget = QtWidgets.QWidget(CRUDAccidentes)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.IdAccidente = QtWidgets.QLineEdit(self.centralwidget)
        self.IdAccidente.setGeometry(QtCore.QRect(260, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IdAccidente.setFont(font)
        self.IdAccidente.setObjectName("IdAccidente")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 230, 411, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAgregar = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setObjectName("btnAgregar")
        self.gridLayout.addWidget(self.btnAgregar, 0, 0, 1, 1)
        self.btnBuscar = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setObjectName("btnBuscar")
        self.gridLayout.addWidget(self.btnBuscar, 0, 1, 1, 1)
        self.btnModificar = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnModificar.setFont(font)
        self.btnModificar.setObjectName("btnModificar")
        self.gridLayout.addWidget(self.btnModificar, 0, 2, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout.addWidget(self.btnEliminar, 0, 3, 1, 1)
        self.btnCerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(210, 390, 111, 41))
        self.btnCerrar.setAutoFillBackground(False)
        self.btnCerrar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255,125,100);\n"
"}")
        self.btnCerrar.setObjectName("btnCerrar")
        self.LugarAcc = QtWidgets.QTextEdit(self.centralwidget)
        self.LugarAcc.setGeometry(QtCore.QRect(260, 150, 221, 61))
        self.LugarAcc.setObjectName("LugarAcc")
        self.FechaAcc = QtWidgets.QDateEdit(self.centralwidget)
        self.FechaAcc.setGeometry(QtCore.QRect(260, 80, 171, 31))
        self.FechaAcc.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 9, 1), QtCore.QTime(0, 0, 0)))
        self.FechaAcc.setCalendarPopup(True)
        self.FechaAcc.setCurrentSectionIndex(0)
        self.FechaAcc.setDate(QtCore.QDate(2022, 9, 1))
        self.FechaAcc.setObjectName("FechaAcc")
        CRUDAccidentes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CRUDAccidentes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 26))
        self.menubar.setObjectName("menubar")
        CRUDAccidentes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CRUDAccidentes)
        self.statusbar.setObjectName("statusbar")
        CRUDAccidentes.setStatusBar(self.statusbar)

        self.retranslateUi(CRUDAccidentes)
        QtCore.QMetaObject.connectSlotsByName(CRUDAccidentes)

    def retranslateUi(self, CRUDAccidentes):
        _translate = QtCore.QCoreApplication.translate
        CRUDAccidentes.setWindowTitle(_translate("CRUDAccidentes", "MainWindow"))
        self.label.setText(_translate("CRUDAccidentes", "id Accidente"))
        self.label_2.setText(_translate("CRUDAccidentes", "Fecha Accidentes"))
        self.label_3.setText(_translate("CRUDAccidentes", "Lugar Accidente"))
        self.btnAgregar.setText(_translate("CRUDAccidentes", "Agregar"))
        self.btnBuscar.setText(_translate("CRUDAccidentes", "Buscar"))
        self.btnModificar.setText(_translate("CRUDAccidentes", "Modificar"))
        self.btnEliminar.setText(_translate("CRUDAccidentes", "Eliminar"))
        self.btnCerrar.setText(_translate("CRUDAccidentes", "Salir"))
        self.FechaAcc.setDisplayFormat(_translate("CRUDAccidentes", "dd/MM/yyyy"))
