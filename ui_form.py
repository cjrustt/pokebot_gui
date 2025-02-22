# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1150, 538)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"	background-color: rgb(14, 14, 14);\n"
"	color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"	selection-background-color:#007b50;\n"
"	background-color:#1e1d23;\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: rgb(65, 65, 65);\n"
"	border-right-color: rgb(65, 65, 65);\n"
"	border-left-color: rgb(65, 65, 65);\n"
"	border-bottom-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: rgb(39, 40, 45);\n"
"}\n"
"QPushButton::default{\n"
"	border-style: inset;\n"
"	border-top-color: transparent;\n"
"	border-right-color: trans"
                        "parent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: rgb(44, 45, 48);\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-b"
                        "ottom-color: #37efba;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #37efba;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #808086;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#1"
                        "e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"	color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"	color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #04b97f;\n"
"	border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"	color: #a9b7c6;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"  	background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background:#1e1d23;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: #04b97f;\n"
"	border-bottom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #FFFFFF;\n"
"	padding-left:15px;\n"
""
                        "	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(77,77,77);\n"
"		background-color:#1e1d23;\n"
"		border-style: solid;\n"
"		border-width: 1px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom"
                        "-width: 1px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding: 3px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-bottom: 2px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	spacing: 20px;\n"
"	padding-left: 10px;\n"
"	padding-right: 5px;\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	border-color: rgb(65, 65, 65);\n"
"\n"
"\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"    spacing: 20px;\n"
"	padding-left: 10px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	border"
                        "-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f"
                        ";\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"	color: #a9b7c6;	\n"
