# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modal_file_open.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_dialog_open_file(object):
    def setupUi(self, dialog_open_file):
        if not dialog_open_file.objectName():
            dialog_open_file.setObjectName(u"dialog_open_file")
        dialog_open_file.setWindowModality(Qt.WindowModality.ApplicationModal)
        dialog_open_file.resize(252, 116)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_open_file.sizePolicy().hasHeightForWidth())
        dialog_open_file.setSizePolicy(sizePolicy)
        dialog_open_file.setMaximumSize(QSize(16777215, 116))
        self.gridLayout = QGridLayout(dialog_open_file)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame = QFrame(dialog_open_file)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.vspacer)

        self.vlay_chk = QVBoxLayout()
        self.vlay_chk.setObjectName(u"vlay_chk")
        self.lbl_sel_type = QLabel(self.main_frame)
        self.lbl_sel_type.setObjectName(u"lbl_sel_type")

        self.vlay_chk.addWidget(self.lbl_sel_type)

        self.cmb_sel_type = QComboBox(self.main_frame)
        self.cmb_sel_type.setObjectName(u"cmb_sel_type")

        self.vlay_chk.addWidget(self.cmb_sel_type)


        self.verticalLayout_2.addLayout(self.vlay_chk)

        self.btn_ok = QPushButton(self.main_frame)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout_2.addWidget(self.btn_ok)


        self.gridLayout.addWidget(self.main_frame, 1, 0, 1, 1)


        self.retranslateUi(dialog_open_file)

        QMetaObject.connectSlotsByName(dialog_open_file)
    # setupUi

    def retranslateUi(self, dialog_open_file):
        dialog_open_file.setWindowTitle(QCoreApplication.translate("dialog_open_file", u"Open file...", None))
        self.lbl_sel_type.setText(QCoreApplication.translate("dialog_open_file", u"Select type of file you want to load:", None))
        self.btn_ok.setText(QCoreApplication.translate("dialog_open_file", u"Select file...", None))
    # retranslateUi

