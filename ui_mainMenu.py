# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(977, 612)
        MainWindow.setStyleSheet(u"")
        self.actionExportExcel = QAction(MainWindow)
        self.actionExportExcel.setObjectName(u"actionExportExcel")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_15 = QGridLayout(self.centralwidget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"/* === TEMA MENU UTAMA: MODERN DASHBOARD === */\n"
"\n"
"/* 1. BACKGROUND UTAMA */\n"
"QWidget {\n"
"    background-color: #f4f7f6; /* Abu-abu sangat muda, biar mata gak sakit */\n"
"    font-family: \"Segoe UI\", \"Roboto\", sans-serif;\n"
"}\n"
"\n"
"/* 2. JUDUL UTAMA (HEADER) */\n"
"QLabel {\n"
"    color: #2c3e50;\n"
"}\n"
"/* Asumsi ada label judul paling atas */\n"
"QLabel#judulMenu { \n"
"    font-size: 28px;\n"
"    font-weight: bold;\n"
"    color: #2c3e50;\n"
"    padding-bottom: 20px;\n"
"}\n"
"\n"
"/* 3. GROUP BOX (CARD STYLE) */\n"
"/* Ini yang bikin rapi saat Full Screen */\n"
"QGroupBox {\n"
"    background-color: #ffffff; /* Kartu Putih */\n"
"    border: 1px solid #dcdde1;\n"
"    border-radius: 15px; /* Sudut membulat */\n"
"    margin-top: 30px; /* Jarak dari atas */\n"
"    font-size: 16px; \n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Judul di tengah */\n"
"    padding: 10px 20px;\n"
"    backgro"
                        "und-color: #ffffff;\n"
"    color: #7f8c8d; /* Warna teks judul kalem */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* Efek saat mouse masuk ke area GroupBox (Opsional) */\n"
"QGroupBox:hover {\n"
"    border: 2px solid #bdc3c7;\n"
"}\n"
"\n"
"/* 4. TOMBOL-TOMBOL (BUTTONS) */\n"
"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    margin: 5px; /* Jarak antar tombol */\n"
"}\n"
"\n"
"/* --- KELOMPOK LINEAR (KIRI) - TEMA BIRU --- */\n"
"/* Pastikan objectName tombol Linear-mu sesuai (btnJacobi, btnSeidel, btnJordan) */\n"
"QPushButton#btnJacobi, QPushButton#btnSeidel, QPushButton#btnJordan {\n"
"    background-color: #eaf6ff; /* Biru Pucat */\n"
"    color: #0984e3;\n"
"    border: 2px solid #eaf6ff;\n"
"}\n"
"QPushButton#btnJacobi:hover, QPushButton#btnSeidel:hover, QPushButton#btnJordan:hover {\n"
"    background-color: #0984e3; /* Jadi Biru Terang */\n"
"    color: white;\n"
"    border: 2px solid #0984e3;\n"
"}\n"
"\n"
"/* --- KELOMPOK"
                        " NON-LINEAR (KANAN) - TEMA ORANYE --- */\n"
"/* Pastikan objectName tombol Non-Linear-mu sesuai (btnBiseksi, btnNewton, btnRegula) */\n"
"QPushButton#btnBiseksi, QPushButton#btnNewton, QPushButton#btnRegula {\n"
"    background-color: #fff0e6; /* Oranye Pucat */\n"
"    color: #e17055;\n"
"    border: 2px solid #fff0e6;\n"
"}\n"
"QPushButton#btnBiseksi:hover, QPushButton#btnNewton:hover, QPushButton#btnRegula:hover {\n"
"    background-color: #e17055; /* Jadi Oranye Terang */\n"
"    color: white;\n"
"    border: 2px solid #e17055;\n"
"}\n"
"\n"
"/* Tombol File/Menu di pojok (jika ada) */\n"
"QMenuBar {\n"
"    background-color: #ffffff;\n"
"    border-bottom: 1px solid #dcdde1;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background-color: #f1f2f6;\n"
"}")
        self.gridLayout = QGridLayout(self.menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.judulMenu = QLabel(self.menu)
        self.judulMenu.setObjectName(u"judulMenu")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.judulMenu.setFont(font)
        self.judulMenu.setTextFormat(Qt.TextFormat.AutoText)
        self.judulMenu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.judulMenu, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter_2 = QSplitter(self.frame_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.persamaanLinear_2 = QLabel(self.splitter_2)
        self.persamaanLinear_2.setObjectName(u"persamaanLinear_2")
        self.persamaanLinear_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.persamaanLinear_2)
        self.btnJacobi = QPushButton(self.splitter_2)
        self.btnJacobi.setObjectName(u"btnJacobi")
        self.splitter_2.addWidget(self.btnJacobi)
        self.btnJordan = QPushButton(self.splitter_2)
        self.btnJordan.setObjectName(u"btnJordan")
        self.splitter_2.addWidget(self.btnJordan)
        self.btnSeidel = QPushButton(self.splitter_2)
        self.btnSeidel.setObjectName(u"btnSeidel")
        self.splitter_2.addWidget(self.btnSeidel)

        self.verticalLayout_3.addWidget(self.splitter_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_4 = QSplitter(self.frame_4)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.persamaanNonLinear_2 = QLabel(self.splitter_4)
        self.persamaanNonLinear_2.setObjectName(u"persamaanNonLinear_2")
        self.persamaanNonLinear_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_4.addWidget(self.persamaanNonLinear_2)
        self.btnBiseksi = QPushButton(self.splitter_4)
        self.btnBiseksi.setObjectName(u"btnBiseksi")
        self.splitter_4.addWidget(self.btnBiseksi)
        self.btnNewton = QPushButton(self.splitter_4)
        self.btnNewton.setObjectName(u"btnNewton")
        self.splitter_4.addWidget(self.btnNewton)
        self.btnRegula = QPushButton(self.splitter_4)
        self.btnRegula.setObjectName(u"btnRegula")
        self.splitter_4.addWidget(self.btnRegula)

        self.gridLayout_2.addWidget(self.splitter_4, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.menu)
        self.pageJacobi = QWidget()
        self.pageJacobi.setObjectName(u"pageJacobi")
        self.pageJacobi.setStyleSheet(u"/* === TEMA JACOBI: BIRU === */\n"
"\n"
"/* Label & Judul */\n"
"QLabel { color: #2d3436; }\n"
"QLabel#labelJudul {\n"
"    font-size: 18px; font-weight: bold; color: #0984e3; /* Judul Biru */\n"
"}\n"
"\n"
"/* GroupBox Container */\n"
"QGroupBox {\n"
"    border: 1px solid #74b9ff; /* Border Biru Muda */\n"
"    border-radius: 8px; margin-top: 25px; background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; left: 15px; color: #0984e3; font-weight: bold;\n"
"}\n"
"\n"
"/* Tabel Input & Hasil */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3; gridline-color: #dfe6e9; selection-background-color: #74b9ff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #e1f0ff; /* Header Biru Pucat */\n"
"    font-weight: bold; border: 1px solid #dfe6e9;\n"
"}\n"
"\n"
"/* Tombol Hitung (Spesifik Jacobi) */\n"
"QPushButton#btnHitung {\n"
"    background-color: #0984e3; color: white; border-radius: 6px; padding: 8px; font-weight: bold;\n"
"}\n"
"QPushButton#btnHitung:hover { backgrou"
                        "nd-color: #74b9ff; }\n"
"QPushButton#btnHitung:pressed { background-color: #00cec9; }\n"
"\n"
"/* Tombol Reset & Kembali */\n"
"QPushButton#btnReset {\n"
"    border: 1px solid #d63031; color: #d63031; border-radius: 6px; padding: 5px;\n"
"}\n"
"QPushButton#btnReset:hover { background-color: #d63031; color: white; }\n"
"QPushButton#btnKembaliJacobi {\n"
"    border: 1px solid #b2bec3; color: #636e72; border-radius: 4px; padding: 4px;\n"
"}")
        self.labelJudul = QLabel(self.pageJacobi)
        self.labelJudul.setObjectName(u"labelJudul")
        self.labelJudul.setGeometry(QRect(160, 0, 616, 29))
        self.labelJudul.setFont(font)
        self.labelJudul.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(self.pageJacobi)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 951, 511))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 60, 441, 221))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.spinOrde = QSpinBox(self.groupBox)
        self.spinOrde.setObjectName(u"spinOrde")
        self.spinOrde.setValue(3)

        self.horizontalLayout_3.addWidget(self.spinOrde)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.btnReset = QPushButton(self.groupBox)
        self.btnReset.setObjectName(u"btnReset")

        self.horizontalLayout_4.addWidget(self.btnReset)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tableInput = QTableWidget(self.groupBox)
        if (self.tableInput.columnCount() < 4):
            self.tableInput.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableInput.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableInput.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableInput.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableInput.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableInput.rowCount() < 3):
            self.tableInput.setRowCount(3)
        self.tableInput.setObjectName(u"tableInput")

        self.verticalLayout_5.addWidget(self.tableInput)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 310, 431, 191))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.inputX0 = QLineEdit(self.groupBox_2)
        self.inputX0.setObjectName(u"inputX0")

        self.verticalLayout_4.addWidget(self.inputX0)

        self.inputToleransi = QLineEdit(self.groupBox_2)
        self.inputToleransi.setObjectName(u"inputToleransi")

        self.verticalLayout_4.addWidget(self.inputToleransi)

        self.inputMaxIter = QSpinBox(self.groupBox_2)
        self.inputMaxIter.setObjectName(u"inputMaxIter")

        self.verticalLayout_4.addWidget(self.inputMaxIter)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.btnHitung = QPushButton(self.groupBox_2)
        self.btnHitung.setObjectName(u"btnHitung")

        self.verticalLayout_6.addWidget(self.btnHitung)

        self.btnKembaliJacobi = QPushButton(self.frame)
        self.btnKembaliJacobi.setObjectName(u"btnKembaliJacobi")
        self.btnKembaliJacobi.setGeometry(QRect(10, 20, 141, 31))

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasil = QTableWidget(self.frame_2)
        if (self.tableHasil.columnCount() < 5):
            self.tableHasil.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableHasil.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableHasil.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableHasil.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableHasil.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableHasil.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableHasil.setObjectName(u"tableHasil")
        self.tableHasil.setGeometry(QRect(10, 70, 451, 201))
        self.tableHasil.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasil.setAlternatingRowColors(True)
        self.tableHasil.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatus = QLabel(self.frame_2)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 300, 451, 181))
        self.txtSolusi = QTextEdit(self.groupBox_3)
        self.txtSolusi.setObjectName(u"txtSolusi")
        self.txtSolusi.setGeometry(QRect(10, 30, 431, 131))
        self.txtSolusi.setReadOnly(True)

        self.horizontalLayout.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pageJacobi)
        self.pageSeidel = QWidget()
        self.pageSeidel.setObjectName(u"pageSeidel")
        self.pageSeidel.setStyleSheet(u"/* === TEMA SEIDEL: HIJAU === */\n"
"\n"
"/* Label & Judul */\n"
"QLabel { color: #2d3436; }\n"
"QLabel#labelJudulSeidel {\n"
"    font-size: 18px; font-weight: bold; color: #00b894; /* Judul Hijau */\n"
"}\n"
"\n"
"/* GroupBox Container */\n"
"QGroupBox {\n"
"    border: 1px solid #55efc4; /* Border Hijau Muda */\n"
"    border-radius: 8px; margin-top: 25px; background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; left: 15px; color: #00b894; font-weight: bold;\n"
"}\n"
"\n"
"/* Tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3; gridline-color: #dfe6e9; selection-background-color: #55efc4;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #e3fff9; /* Header Hijau Pucat */\n"
"    font-weight: bold; border: 1px solid #dfe6e9;\n"
"}\n"
"\n"
"/* Tombol Hitung (Spesifik Seidel) */\n"
"QPushButton#btnHitungSeidel {\n"
"    background-color: #00b894; color: white; border-radius: 6px; padding: 8px; font-weight: bold;\n"
"}\n"
"QPushButton#btnHitungSeidel:hover { "
                        "background-color: #55efc4; }\n"
"QPushButton#btnHitungSeidel:pressed { background-color: #00cec9; }\n"
"\n"
"/* Tombol Reset */\n"
"QPushButton#btnResetSeidel {\n"
"    border: 1px solid #d63031; color: #d63031; border-radius: 6px; padding: 5px;\n"
"}\n"
"QPushButton#btnResetSeidel:hover { background-color: #d63031; color: white; }\n"
"QPushButton#btnKembaliSeidel {\n"
"    border: 1px solid #b2bec3; color: #636e72; border-radius: 4px; padding: 4px;\n"
"}")
        self.layoutWidget_3 = QWidget(self.pageSeidel)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 30, 951, 511))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.layoutWidget_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_10 = QGroupBox(self.frame_13)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 60, 441, 221))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_10)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.spinOrdeSeidel = QSpinBox(self.groupBox_10)
        self.spinOrdeSeidel.setObjectName(u"spinOrdeSeidel")
        self.spinOrdeSeidel.setValue(3)

        self.horizontalLayout_18.addWidget(self.spinOrdeSeidel)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)

        self.btnResetSeidel = QPushButton(self.groupBox_10)
        self.btnResetSeidel.setObjectName(u"btnResetSeidel")

        self.horizontalLayout_17.addWidget(self.btnResetSeidel)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.tableInputSeidel = QTableWidget(self.groupBox_10)
        if (self.tableInputSeidel.columnCount() < 4):
            self.tableInputSeidel.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableInputSeidel.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableInputSeidel.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableInputSeidel.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableInputSeidel.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        if (self.tableInputSeidel.rowCount() < 3):
            self.tableInputSeidel.setRowCount(3)
        self.tableInputSeidel.setObjectName(u"tableInputSeidel")

        self.verticalLayout_17.addWidget(self.tableInputSeidel)

        self.groupBox_11 = QGroupBox(self.frame_13)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 310, 431, 191))
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_14 = QLabel(self.groupBox_11)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_19.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox_11)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_19.addWidget(self.label_15)

        self.label_16 = QLabel(self.groupBox_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_19.addWidget(self.label_16)


        self.horizontalLayout_19.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.inputX0Seidel = QLineEdit(self.groupBox_11)
        self.inputX0Seidel.setObjectName(u"inputX0Seidel")

        self.verticalLayout_20.addWidget(self.inputX0Seidel)

        self.inputTolSeidel = QLineEdit(self.groupBox_11)
        self.inputTolSeidel.setObjectName(u"inputTolSeidel")

        self.verticalLayout_20.addWidget(self.inputTolSeidel)

        self.inputIterSeidel = QSpinBox(self.groupBox_11)
        self.inputIterSeidel.setObjectName(u"inputIterSeidel")

        self.verticalLayout_20.addWidget(self.inputIterSeidel)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)

        self.btnHitungSeidel = QPushButton(self.groupBox_11)
        self.btnHitungSeidel.setObjectName(u"btnHitungSeidel")

        self.verticalLayout_18.addWidget(self.btnHitungSeidel)

        self.btnKembaliSeidel = QPushButton(self.frame_13)
        self.btnKembaliSeidel.setObjectName(u"btnKembaliSeidel")
        self.btnKembaliSeidel.setGeometry(QRect(10, 20, 141, 31))

        self.horizontalLayout_16.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.layoutWidget_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasilSeidel = QTableWidget(self.frame_14)
        if (self.tableHasilSeidel.columnCount() < 5):
            self.tableHasilSeidel.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableHasilSeidel.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableHasilSeidel.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableHasilSeidel.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableHasilSeidel.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableHasilSeidel.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.tableHasilSeidel.setObjectName(u"tableHasilSeidel")
        self.tableHasilSeidel.setGeometry(QRect(10, 70, 451, 201))
        self.tableHasilSeidel.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasilSeidel.setAlternatingRowColors(True)
        self.tableHasilSeidel.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatusSeidel = QLabel(self.frame_14)
        self.labelStatusSeidel.setObjectName(u"labelStatusSeidel")
        self.labelStatusSeidel.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_12 = QGroupBox(self.frame_14)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 300, 451, 181))
        self.txtSolusiSeidel = QTextEdit(self.groupBox_12)
        self.txtSolusiSeidel.setObjectName(u"txtSolusiSeidel")
        self.txtSolusiSeidel.setGeometry(QRect(10, 30, 431, 141))
        self.txtSolusiSeidel.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.frame_14)

        self.labelJudulSeidel = QLabel(self.pageSeidel)
        self.labelJudulSeidel.setObjectName(u"labelJudulSeidel")
        self.labelJudulSeidel.setGeometry(QRect(160, 0, 616, 29))
        self.labelJudulSeidel.setFont(font)
        self.labelJudulSeidel.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudulSeidel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.pageSeidel)
        self.pageJordan = QWidget()
        self.pageJordan.setObjectName(u"pageJordan")
        self.pageJordan.setStyleSheet(u"/* === TEMA JORDAN: UNGU === */\n"
"\n"
"/* Label & Judul */\n"
"QLabel { color: #2d3436; }\n"
"QLabel#labelJudulJordan {\n"
"    font-size: 18px; font-weight: bold; color: #6c5ce7; /* Judul Ungu */\n"
"}\n"
"\n"
"/* GroupBox Container */\n"
"QGroupBox {\n"
"    border: 1px solid #a29bfe; /* Border Ungu Muda */\n"
"    border-radius: 8px; margin-top: 25px; background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; left: 15px; color: #6c5ce7; font-weight: bold;\n"
"}\n"
"\n"
"/* Tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3; gridline-color: #dfe6e9; selection-background-color: #a29bfe;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #f0f0ff; /* Header Ungu Pucat */\n"
"    font-weight: bold; border: 1px solid #dfe6e9;\n"
"}\n"
"\n"
"/* Tombol Hitung (Spesifik Jordan) */\n"
"QPushButton#btnHitungJordan {\n"
"    background-color: #6c5ce7; color: white; border-radius: 6px; padding: 8px; font-weight: bold;\n"
"}\n"
"QPushButton#btnHitungJordan:hover { back"
                        "ground-color: #a29bfe; }\n"
"QPushButton#btnHitungJordan:pressed { background-color: #0984e3; }\n"
"\n"
"/* Tombol Reset */\n"
"QPushButton#btnResetJordan {\n"
"    border: 1px solid #d63031; color: #d63031; border-radius: 6px; padding: 5px;\n"
"}\n"
"QPushButton#btnResetJordan:hover { background-color: #d63031; color: white; }\n"
"QPushButton#btnKembaliJordan {\n"
"    border: 1px solid #b2bec3; color: #636e72; border-radius: 4px; padding: 4px;\n"
"}")
        self.labelJudulJordan = QLabel(self.pageJordan)
        self.labelJudulJordan.setObjectName(u"labelJudulJordan")
        self.labelJudulJordan.setGeometry(QRect(160, 0, 616, 29))
        self.labelJudulJordan.setFont(font)
        self.labelJudulJordan.setStyleSheet(u"")
        self.labelJudulJordan.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudulJordan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget_4 = QWidget(self.pageJordan)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 30, 951, 501))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.layoutWidget_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_13 = QGroupBox(self.frame_15)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 60, 441, 371))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_17 = QLabel(self.groupBox_13)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_22.addWidget(self.label_17)

        self.spinOrdeJordan = QSpinBox(self.groupBox_13)
        self.spinOrdeJordan.setObjectName(u"spinOrdeJordan")
        self.spinOrdeJordan.setValue(3)

        self.horizontalLayout_22.addWidget(self.spinOrdeJordan)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)

        self.btnResetJordan = QPushButton(self.groupBox_13)
        self.btnResetJordan.setObjectName(u"btnResetJordan")

        self.horizontalLayout_21.addWidget(self.btnResetJordan)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)

        self.tableInputJordan = QTableWidget(self.groupBox_13)
        if (self.tableInputJordan.columnCount() < 4):
            self.tableInputJordan.setColumnCount(4)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableInputJordan.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableInputJordan.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableInputJordan.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableInputJordan.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        if (self.tableInputJordan.rowCount() < 3):
            self.tableInputJordan.setRowCount(3)
        self.tableInputJordan.setObjectName(u"tableInputJordan")

        self.verticalLayout_21.addWidget(self.tableInputJordan)

        self.btnKembaliJordan = QPushButton(self.frame_15)
        self.btnKembaliJordan.setObjectName(u"btnKembaliJordan")
        self.btnKembaliJordan.setGeometry(QRect(10, 20, 141, 31))
        self.btnHitungJordan = QPushButton(self.frame_15)
        self.btnHitungJordan.setObjectName(u"btnHitungJordan")
        self.btnHitungJordan.setGeometry(QRect(20, 440, 421, 41))

        self.horizontalLayout_20.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.layoutWidget_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasilJordan = QTableWidget(self.frame_16)
        if (self.tableHasilJordan.columnCount() < 5):
            self.tableHasilJordan.setColumnCount(5)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableHasilJordan.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableHasilJordan.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableHasilJordan.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableHasilJordan.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableHasilJordan.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        self.tableHasilJordan.setObjectName(u"tableHasilJordan")
        self.tableHasilJordan.setGeometry(QRect(10, 70, 451, 201))
        self.tableHasilJordan.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasilJordan.setAlternatingRowColors(True)
        self.tableHasilJordan.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatusJordan = QLabel(self.frame_16)
        self.labelStatusJordan.setObjectName(u"labelStatusJordan")
        self.labelStatusJordan.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_15 = QGroupBox(self.frame_16)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 300, 451, 181))
        self.txtSolusiJordan = QTextEdit(self.groupBox_15)
        self.txtSolusiJordan.setObjectName(u"txtSolusiJordan")
        self.txtSolusiJordan.setGeometry(QRect(10, 30, 431, 141))
        self.txtSolusiJordan.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.pageJordan)
        self.pageBiseksi = QWidget()
        self.pageBiseksi.setObjectName(u"pageBiseksi")
        self.pageBiseksi.setStyleSheet(u"/* === TEMA BISEKSI: ORANYE SUNRISE === */\n"
"\n"
"/* Label & Judul */\n"
"QLabel { color: #2d3436; }\n"
"QLabel#labelJudulBiseksi {\n"
"    font-size: 18px; font-weight: bold; color: #e17055; /* Judul Oranye */\n"
"}\n"
"\n"
"/* GroupBox Container */\n"
"QGroupBox {\n"
"    border: 1px solid #fab1a0; /* Border Peach */\n"
"    border-radius: 8px; margin-top: 25px; background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; left: 15px; color: #e17055; font-weight: bold;\n"
"}\n"
"\n"
"/* Tabel */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3; gridline-color: #dfe6e9; selection-background-color: #fab1a0;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #fff0e6; /* Header Oranye Pucat */\n"
"    font-weight: bold; border: 1px solid #dfe6e9;\n"
"}\n"
"\n"
"/* Tombol Hitung (Spesifik Biseksi) */\n"
"QPushButton#btnHitungBiseksi {\n"
"    background-color: #e17055; color: white; border-radius: 6px; padding: 8px; font-weight: bold;\n"
"}\n"
"QPushButton#btnHitungBisek"
                        "si:hover { background-color: #fab1a0; }\n"
"QPushButton#btnHitungBiseksi:pressed { background-color: #d63031; }\n"
"\n"
"/* Tombol Reset & Kembali */\n"
"QPushButton#btnResetBiseksi {\n"
"    border: 1px solid #d63031; color: #d63031; border-radius: 6px; padding: 5px;\n"
"}\n"
"QPushButton#btnResetBiseksi:hover { background-color: #d63031; color: white; }\n"
"QPushButton#btnKembaliBiseksi {\n"
"    border: 1px solid #b2bec3; color: #636e72; border-radius: 4px; padding: 4px;\n"
"}")
        self.labelJudulBiseksi = QLabel(self.pageBiseksi)
        self.labelJudulBiseksi.setObjectName(u"labelJudulBiseksi")
        self.labelJudulBiseksi.setGeometry(QRect(150, -10, 616, 31))
        self.labelJudulBiseksi.setFont(font)
        self.labelJudulBiseksi.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudulBiseksi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_17 = QFrame(self.pageBiseksi)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 30, 311, 311))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btnKembaliBiseksi = QPushButton(self.frame_17)
        self.btnKembaliBiseksi.setObjectName(u"btnKembaliBiseksi")

        self.gridLayout_6.addWidget(self.btnKembaliBiseksi, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_14 = QGroupBox(self.frame_17)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_3 = QGridLayout(self.groupBox_14)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.groupBox_14)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox_14)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_14)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.inputFungsiBiseksi = QLineEdit(self.groupBox_14)
        self.inputFungsiBiseksi.setObjectName(u"inputFungsiBiseksi")

        self.verticalLayout_7.addWidget(self.inputFungsiBiseksi)

        self.inputABiseksi = QLineEdit(self.groupBox_14)
        self.inputABiseksi.setObjectName(u"inputABiseksi")

        self.verticalLayout_7.addWidget(self.inputABiseksi)

        self.inputBBiseksi = QLineEdit(self.groupBox_14)
        self.inputBBiseksi.setObjectName(u"inputBBiseksi")

        self.verticalLayout_7.addWidget(self.inputBBiseksi)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.frame_17)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_4 = QGridLayout(self.groupBox_16)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.groupBox_16)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox_16)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.inputTolBiseksi = QLineEdit(self.groupBox_16)
        self.inputTolBiseksi.setObjectName(u"inputTolBiseksi")

        self.verticalLayout_10.addWidget(self.inputTolBiseksi)

        self.inputIterBiseksi = QSpinBox(self.groupBox_16)
        self.inputIterBiseksi.setObjectName(u"inputIterBiseksi")

        self.verticalLayout_10.addWidget(self.inputIterBiseksi)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_16, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnHitungBiseksi = QPushButton(self.frame_17)
        self.btnHitungBiseksi.setObjectName(u"btnHitungBiseksi")

        self.horizontalLayout_8.addWidget(self.btnHitungBiseksi)

        self.btnResetBiseksi = QPushButton(self.frame_17)
        self.btnResetBiseksi.setObjectName(u"btnResetBiseksi")

        self.horizontalLayout_8.addWidget(self.btnResetBiseksi)


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.frame_18 = QFrame(self.pageBiseksi)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(317, 30, 631, 521))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasilBiseksi = QTableWidget(self.frame_18)
        if (self.tableHasilBiseksi.columnCount() < 7):
            self.tableHasilBiseksi.setColumnCount(7)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableHasilBiseksi.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        self.tableHasilBiseksi.setObjectName(u"tableHasilBiseksi")
        self.tableHasilBiseksi.setGeometry(QRect(10, 70, 621, 231))
        self.tableHasilBiseksi.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasilBiseksi.setAlternatingRowColors(True)
        self.tableHasilBiseksi.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatusBiseksi = QLabel(self.frame_18)
        self.labelStatusBiseksi.setObjectName(u"labelStatusBiseksi")
        self.labelStatusBiseksi.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_17 = QGroupBox(self.frame_18)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(10, 320, 621, 181))
        self.txtSolusiBiseksi = QTextEdit(self.groupBox_17)
        self.txtSolusiBiseksi.setObjectName(u"txtSolusiBiseksi")
        self.txtSolusiBiseksi.setGeometry(QRect(10, 30, 601, 131))
        self.txtSolusiBiseksi.setReadOnly(True)
        self.stackedWidget.addWidget(self.pageBiseksi)
        self.pageNewtonRapshon = QWidget()
        self.pageNewtonRapshon.setObjectName(u"pageNewtonRapshon")
        self.pageNewtonRapshon.setStyleSheet(u"/* === TEMA NEWTON-RAPHSON: MAGENTA SPEED \U000026a1 === */\n"
"\n"
"/* 1. LABEL & JUDUL */\n"
"QLabel {\n"
"    color: #2d3436;\n"
"}\n"
"/* Judul Halaman */\n"
"QLabel#labelJudulNewtonRaphson {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #e84393; /* Judul Warna Magenta */\n"
"}\n"
"\n"
"/* 2. GROUP BOX (KOTAK KONTAINER) */\n"
"QGroupBox {\n"
"    border: 1px solid #fd79a8; /* Border Pink */\n"
"    border-radius: 8px;\n"
"    margin-top: 25px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"    color: #e84393; /* Judul Group Pink */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* 3. TABEL HASIL */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3;\n"
"    gridline-color: #dfe6e9;\n"
"    selection-background-color: #fd79a8; /* Warna saat baris diklik (Pink) */\n"
"    selection-color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #fff5f7; /* Header Pink Sangat Muda/P"
                        "ucat */\n"
"    color: #2d3436;\n"
"    font-weight: bold;\n"
"    border: 1px solid #dfe6e9;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* 4. INPUT FIELDS (Kotak Ketik) */\n"
"QLineEdit, QSpinBox {\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"/* Saat diklik jadi warna Magenta */\n"
"QLineEdit:focus, QSpinBox:focus {\n"
"    border: 2px solid #e84393; \n"
"    background-color: #fff0f6;\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f680 TOMBOL UTAMA (HITUNG) - MAGENTA\n"
"   ============================================ */\n"
"QPushButton#btnHitungNewton {\n"
"    background-color: #e84393; /* Warna Dasar Magenta */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"QPushButton#btnHitungNewton:hover {\n"
"    background-color: #fd79a8; /* Jadi lebih terang saat didekati mouse */\n"
"}\n"
"QPushButton#btnHitungNewton:pres"
                        "sed {\n"
"    background-color: #d63031; /* Jadi merah saat ditekan */\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f504 TOMBOL RESET - MERAH OUTLINE\n"
"   ============================================ */\n"
"QPushButton#btnResetNewton {\n"
"    background-color: #ffffff;\n"
"    color: #d63031;\n"
"    border: 1px solid #d63031;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnResetNewton:hover {\n"
"    background-color: #d63031;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f519 TOMBOL KEMBALI - ABU-ABU NETRAL\n"
"   ============================================ */\n"
"QPushButton#btnKembaliNewton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 4px;\n"
"    color: #636e72;\n"
"    padding: 4px 10px;\n"
"}\n"
"QPushButton#btnKembaliNewton:hover {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"/"
                        "* 6. KOTAK SOLUSI (HASIL AKHIR) */\n"
"QTextEdit {\n"
"    background-color: #fffdfd; /* Putih kemerahan dikit */\n"
"    border: 1px dashed #fd79a8;\n"
"    border-radius: 6px;\n"
"    font-family: \"Consolas\", monospace;\n"
"}")
        self.labelJudulNewtonRaphson = QLabel(self.pageNewtonRapshon)
        self.labelJudulNewtonRaphson.setObjectName(u"labelJudulNewtonRaphson")
        self.labelJudulNewtonRaphson.setGeometry(QRect(170, -10, 616, 31))
        self.labelJudulNewtonRaphson.setFont(font)
        self.labelJudulNewtonRaphson.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudulNewtonRaphson.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_19 = QFrame(self.pageNewtonRapshon)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(317, 30, 641, 511))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasilNewton = QTableWidget(self.frame_19)
        if (self.tableHasilNewton.columnCount() < 6):
            self.tableHasilNewton.setColumnCount(6)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableHasilNewton.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        self.tableHasilNewton.setObjectName(u"tableHasilNewton")
        self.tableHasilNewton.setGeometry(QRect(10, 70, 621, 231))
        self.tableHasilNewton.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasilNewton.setAlternatingRowColors(True)
        self.tableHasilNewton.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatusNewton = QLabel(self.frame_19)
        self.labelStatusNewton.setObjectName(u"labelStatusNewton")
        self.labelStatusNewton.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_18 = QGroupBox(self.frame_19)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(10, 320, 621, 181))
        self.txtSolusiNewton = QTextEdit(self.groupBox_18)
        self.txtSolusiNewton.setObjectName(u"txtSolusiNewton")
        self.txtSolusiNewton.setGeometry(QRect(10, 30, 601, 131))
        self.txtSolusiNewton.setReadOnly(True)
        self.frame_20 = QFrame(self.pageNewtonRapshon)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 30, 311, 301))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_20)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btnKembaliNewton = QPushButton(self.frame_20)
        self.btnKembaliNewton.setObjectName(u"btnKembaliNewton")

        self.gridLayout_7.addWidget(self.btnKembaliNewton, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_19 = QGroupBox(self.frame_20)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_9 = QGridLayout(self.groupBox_19)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.groupBox_19)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_19)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.inputFungsiNewton = QLineEdit(self.groupBox_19)
        self.inputFungsiNewton.setObjectName(u"inputFungsiNewton")

        self.verticalLayout_12.addWidget(self.inputFungsiNewton)

        self.inputX0Newton = QLineEdit(self.groupBox_19)
        self.inputX0Newton.setObjectName(u"inputX0Newton")

        self.verticalLayout_12.addWidget(self.inputX0Newton)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)


        self.gridLayout_9.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.frame_20)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_10 = QGridLayout(self.groupBox_20)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_18 = QLabel(self.groupBox_20)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_13.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_20)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_13.addWidget(self.label_19)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.inputTolNewton = QLineEdit(self.groupBox_20)
        self.inputTolNewton.setObjectName(u"inputTolNewton")

        self.verticalLayout_14.addWidget(self.inputTolNewton)

        self.inputIterNewton = QSpinBox(self.groupBox_20)
        self.inputIterNewton.setObjectName(u"inputIterNewton")

        self.verticalLayout_14.addWidget(self.inputIterNewton)


        self.horizontalLayout_10.addLayout(self.verticalLayout_14)


        self.gridLayout_10.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_20, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnHitungNewton = QPushButton(self.frame_20)
        self.btnHitungNewton.setObjectName(u"btnHitungNewton")

        self.horizontalLayout_11.addWidget(self.btnHitungNewton)

        self.btnResetNewton = QPushButton(self.frame_20)
        self.btnResetNewton.setObjectName(u"btnResetNewton")

        self.horizontalLayout_11.addWidget(self.btnResetNewton)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageNewtonRapshon)
        self.pageRegula = QWidget()
        self.pageRegula.setObjectName(u"pageRegula")
        self.pageRegula.setStyleSheet(u"/* === TEMA REGULA FALSI: TOSCA OCEAN \U0001f30a === */\n"
"\n"
"/* 1. LABEL & JUDUL */\n"
"QLabel {\n"
"    color: #2d3436;\n"
"}\n"
"/* Judul Halaman - Tosca Gelap */\n"
"QLabel#labelJudulRegula {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #0097e6; \n"
"}\n"
"\n"
"/* 2. GROUP BOX (KOTAK KONTAINER) */\n"
"QGroupBox {\n"
"    border: 1px solid #00a8ff; /* Border Biru Laut */\n"
"    border-radius: 8px;\n"
"    margin-top: 25px;\n"
"    background-color: #ffffff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"    color: #0097e6; /* Judul Group Tosca */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* 3. TABEL HASIL */\n"
"QTableWidget {\n"
"    border: 1px solid #b2bec3;\n"
"    gridline-color: #dfe6e9;\n"
"    selection-background-color: #00a8ff; /* Warna saat baris diklik (Biru Laut) */\n"
"    selection-color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #eaf6ff; /* Header Biru Sangat Muda */\n"
"    c"
                        "olor: #2d3436;\n"
"    font-weight: bold;\n"
"    border: 1px solid #dfe6e9;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* 4. INPUT FIELDS (Kotak Ketik) */\n"
"QLineEdit, QSpinBox {\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"/* Saat diklik jadi warna Tosca */\n"
"QLineEdit:focus, QSpinBox:focus {\n"
"    border: 2px solid #0097e6; \n"
"    background-color: #f0faff;\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f680 TOMBOL UTAMA (HITUNG) - TOSCA\n"
"   ============================================ */\n"
"QPushButton#btnHitungRegula {\n"
"    background-color: #0097e6; /* Warna Dasar Tosca */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"QPushButton#btnHitungRegula:hover {\n"
"    background-color: #00a8ff; /* Lebih terang saat hover */\n"
"}\n"
"QPushButton#btnHitungRegula:pressed {\n"
"    background-color: #0062"
                        "66; /* Hijau tua saat ditekan */\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f504 TOMBOL RESET - MERAH BATA\n"
"   ============================================ */\n"
"QPushButton#btnResetRegula {\n"
"    background-color: #ffffff;\n"
"    color: #c23616; /* Merah Bata */\n"
"    border: 1px solid #c23616;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#btnResetRegula:hover {\n"
"    background-color: #c23616;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ============================================\n"
"   \U0001f519 TOMBOL KEMBALI - ABU-ABU NETRAL\n"
"   ============================================ */\n"
"QPushButton#btnKembaliRegula {\n"
"    background-color: transparent;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 4px;\n"
"    color: #636e72;\n"
"    padding: 4px 10px;\n"
"}\n"
"QPushButton#btnKembaliRegula:hover {\n"
"    background-color: #dfe6e9;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"/* 6. KOTAK SOLUSI (HASIL"
                        " AKHIR) */\n"
"QTextEdit {\n"
"    background-color: #f8fbff; /* Biru super tipis */\n"
"    border: 1px dashed #0097e6;\n"
"    border-radius: 6px;\n"
"    font-family: \"Consolas\", monospace;\n"
"}")
        self.labelJudulRegula = QLabel(self.pageRegula)
        self.labelJudulRegula.setObjectName(u"labelJudulRegula")
        self.labelJudulRegula.setGeometry(QRect(153, -10, 616, 31))
        self.labelJudulRegula.setFont(font)
        self.labelJudulRegula.setTextFormat(Qt.TextFormat.AutoText)
        self.labelJudulRegula.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_21 = QFrame(self.pageRegula)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(317, 30, 641, 511))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.tableHasilRegula = QTableWidget(self.frame_21)
        if (self.tableHasilRegula.columnCount() < 7):
            self.tableHasilRegula.setColumnCount(7)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableHasilRegula.setHorizontalHeaderItem(6, __qtablewidgetitem46)
        self.tableHasilRegula.setObjectName(u"tableHasilRegula")
        self.tableHasilRegula.setGeometry(QRect(10, 70, 621, 231))
        self.tableHasilRegula.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableHasilRegula.setAlternatingRowColors(True)
        self.tableHasilRegula.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.labelStatusRegula = QLabel(self.frame_21)
        self.labelStatusRegula.setObjectName(u"labelStatusRegula")
        self.labelStatusRegula.setGeometry(QRect(10, 20, 431, 31))
        self.groupBox_21 = QGroupBox(self.frame_21)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(10, 320, 621, 181))
        self.txtSolusiRegula = QTextEdit(self.groupBox_21)
        self.txtSolusiRegula.setObjectName(u"txtSolusiRegula")
        self.txtSolusiRegula.setGeometry(QRect(10, 30, 601, 131))
        self.txtSolusiRegula.setReadOnly(True)
        self.frame_22 = QFrame(self.pageRegula)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 30, 311, 341))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.btnKembaliRegula = QPushButton(self.frame_22)
        self.btnKembaliRegula.setObjectName(u"btnKembaliRegula")

        self.gridLayout_11.addWidget(self.btnKembaliRegula, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_22 = QGroupBox(self.frame_22)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_13 = QGridLayout(self.groupBox_22)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.groupBox_22)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_15.addWidget(self.label_12)

        self.label_20 = QLabel(self.groupBox_22)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_15.addWidget(self.label_20)

        self.label_21 = QLabel(self.groupBox_22)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_15.addWidget(self.label_21)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.inputFungsiRegula = QLineEdit(self.groupBox_22)
        self.inputFungsiRegula.setObjectName(u"inputFungsiRegula")

        self.verticalLayout_16.addWidget(self.inputFungsiRegula)

        self.inputARegula = QLineEdit(self.groupBox_22)
        self.inputARegula.setObjectName(u"inputARegula")

        self.verticalLayout_16.addWidget(self.inputARegula)

        self.inputBRegula = QLineEdit(self.groupBox_22)
        self.inputBRegula.setObjectName(u"inputBRegula")

        self.verticalLayout_16.addWidget(self.inputBRegula)


        self.horizontalLayout_12.addLayout(self.verticalLayout_16)


        self.gridLayout_13.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.frame_22)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_14 = QGridLayout(self.groupBox_23)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_22 = QLabel(self.groupBox_23)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_22.addWidget(self.label_22)

        self.label_23 = QLabel(self.groupBox_23)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_22.addWidget(self.label_23)


        self.horizontalLayout_13.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.inputTolRegula = QLineEdit(self.groupBox_23)
        self.inputTolRegula.setObjectName(u"inputTolRegula")

        self.verticalLayout_23.addWidget(self.inputTolRegula)

        self.inputIterRegula = QSpinBox(self.groupBox_23)
        self.inputIterRegula.setObjectName(u"inputIterRegula")

        self.verticalLayout_23.addWidget(self.inputIterRegula)


        self.horizontalLayout_13.addLayout(self.verticalLayout_23)


        self.gridLayout_14.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_23, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_12, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnHitungRegula = QPushButton(self.frame_22)
        self.btnHitungRegula.setObjectName(u"btnHitungRegula")

        self.horizontalLayout_14.addWidget(self.btnHitungRegula)

        self.btnResetRegula = QPushButton(self.frame_22)
        self.btnResetRegula.setObjectName(u"btnResetRegula")

        self.horizontalLayout_14.addWidget(self.btnResetRegula)


        self.gridLayout_11.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageRegula)

        self.gridLayout_15.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 977, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menuFile.addAction(self.actionExportExcel)
        self.menuabout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExportExcel.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Info Kelompok", None))
        self.judulMenu.setText(QCoreApplication.translate("MainWindow", u"Perhitungan Persamaan Linear dan Non Linear", None))
        self.persamaanLinear_2.setText(QCoreApplication.translate("MainWindow", u"Persamaan Linear", None))
        self.btnJacobi.setText(QCoreApplication.translate("MainWindow", u"Metode Jacobi", None))
        self.btnJordan.setText(QCoreApplication.translate("MainWindow", u"Gauss- Jordan", None))
        self.btnSeidel.setText(QCoreApplication.translate("MainWindow", u"Gauss seidel", None))
        self.persamaanNonLinear_2.setText(QCoreApplication.translate("MainWindow", u"Persamaan Non-Linear", None))
        self.btnBiseksi.setText(QCoreApplication.translate("MainWindow", u"Metode Biseksi", None))
        self.btnNewton.setText(QCoreApplication.translate("MainWindow", u"Metode Newton-Raphson", None))
        self.btnRegula.setText(QCoreApplication.translate("MainWindow", u"Regula Falsi", None))
        self.labelJudul.setText(QCoreApplication.translate("MainWindow", u"Metode Jacobi", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Matriks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ukuran n", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset Matriks", None))
        ___qtablewidgetitem = self.tableInput.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem1 = self.tableInput.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem2 = self.tableInput.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem3 = self.tableInput.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"b(hasil)", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Iterasi", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tebakan Awal x0 :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Toleransi Error", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Max Iterasi :", None))
        self.btnHitung.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.btnKembaliJacobi.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        ___qtablewidgetitem4 = self.tableHasil.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem5 = self.tableHasil.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem6 = self.tableHasil.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem7 = self.tableHasil.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem8 = self.tableHasil.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Error Max", None));
        self.labelStatus.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Matriks", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ukuran n", None))
        self.btnResetSeidel.setText(QCoreApplication.translate("MainWindow", u"Reset Matriks", None))
        ___qtablewidgetitem9 = self.tableInputSeidel.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem10 = self.tableInputSeidel.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem11 = self.tableInputSeidel.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem12 = self.tableInputSeidel.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"b(hasil)", None));
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Iterasi", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tebakan Awal x0 :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Toleransi Error", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Max Iterasi :", None))
        self.btnHitungSeidel.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.btnKembaliSeidel.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        ___qtablewidgetitem13 = self.tableHasilSeidel.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem14 = self.tableHasilSeidel.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem15 = self.tableHasilSeidel.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem16 = self.tableHasilSeidel.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem17 = self.tableHasilSeidel.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Error Max", None));
        self.labelStatusSeidel.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.labelJudulSeidel.setText(QCoreApplication.translate("MainWindow", u"Metode Gauss Seidel", None))
        self.labelJudulJordan.setText(QCoreApplication.translate("MainWindow", u"Metode Gauss-Jordan", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Matriks", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Ukuran n", None))
        self.btnResetJordan.setText(QCoreApplication.translate("MainWindow", u"Reset Matriks", None))
        ___qtablewidgetitem18 = self.tableInputJordan.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem19 = self.tableInputJordan.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem20 = self.tableInputJordan.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem21 = self.tableInputJordan.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"b(hasil)", None));
        self.btnKembaliJordan.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.btnHitungJordan.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        ___qtablewidgetitem22 = self.tableHasilJordan.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem23 = self.tableHasilJordan.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem24 = self.tableHasilJordan.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem25 = self.tableHasilJordan.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem26 = self.tableHasilJordan.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Error Max", None));
        self.labelStatusJordan.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.labelJudulBiseksi.setText(QCoreApplication.translate("MainWindow", u"Metode Biseksi", None))
        self.btnKembaliBiseksi.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Input Fungsi dan Batas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fungsi f(x) :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Batas Bawah (a) :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Batas Atas (b) :", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Iterasi", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Toleransi Error :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Max Iterasi :", None))
        self.btnHitungBiseksi.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.btnResetBiseksi.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        ___qtablewidgetitem27 = self.tableHasilBiseksi.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem28 = self.tableHasilBiseksi.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem29 = self.tableHasilBiseksi.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem30 = self.tableHasilBiseksi.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"c (Tengah)", None));
        ___qtablewidgetitem31 = self.tableHasilBiseksi.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"f(c)", None));
        ___qtablewidgetitem32 = self.tableHasilBiseksi.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        ___qtablewidgetitem33 = self.tableHasilBiseksi.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Ket", None));
        self.labelStatusBiseksi.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.labelJudulNewtonRaphson.setText(QCoreApplication.translate("MainWindow", u"Metode Newton-Raphson", None))
        ___qtablewidgetitem34 = self.tableHasilNewton.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem35 = self.tableHasilNewton.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"x(old)", None));
        ___qtablewidgetitem36 = self.tableHasilNewton.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"f(x)", None));
        ___qtablewidgetitem37 = self.tableHasilNewton.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"f'(x)", None));
        ___qtablewidgetitem38 = self.tableHasilNewton.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"x(new)", None));
        ___qtablewidgetitem39 = self.tableHasilNewton.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.labelStatusNewton.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.btnKembaliNewton.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Input Fungsi dan Tebakan Awal", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fungsi f(x) :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tebakan Aawl x0 :", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Iterasi", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Toleransi Error :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max Iterasi :", None))
        self.btnHitungNewton.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.btnResetNewton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.labelJudulRegula.setText(QCoreApplication.translate("MainWindow", u"Metode Regula Falsi", None))
        ___qtablewidgetitem40 = self.tableHasilRegula.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Iterasi", None));
        ___qtablewidgetitem41 = self.tableHasilRegula.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem42 = self.tableHasilRegula.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem43 = self.tableHasilRegula.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"c (Regula)", None));
        ___qtablewidgetitem44 = self.tableHasilRegula.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"f(c)", None));
        ___qtablewidgetitem45 = self.tableHasilRegula.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        ___qtablewidgetitem46 = self.tableHasilRegula.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Ket", None));
        self.labelStatusRegula.setText(QCoreApplication.translate("MainWindow", u"Status: Menunggu...", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Solusi Akhir", None))
        self.btnKembaliRegula.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Input Fungsi dan Batas", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fungsi f(x) :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Batas Bawah (a) :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Batas Atas (b) :", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Iterasi", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Toleransi Error :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Max Iterasi :", None))
        self.btnHitungRegula.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.btnResetRegula.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