"	background-col"
                        "or: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	height: 14px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSli"
                        "der::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"font: \"Noto Sans\";")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.baseWidget = QWidget(MainWindow)
        self.baseWidget.setObjectName(u"baseWidget")
        self.baseWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.baseWidget.sizePolicy().hasHeightForWidth())
        self.baseWidget.setSizePolicy(sizePolicy)
        self.baseWidget.setStyleSheet(u"font: \"Noto Sans\";")
        self.tabWidget = QTabWidget(self.baseWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-1, 0, 1161, 581))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setBold(False)
        font1.setItalic(False)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"font: \"Noto Sans\";")
        self.tabWidget.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.Program = QWidget()
        self.Program.setObjectName(u"Program")
        sizePolicy.setHeightForWidth(self.Program.sizePolicy().hasHeightForWidth())
        self.Program.setSizePolicy(sizePolicy)
        self.widget = QWidget(self.Program)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 1151, 511))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setFont(font1)
        self.widget.setStyleSheet(u"font: \"Noto Sans\";")
        self.verticalLayoutWidget_4 = QWidget(self.widget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(1010, 270, 131, 111))
        self.button_and_status_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.button_and_status_layout.setObjectName(u"button_and_status_layout")
        self.button_and_status_layout.setContentsMargins(5, 5, 5, 5)
        self.start_button = QPushButton(self.verticalLayoutWidget_4)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 40))
        self.start_button.setBaseSize(QSize(0, 0))
        self.start_button.setFont(font1)
        self.start_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.start_button.setStyleSheet(u"border-radius:8px")
        icon = QIcon()
        iconThemeName = u"applications-internet"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.start_button.setIcon(icon)

        self.button_and_status_layout.addWidget(self.start_button)

        self.stop_button = QPushButton(self.verticalLayoutWidget_4)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setEnabled(True)
        self.stop_button.setMinimumSize(QSize(0, 40))
        self.stop_button.setBaseSize(QSize(0, 0))
        self.stop_button.setFont(font1)
        self.stop_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stop_button.setStyleSheet(u"border-radius:8px")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.stop_button.setIcon(icon1)

        self.button_and_status_layout.addWidget(self.stop_button)

        self.console_display = QTextEdit(self.widget)
        self.console_display.setObjectName(u"console_display")
        self.console_display.setGeometry(QRect(9, 271, 991, 221))
        sizePolicy.setHeightForWidth(self.console_display.sizePolicy().hasHeightForWidth())
        self.console_display.setSizePolicy(sizePolicy)
        self.console_display.setMinimumSize(QSize(990, 10))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.console_display.setFont(font2)
        self.console_display.setReadOnly(True)
        self.console_display.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.title_text = QLabel(self.widget)
        self.title_text.setObjectName(u"title_text")
        self.title_text.setGeometry(QRect(860, 0, 281, 31))
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        self.title_text.setFont(font3)
        self.title_text.setStyleSheet(u"color: rgb(224, 27, 36);")
        self.title_text.setFrameShape(QFrame.Shape.NoFrame)
        self.title_text.setScaledContents(False)
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_url_button = QPushButton(self.widget)
        self.add_url_button.setObjectName(u"add_url_button")
        self.add_url_button.setGeometry(QRect(10, 230, 91, 31))
        self.add_url_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.add_url_button.setStyleSheet(u"border-radius:8px")
        icon2 = QIcon()
        iconThemeName = u"edit-redo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.add_url_button.setIcon(icon2)
        self.item_logo = QLabel(self.widget)
        self.item_logo.setObjectName(u"item_logo")
        self.item_logo.setGeometry(QRect(860, 40, 281, 221))
        self.item_logo.setFont(font1)
        self.item_logo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.item_logo.setFrameShape(QFrame.Shape.NoFrame)
        self.item_logo.setTextFormat(Qt.TextFormat.PlainText)
        self.item_logo.setPixmap(QPixmap(u"../../../Pictures/purepng.com-pokeballpokeballdevicepokemon-ballpokemon-capture-ball-1701527825896xpp8j.png"))
        self.item_logo.setScaledContents(True)
        self.product_display_list = QListWidget(self.widget)
        self.product_display_list.setObjectName(u"product_display_list")
        self.product_display_list.setGeometry(QRect(10, 30, 841, 191))
        sizePolicy.setHeightForWidth(self.product_display_list.sizePolicy().hasHeightForWidth())
        self.product_display_list.setSizePolicy(sizePolicy)
        self.product_display_list.setFont(font1)
        self.product_display_list.setStyleSheet(u"background-color: rgb(54, 54, 55);")
        self.product_display_list.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1010, 390, 131, 101))
        self.refreshCountLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.refreshCountLayout.setSpacing(5)
        self.refreshCountLayout.setObjectName(u"refreshCountLayout")
        self.refreshCountLayout.setContentsMargins(5, 5, 5, 5)
        self.refresh_text = QLabel(self.verticalLayoutWidget_2)
        self.refresh_text.setObjectName(u"refresh_text")
        self.refresh_text.setFont(font1)

        self.refreshCountLayout.addWidget(self.refresh_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.refresh_number = QLCDNumber(self.verticalLayoutWidget_2)
        self.refresh_number.setObjectName(u"refresh_number")
        sizePolicy.setHeightForWidth(self.refresh_number.sizePolicy().hasHeightForWidth())
        self.refresh_number.setSizePolicy(sizePolicy)
        self.refresh_number.setMinimumSize(QSize(120, 55))
        self.refresh_number.setFont(font1)
        self.refresh_number.setMode(QLCDNumber.Mode.Dec)

        self.refreshCountLayout.addWidget(self.refresh_number)

        self.url_entry_line = QLineEdit(self.widget)
        self.url_entry_line.setObjectName(u"url_entry_line")
        self.url_entry_line.setGeometry(QRect(110, 230, 741, 31))
        self.url_entry_line.setFont(font1)
        self.remove_url_button = QPushButton(self.widget)
        self.remove_url_button.setObjectName(u"remove_url_button")
        self.remove_url_button.setGeometry(QRect(10, 230, 91, 31))
        self.remove_url_button.setFont(font1)
        self.remove_url_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.remove_url_button.setStyleSheet(u"border-radius:8px")
        icon3 = QIcon()
        iconThemeName = u"edit-undo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.remove_url_button.setIcon(icon3)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(730, 10, 121, 21))
        font4 = QFont()
        font4.setFamilies([u"Noto Sans"])
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(59, 75, 115);")
        self.selected_product_label = QLabel(self.widget)
        self.selected_product_label.setObjectName(u"selected_product_label")
        self.selected_product_label.setGeometry(QRect(10, 0, 721, 31))
        self.selected_product_label.setFont(font1)
        self.selected_product_label.setFrameShape(QFrame.Shape.NoFrame)
        self.selected_product_label.setScaledContents(True)
        self.selected_product_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selected_product_label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.verticalLayoutWidget_4.raise_()
        self.console_display.raise_()
        self.title_text.raise_()
        self.item_logo.raise_()
        self.product_display_list.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.url_entry_line.raise_()
        self.remove_url_button.raise_()
        self.label.raise_()
        self.selected_product_label.raise_()
        self.add_url_button.raise_()
        self.tabWidget.addTab(self.Program, "")
        self.Config = QWidget()
        self.Config.setObjectName(u"Config")
        sizePolicy.setHeightForWidth(self.Config.sizePolicy().hasHeightForWidth())
        self.Config.setSizePolicy(sizePolicy)
        self.Config.setStyleSheet(u"")
        self.timezone_frame = QFrame(self.Config)
        self.timezone_frame.setObjectName(u"timezone_frame")
        self.timezone_frame.setGeometry(QRect(30, 40, 181, 121))
        self.timezone_frame.setStyleSheet(u"#timezone_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.timezone_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.timezone_frame.setLineWidth(1)
        self.timezone_field = QComboBox(self.timezone_frame)
        self.timezone_field.addItem("")
        self.timezone_field.addItem("")
        self.timezone_field.setObjectName(u"timezone_field")
        self.timezone_field.setGeometry(QRect(10, 70, 161, 31))
        self.timezone_field.setFont(font1)
        self.timezone_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget_8 = QWidget(self.timezone_frame)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 10, 160, 41))
        self.timezone_layout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.timezone_layout.setObjectName(u"timezone_layout")
        self.timezone_layout.setContentsMargins(0, 0, 0, 0)
        self.timezone_label = QLabel(self.verticalLayoutWidget_8)
        self.timezone_label.setObjectName(u"timezone_label")
        sizePolicy.setHeightForWidth(self.timezone_label.sizePolicy().hasHeightForWidth())
        self.timezone_label.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Noto Sans"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setKerning(True)
        self.timezone_label.setFont(font5)
        self.timezone_label.setScaledContents(False)

        self.timezone_layout.addWidget(self.timezone_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.max_quantity_frame = QFrame(self.Config)
        self.max_quantity_frame.setObjectName(u"max_quantity_frame")
        self.max_quantity_frame.setGeometry(QRect(30, 190, 181, 121))
        self.max_quantity_frame.setStyleSheet(u"#max_quantity_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.max_quantity_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.max_quantity_frame.setLineWidth(1)
        self.max_quantity_field = QComboBox(self.max_quantity_frame)
        self.max_quantity_field.addItem("")
        self.max_quantity_field.addItem("")
        self.max_quantity_field.addItem("")
        self.max_quantity_field.setObjectName(u"max_quantity_field")
        self.max_quantity_field.setGeometry(QRect(10, 70, 161, 31))
        self.max_quantity_field.setFont(font1)
        self.max_quantity_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.max_quantity_field.setEditable(False)
        self.verticalLayoutWidget_5 = QWidget(self.max_quantity_frame)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 160, 41))
        self.max_quantity_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.max_quantity_layout.setObjectName(u"max_quantity_layout")
        self.max_quantity_layout.setContentsMargins(0, 0, 0, 0)
        self.max_quantity_label = QLabel(self.verticalLayoutWidget_5)
        self.max_quantity_label.setObjectName(u"max_quantity_label")
        sizePolicy.setHeightForWidth(self.max_quantity_label.sizePolicy().hasHeightForWidth())
        self.max_quantity_label.setSizePolicy(sizePolicy)
        self.max_quantity_label.setFont(font5)
        self.max_quantity_label.setScaledContents(False)

        self.max_quantity_layout.addWidget(self.max_quantity_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.refresh_time_frame = QFrame(self.Config)
        self.refresh_time_frame.setObjectName(u"refresh_time_frame")
        self.refresh_time_frame.setGeometry(QRect(260, 190, 181, 121))
        self.refresh_time_frame.setStyleSheet(u"#refresh_time_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.refresh_time_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.refresh_time_frame.setLineWidth(1)
        self.verticalLayoutWidget_6 = QWidget(self.refresh_time_frame)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 160, 41))
        self.refresh_time_layout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.refresh_time_layout.setObjectName(u"refresh_time_layout")
        self.refresh_time_layout.setContentsMargins(0, 0, 0, 0)
        self.refresh_time_label = QLabel(self.verticalLayoutWidget_6)
        self.refresh_time_label.setObjectName(u"refresh_time_label")
        sizePolicy.setHeightForWidth(self.refresh_time_label.sizePolicy().hasHeightForWidth())
        self.refresh_time_label.setSizePolicy(sizePolicy)
        self.refresh_time_label.setFont(font5)
        self.refresh_time_label.setScaledContents(False)

        self.refresh_time_layout.addWidget(self.refresh_time_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.refresh_time_field = QComboBox(self.refresh_time_frame)
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.addItem("")
        self.refresh_time_field.setObjectName(u"refresh_time_field")
        self.refresh_time_field.setGeometry(QRect(10, 70, 161, 31))
        self.refresh_time_field.setFont(font1)
        self.refresh_time_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.refresh_time_field.setEditable(False)
        self.chrome_data_path_frame = QFrame(self.Config)
        self.chrome_data_path_frame.setObjectName(u"chrome_data_path_frame")
        self.chrome_data_path_frame.setGeometry(QRect(30, 350, 561, 141))
        self.chrome_data_path_frame.setStyleSheet(u"#chrome_data_path_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.chrome_data_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.chrome_data_path_frame.setLineWidth(1)
        self.chrome_data_path_field = QLineEdit(self.chrome_data_path_frame)
        self.chrome_data_path_field.setObjectName(u"chrome_data_path_field")
        self.chrome_data_path_field.setGeometry(QRect(10, 80, 471, 26))
        self.chrome_data_path_field.setFont(font1)
        self.chrome_data_path_current_label = QLabel(self.chrome_data_path_frame)
        self.chrome_data_path_current_label.setObjectName(u"chrome_data_path_current_label")
        self.chrome_data_path_current_label.setGeometry(QRect(10, 50, 61, 21))
        sizePolicy.setHeightForWidth(self.chrome_data_path_current_label.sizePolicy().hasHeightForWidth())
        self.chrome_data_path_current_label.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Noto Sans"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.chrome_data_path_current_label.setFont(font6)
        self.chrome_data_path_button = QPushButton(self.chrome_data_path_frame)
        self.chrome_data_path_button.setObjectName(u"chrome_data_path_button")
        self.chrome_data_path_button.setGeometry(QRect(490, 80, 61, 26))
        font7 = QFont()
        font7.setFamilies([u"Noto Sans"])
        font7.setPointSize(13)
        font7.setBold(False)
        font7.setItalic(False)
        self.chrome_data_path_button.setFont(font7)
        self.chrome_data_path_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chrome_data_path_button.setStyleSheet(u"border-radius:8px")
        self.verticalLayoutWidget_9 = QWidget(self.chrome_data_path_frame)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(0, 0, 561, 41))
        self.chrome_data_path_layout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.chrome_data_path_layout.setObjectName(u"chrome_data_path_layout")
        self.chrome_data_path_layout.setContentsMargins(0, 0, 0, 0)
        self.chrome_data_path_label = QLabel(self.verticalLayoutWidget_9)
        self.chrome_data_path_label.setObjectName(u"chrome_data_path_label")
        sizePolicy.setHeightForWidth(self.chrome_data_path_label.sizePolicy().hasHeightForWidth())
        self.chrome_data_path_label.setSizePolicy(sizePolicy)
        self.chrome_data_path_label.setFont(font5)
        self.chrome_data_path_label.setScaledContents(False)

        self.chrome_data_path_layout.addWidget(self.chrome_data_path_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.chrome_data_path_display = QLabel(self.chrome_data_path_frame)
        self.chrome_data_path_display.setObjectName(u"chrome_data_path_display")
        self.chrome_data_path_display.setGeometry(QRect(90, 50, 451, 21))
        sizePolicy.setHeightForWidth(self.chrome_data_path_display.sizePolicy().hasHeightForWidth())
        self.chrome_data_path_display.setSizePolicy(sizePolicy)
        self.chrome_data_path_display.setFont(font2)
        self.chrome_data_path_display.setStyleSheet(u"color: rgb(98, 160, 234);")
        self.chrome_data_path_display.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.chrome_data_path_example = QLabel(self.chrome_data_path_frame)
        self.chrome_data_path_example.setObjectName(u"chrome_data_path_example")
        self.chrome_data_path_example.setGeometry(QRect(30, 110, 511, 21))
        sizePolicy.setHeightForWidth(self.chrome_data_path_example.sizePolicy().hasHeightForWidth())
        self.chrome_data_path_example.setSizePolicy(sizePolicy)
        self.chrome_data_path_example.setFont(font2)
        self.chrome_data_path_example.setStyleSheet(u"color: rgb(98, 98, 98);")
        self.chrome_profile_frame = QFrame(self.Config)
        self.chrome_profile_frame.setObjectName(u"chrome_profile_frame")
        self.chrome_profile_frame.setGeometry(QRect(260, 40, 181, 121))
        self.chrome_profile_frame.setStyleSheet(u"#chrome_profile_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.chrome_profile_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.chrome_profile_frame.setLineWidth(1)
        self.verticalLayoutWidget_7 = QWidget(self.chrome_profile_frame)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 160, 41))
        self.chrome_profile_layout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.chrome_profile_layout.setObjectName(u"chrome_profile_layout")
        self.chrome_profile_layout.setContentsMargins(0, 0, 0, 0)
        self.chrome_profile_label = QLabel(self.verticalLayoutWidget_7)
        self.chrome_profile_label.setObjectName(u"chrome_profile_label")
        sizePolicy.setHeightForWidth(self.chrome_profile_label.sizePolicy().hasHeightForWidth())
        self.chrome_profile_label.setSizePolicy(sizePolicy)
        self.chrome_profile_label.setFont(font5)
        self.chrome_profile_label.setScaledContents(False)

        self.chrome_profile_layout.addWidget(self.chrome_profile_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.chrome_profile_field = QComboBox(self.chrome_profile_frame)
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.addItem("")
        self.chrome_profile_field.setObjectName(u"chrome_profile_field")
        self.chrome_profile_field.setGeometry(QRect(10, 70, 161, 31))
        self.chrome_profile_field.setFont(font1)
        self.chrome_profile_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.save_settings_button = QPushButton(self.Config)
        self.save_settings_button.setObjectName(u"save_settings_button")
        self.save_settings_button.setGeometry(QRect(990, 450, 131, 41))
        self.save_settings_button.setFont(font7)
        self.save_settings_button.setStyleSheet(u"border-radius: 8px;\n"
"color: rgb(38, 162, 105);")
        self.cvv_code_frame = QFrame(self.Config)
        self.cvv_code_frame.setObjectName(u"cvv_code_frame")
        self.cvv_code_frame.setGeometry(QRect(490, 40, 181, 121))
        self.cvv_code_frame.setStyleSheet(u"#cvv_code_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.cvv_code_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.cvv_code_frame.setLineWidth(1)
        self.cvv_field = QLineEdit(self.cvv_code_frame)
        self.cvv_field.setObjectName(u"cvv_field")
        self.cvv_field.setGeometry(QRect(20, 80, 61, 26))
        self.cvv_field.setFont(font1)
        self.cvv_field.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.cvv_field.setText(u"")
        self.cvv_field.setClearButtonEnabled(False)
        self.cvv_button = QPushButton(self.cvv_code_frame)
        self.cvv_button.setObjectName(u"cvv_button")
        self.cvv_button.setGeometry(QRect(100, 80, 61, 26))
        self.cvv_button.setFont(font7)
        self.cvv_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cvv_button.setStyleSheet(u"border-radius:8px")
        self.verticalLayoutWidget_10 = QWidget(self.cvv_code_frame)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(0, 0, 181, 41))
        self.cvv_layout = QVBoxLayout(self.verticalLayoutWidget_10)
        self.cvv_layout.setObjectName(u"cvv_layout")
        self.cvv_layout.setContentsMargins(0, 0, 0, 0)
        self.cvv_label = QLabel(self.verticalLayoutWidget_10)
        self.cvv_label.setObjectName(u"cvv_label")
        sizePolicy.setHeightForWidth(self.cvv_label.sizePolicy().hasHeightForWidth())
        self.cvv_label.setSizePolicy(sizePolicy)
        self.cvv_label.setFont(font5)
        self.cvv_label.setScaledContents(False)

        self.cvv_layout.addWidget(self.cvv_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cvv_set_indicator = QLabel(self.cvv_code_frame)
        self.cvv_set_indicator.setObjectName(u"cvv_set_indicator")
        self.cvv_set_indicator.setGeometry(QRect(20, 50, 141, 21))
        sizePolicy.setHeightForWidth(self.cvv_set_indicator.sizePolicy().hasHeightForWidth())
        self.cvv_set_indicator.setSizePolicy(sizePolicy)
        self.cvv_set_indicator.setFont(font6)
        self.chrome_data_path_notice = QLabel(self.Config)
        self.chrome_data_path_notice.setObjectName(u"chrome_data_path_notice")
        self.chrome_data_path_notice.setGeometry(QRect(190, 490, 401, 20))
        self.chrome_data_path_notice.setFont(font4)
        self.chrome_data_path_notice.setStyleSheet(u"color: rgb(246, 97, 81);")
        self.reset_defaults_button = QPushButton(self.Config)
        self.reset_defaults_button.setObjectName(u"reset_defaults_button")
        self.reset_defaults_button.setGeometry(QRect(990, 400, 131, 41))
        self.reset_defaults_button.setFont(font7)
        self.reset_defaults_button.setStyleSheet(u"border-radius: 8px;\n"
"color: rgb(192, 28, 40)")
        self.confirm_reset_warning = QLabel(self.Config)
        self.confirm_reset_warning.setObjectName(u"confirm_reset_warning")
        self.confirm_reset_warning.setGeometry(QRect(840, 450, 141, 41))
        self.confirm_reset_warning.setFont(font1)
        self.confirm_reset_warning.setStyleSheet(u"color: rgb(224, 27, 36);")
        self.confirm_reset_warning.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.selenium_options_frame = QFrame(self.Config)
        self.selenium_options_frame.setObjectName(u"selenium_options_frame")
        self.selenium_options_frame.setGeometry(QRect(760, 40, 311, 271))
        self.selenium_options_frame.setStyleSheet(u"#selenium_options_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.selenium_options_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.selenium_options_frame.setLineWidth(1)
        self.verticalLayoutWidget_11 = QWidget(self.selenium_options_frame)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(0, 0, 311, 41))
        self.selenium_options_layout = QVBoxLayout(self.verticalLayoutWidget_11)
        self.selenium_options_layout.setObjectName(u"selenium_options_layout")
        self.selenium_options_layout.setContentsMargins(0, 0, 0, 0)
        self.selenium_options_label = QLabel(self.verticalLayoutWidget_11)
        self.selenium_options_label.setObjectName(u"selenium_options_label")
        sizePolicy.setHeightForWidth(self.selenium_options_label.sizePolicy().hasHeightForWidth())
        self.selenium_options_label.setSizePolicy(sizePolicy)
        self.selenium_options_label.setFont(font5)
        self.selenium_options_label.setScaledContents(False)

        self.selenium_options_layout.addWidget(self.selenium_options_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.headless_checkbox = QCheckBox(self.selenium_options_frame)
        self.headless_checkbox.setObjectName(u"headless_checkbox")
        self.headless_checkbox.setGeometry(QRect(10, 60, 131, 31))
        self.detach_checkbox = QCheckBox(self.selenium_options_frame)
        self.detach_checkbox.setObjectName(u"detach_checkbox")
        self.detach_checkbox.setGeometry(QRect(160, 60, 131, 31))
        self.headless_label = QLabel(self.selenium_options_frame)
        self.headless_label.setObjectName(u"headless_label")
        self.headless_label.setGeometry(QRect(20, 100, 121, 111))
        self.headless_label.setFont(font1)
        self.headless_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.headless_label.setWordWrap(True)
        self.headless_label_2 = QLabel(self.selenium_options_frame)
        self.headless_label_2.setObjectName(u"headless_label_2")
        self.headless_label_2.setGeometry(QRect(170, 100, 121, 111))
        self.headless_label_2.setFont(font1)
        self.headless_label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.headless_label_2.setWordWrap(True)
        self.auto_complete_frame = QFrame(self.Config)
        self.auto_complete_frame.setObjectName(u"auto_complete_frame")
        self.auto_complete_frame.setGeometry(QRect(490, 190, 181, 121))
        self.auto_complete_frame.setStyleSheet(u"#auto_complete_frame {\n"
" border: 1px solid rgb(237, 51, 59);\n"
"border-radius:2px;\n"
"}")
        self.auto_complete_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.auto_complete_frame.setLineWidth(1)
        self.verticalLayoutWidget_12 = QWidget(self.auto_complete_frame)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(10, 10, 160, 41))
        self.auto_complete_layout = QVBoxLayout(self.verticalLayoutWidget_12)
        self.auto_complete_layout.setObjectName(u"auto_complete_layout")
        self.auto_complete_layout.setContentsMargins(0, 0, 0, 0)
        self.auto_complete_label = QLabel(self.verticalLayoutWidget_12)
        self.auto_complete_label.setObjectName(u"auto_complete_label")
        sizePolicy.setHeightForWidth(self.auto_complete_label.sizePolicy().hasHeightForWidth())
        self.auto_complete_label.setSizePolicy(sizePolicy)
        self.auto_complete_label.setFont(font5)
        self.auto_complete_label.setScaledContents(False)

        self.auto_complete_layout.addWidget(self.auto_complete_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.auto_complete_button = QCheckBox(self.auto_complete_frame)
        self.auto_complete_button.setObjectName(u"auto_complete_button")
        self.auto_complete_button.setGeometry(QRect(30, 60, 121, 51))
        self.auto_complete_button.setBaseSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Noto Sans"])
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.auto_complete_button.setFont(font8)
        self.auto_complete_button.setStyleSheet(u"border-radius:8px")
        self.auto_complete_button.setIconSize(QSize(20, 20))
        self.tabWidget.addTab(self.Config, "")
        MainWindow.setCentralWidget(self.baseWidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.timezone_field.setCurrentIndex(0)
        self.max_quantity_field.setCurrentIndex(0)
        self.refresh_time_field.setCurrentIndex(0)
        self.chrome_profile_field.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u" START  ", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u" STOP", None))
        self.console_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.title_text.setText(QCoreApplication.translate("MainWindow", u"PokeBot 2.1", None))
        self.add_url_button.setText(QCoreApplication.translate("MainWindow", u"  Add ", None))
        self.item_logo.setText("")
        self.refresh_text.setText(QCoreApplication.translate("MainWindow", u"REFRESHES", None))
        self.url_entry_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter URL...", None))
        self.remove_url_button.setText(QCoreApplication.translate("MainWindow", u" Remove", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Double-click to select", None))
        self.selected_product_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Program), QCoreApplication.translate("MainWindow", u"Program", None))
        self.timezone_field.setItemText(0, QCoreApplication.translate("MainWindow", u"Local", None))
        self.timezone_field.setItemText(1, QCoreApplication.translate("MainWindow", u"UTC", None))

        self.timezone_field.setPlaceholderText("")
        self.timezone_label.setText(QCoreApplication.translate("MainWindow", u"Timezone", None))
        self.max_quantity_field.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.max_quantity_field.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.max_quantity_field.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.max_quantity_field.setPlaceholderText("")
        self.max_quantity_label.setText(QCoreApplication.translate("MainWindow", u"Max. Quantity", None))
        self.refresh_time_label.setText(QCoreApplication.translate("MainWindow", u"Refresh Time", None))
        self.refresh_time_field.setItemText(0, QCoreApplication.translate("MainWindow", u"1 second", None))
        self.refresh_time_field.setItemText(1, QCoreApplication.translate("MainWindow", u"2 seconds", None))
        self.refresh_time_field.setItemText(2, QCoreApplication.translate("MainWindow", u"3 seconds", None))
        self.refresh_time_field.setItemText(3, QCoreApplication.translate("MainWindow", u"4 seconds", None))
        self.refresh_time_field.setItemText(4, QCoreApplication.translate("MainWindow", u"5 seconds", None))
        self.refresh_time_field.setItemText(5, QCoreApplication.translate("MainWindow", u"6 seconds", None))
        self.refresh_time_field.setItemText(6, QCoreApplication.translate("MainWindow", u"7 seconds", None))
        self.refresh_time_field.setItemText(7, QCoreApplication.translate("MainWindow", u"8 seconds", None))
        self.refresh_time_field.setItemText(8, QCoreApplication.translate("MainWindow", u"9 seconds", None))
        self.refresh_time_field.setItemText(9, QCoreApplication.translate("MainWindow", u"10 seconds", None))
        self.refresh_time_field.setItemText(10, QCoreApplication.translate("MainWindow", u"11 seconds", None))
        self.refresh_time_field.setItemText(11, QCoreApplication.translate("MainWindow", u"12 seconds", None))
        self.refresh_time_field.setItemText(12, QCoreApplication.translate("MainWindow", u"13 seconds", None))
        self.refresh_time_field.setItemText(13, QCoreApplication.translate("MainWindow", u"14 seconds", None))
        self.refresh_time_field.setItemText(14, QCoreApplication.translate("MainWindow", u"15 seconds", None))
        self.refresh_time_field.setItemText(15, QCoreApplication.translate("MainWindow", u"20 seconds", None))
        self.refresh_time_field.setItemText(16, QCoreApplication.translate("MainWindow", u"30 seconds", None))
        self.refresh_time_field.setItemText(17, QCoreApplication.translate("MainWindow", u"1 minute", None))
        self.refresh_time_field.setItemText(18, QCoreApplication.translate("MainWindow", u"2 minutes", None))
        self.refresh_time_field.setItemText(19, QCoreApplication.translate("MainWindow", u"5 minutes", None))

        self.refresh_time_field.setPlaceholderText("")
        self.chrome_data_path_current_label.setText(QCoreApplication.translate("MainWindow", u"Current:", None))
        self.chrome_data_path_button.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.chrome_data_path_label.setText(QCoreApplication.translate("MainWindow", u"Chrome User Data Path", None))
        self.chrome_data_path_display.setText("")
        self.chrome_data_path_example.setText("")
        self.chrome_profile_label.setText(QCoreApplication.translate("MainWindow", u"Chrome Profile", None))
        self.chrome_profile_field.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.chrome_profile_field.setItemText(1, QCoreApplication.translate("MainWindow", u"Profile 1", None))
        self.chrome_profile_field.setItemText(2, QCoreApplication.translate("MainWindow", u"Profile 2", None))
        self.chrome_profile_field.setItemText(3, QCoreApplication.translate("MainWindow", u"Profile 3", None))
        self.chrome_profile_field.setItemText(4, QCoreApplication.translate("MainWindow", u"Profile 4", None))
        self.chrome_profile_field.setItemText(5, QCoreApplication.translate("MainWindow", u"Profile 5", None))
        self.chrome_profile_field.setItemText(6, QCoreApplication.translate("MainWindow", u"Profile 6", None))
        self.chrome_profile_field.setItemText(7, QCoreApplication.translate("MainWindow", u"Profile 7", None))
        self.chrome_profile_field.setItemText(8, QCoreApplication.translate("MainWindow", u"Profile 8", None))
        self.chrome_profile_field.setItemText(9, QCoreApplication.translate("MainWindow", u"Profile 9", None))

        self.chrome_profile_field.setPlaceholderText("")
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.cvv_button.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.cvv_label.setText(QCoreApplication.translate("MainWindow", u"CVV Code", None))
        self.cvv_set_indicator.setText(QCoreApplication.translate("MainWindow", u"Not Set", None))
        self.chrome_data_path_notice.setText(QCoreApplication.translate("MainWindow", u"* Note: Backslashes will be automatically converted to forward slashes", None))
        self.reset_defaults_button.setText(QCoreApplication.translate("MainWindow", u"Reset Defaults", None))
        self.confirm_reset_warning.setText(QCoreApplication.translate("MainWindow", u"Press Save Settings \n"
"to confirm -->", None))
        self.selenium_options_label.setText(QCoreApplication.translate("MainWindow", u"Selenium Options", None))
        self.headless_checkbox.setText(QCoreApplication.translate("MainWindow", u"Headless", None))
        self.detach_checkbox.setText(QCoreApplication.translate("MainWindow", u"Detach", None))
        self.headless_label.setText(QCoreApplication.translate("MainWindow", u"Headless mode means that the browser will not open a visible window", None))
        self.headless_label_2.setText(QCoreApplication.translate("MainWindow", u"Detach means that the browser will stay open after the program stops", None))
        self.auto_complete_label.setText(QCoreApplication.translate("MainWindow", u"Auto-Complete", None))
        self.auto_complete_button.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Config), QCoreApplication.translate("MainWindow", u"Config", None))
    # retranslateUi

