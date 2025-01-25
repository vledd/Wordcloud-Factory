# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 719)
        MainWindow.setMinimumSize(QSize(910, 710))
        self.actionGet_statistics_as_txt = QAction(MainWindow)
        self.actionGet_statistics_as_txt.setObjectName(u"actionGet_statistics_as_txt")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp_me = QAction(MainWindow)
        self.actionHelp_me.setObjectName(u"actionHelp_me")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_global = QFrame(self.centralwidget)
        self.frame_global.setObjectName(u"frame_global")
        self.frame_global.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_global.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_global)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalFrame_2 = QFrame(self.frame_global)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.generate_btn = QPushButton(self.verticalFrame_2)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setEnabled(False)

        self.verticalLayout_4.addWidget(self.generate_btn)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.save_btn = QPushButton(self.verticalFrame_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.save_btn)

        self.generate_vid_btn = QPushButton(self.verticalFrame_2)
        self.generate_vid_btn.setObjectName(u"generate_vid_btn")
        self.generate_vid_btn.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.generate_vid_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.progressBar = QProgressBar(self.verticalFrame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.preview_scroll = QScrollArea(self.verticalFrame_2)
        self.preview_scroll.setObjectName(u"preview_scroll")
        self.preview_scroll.setWidgetResizable(True)
        self.preview_scroll_contents = QWidget()
        self.preview_scroll_contents.setObjectName(u"preview_scroll_contents")
        self.preview_scroll_contents.setGeometry(QRect(0, 0, 422, 543))
        self.gridLayout_4 = QGridLayout(self.preview_scroll_contents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.preview_lbl = QLabel(self.preview_scroll_contents)
        self.preview_lbl.setObjectName(u"preview_lbl")
        self.preview_lbl.setScaledContents(False)
        self.preview_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.preview_lbl, 0, 0, 1, 1)

        self.preview_scroll.setWidget(self.preview_scroll_contents)

        self.verticalLayout_3.addWidget(self.preview_scroll)


        self.horizontalLayout_9.addWidget(self.verticalFrame_2)

        self.frame_settings_1 = QFrame(self.frame_global)
        self.frame_settings_1.setObjectName(u"frame_settings_1")
        self.frame_settings_1.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.frame_settings_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.subframe_settings_1 = QFrame(self.frame_settings_1)
        self.subframe_settings_1.setObjectName(u"subframe_settings_1")
        self.subframe_settings_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.subframe_settings_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.subframe_settings_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_json_file = QLabel(self.subframe_settings_1)
        self.lbl_json_file.setObjectName(u"lbl_json_file")

        self.verticalLayout.addWidget(self.lbl_json_file)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.path_json_edit = QLineEdit(self.subframe_settings_1)
        self.path_json_edit.setObjectName(u"path_json_edit")

        self.horizontalLayout_3.addWidget(self.path_json_edit)

        self.path_json_btn = QPushButton(self.subframe_settings_1)
        self.path_json_btn.setObjectName(u"path_json_btn")
        self.path_json_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.path_json_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lbl_stop_file = QLabel(self.subframe_settings_1)
        self.lbl_stop_file.setObjectName(u"lbl_stop_file")
        self.lbl_stop_file.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_stop_file)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.path_stop_edit = QLineEdit(self.subframe_settings_1)
        self.path_stop_edit.setObjectName(u"path_stop_edit")

        self.horizontalLayout_4.addWidget(self.path_stop_edit)

        self.path_stop_btn = QPushButton(self.subframe_settings_1)
        self.path_stop_btn.setObjectName(u"path_stop_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_stop_btn.sizePolicy().hasHeightForWidth())
        self.path_stop_btn.setSizePolicy(sizePolicy)
        self.path_stop_btn.setMinimumSize(QSize(0, 0))
        self.path_stop_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.path_stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.lbl_png_file = QLabel(self.subframe_settings_1)
        self.lbl_png_file.setObjectName(u"lbl_png_file")
        self.lbl_png_file.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_png_file)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.path_mask_edit = QLineEdit(self.subframe_settings_1)
        self.path_mask_edit.setObjectName(u"path_mask_edit")

        self.horizontalLayout_5.addWidget(self.path_mask_edit)

        self.path_mask_btn = QPushButton(self.subframe_settings_1)
        self.path_mask_btn.setObjectName(u"path_mask_btn")
        self.path_mask_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.path_mask_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.line = QFrame(self.subframe_settings_1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_width = QLabel(self.subframe_settings_1)
        self.lbl_width.setObjectName(u"lbl_width")

        self.verticalLayout_6.addWidget(self.lbl_width)

        self.img_width_spin = QSpinBox(self.subframe_settings_1)
        self.img_width_spin.setObjectName(u"img_width_spin")
        self.img_width_spin.setMinimum(100)
        self.img_width_spin.setMaximum(4000)
        self.img_width_spin.setSingleStep(10)
        self.img_width_spin.setValue(640)

        self.verticalLayout_6.addWidget(self.img_width_spin)

        self.lbl_height = QLabel(self.subframe_settings_1)
        self.lbl_height.setObjectName(u"lbl_height")

        self.verticalLayout_6.addWidget(self.lbl_height)

        self.img_height_spin = QSpinBox(self.subframe_settings_1)
        self.img_height_spin.setObjectName(u"img_height_spin")
        self.img_height_spin.setMinimum(100)
        self.img_height_spin.setMaximum(4000)
        self.img_height_spin.setSingleStep(10)
        self.img_height_spin.setValue(480)
        self.img_height_spin.setDisplayIntegerBase(10)

        self.verticalLayout_6.addWidget(self.img_height_spin)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.line_3 = QFrame(self.subframe_settings_1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_max_word = QLabel(self.subframe_settings_1)
        self.lbl_max_word.setObjectName(u"lbl_max_word")

        self.verticalLayout_7.addWidget(self.lbl_max_word)

        self.max_word_spin = QSpinBox(self.subframe_settings_1)
        self.max_word_spin.setObjectName(u"max_word_spin")
        self.max_word_spin.setMinimum(1)
        self.max_word_spin.setMaximum(4000)
        self.max_word_spin.setSingleStep(10)
        self.max_word_spin.setValue(200)

        self.verticalLayout_7.addWidget(self.max_word_spin)

        self.lbl_min_word_len = QLabel(self.subframe_settings_1)
        self.lbl_min_word_len.setObjectName(u"lbl_min_word_len")

        self.verticalLayout_7.addWidget(self.lbl_min_word_len)

        self.min_word_len_spin = QSpinBox(self.subframe_settings_1)
        self.min_word_len_spin.setObjectName(u"min_word_len_spin")
        self.min_word_len_spin.setValue(3)

        self.verticalLayout_7.addWidget(self.min_word_len_spin)

        self.lbl_sort_word = QLabel(self.subframe_settings_1)
        self.lbl_sort_word.setObjectName(u"lbl_sort_word")

        self.verticalLayout_7.addWidget(self.lbl_sort_word)

        self.sort_combo = QComboBox(self.subframe_settings_1)
        self.sort_combo.setObjectName(u"sort_combo")

        self.verticalLayout_7.addWidget(self.sort_combo)

        self.lbl_scaling = QLabel(self.subframe_settings_1)
        self.lbl_scaling.setObjectName(u"lbl_scaling")

        self.verticalLayout_7.addWidget(self.lbl_scaling)

        self.scaling_spin = QDoubleSpinBox(self.subframe_settings_1)
        self.scaling_spin.setObjectName(u"scaling_spin")
        self.scaling_spin.setDecimals(1)
        self.scaling_spin.setMinimum(1.000000000000000)
        self.scaling_spin.setMaximum(8.000000000000000)
        self.scaling_spin.setSingleStep(0.100000000000000)
        self.scaling_spin.setValue(1.000000000000000)

        self.verticalLayout_7.addWidget(self.scaling_spin)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.subframe_settings_1)


        self.horizontalLayout_9.addWidget(self.frame_settings_1)

        self.frame_settings_2 = QFrame(self.frame_global)
        self.frame_settings_2.setObjectName(u"frame_settings_2")
        self.frame_settings_2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.frame_settings_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.frame_settings_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.path_font_lbl = QLabel(self.frame_4)
        self.path_font_lbl.setObjectName(u"path_font_lbl")

        self.verticalLayout_10.addWidget(self.path_font_lbl)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.path_font_edit = QLineEdit(self.frame_4)
        self.path_font_edit.setObjectName(u"path_font_edit")

        self.horizontalLayout_6.addWidget(self.path_font_edit)

        self.path_font_btn = QPushButton(self.frame_4)
        self.path_font_btn.setObjectName(u"path_font_btn")
        self.path_font_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_6.addWidget(self.path_font_btn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.line_4 = QFrame(self.frame_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.min_font_size_lbl = QLabel(self.frame_4)
        self.min_font_size_lbl.setObjectName(u"min_font_size_lbl")

        self.verticalLayout_11.addWidget(self.min_font_size_lbl)

        self.min_font_size_spin = QSpinBox(self.frame_4)
        self.min_font_size_spin.setObjectName(u"min_font_size_spin")
        self.min_font_size_spin.setMinimum(1)
        self.min_font_size_spin.setMaximum(4000)
        self.min_font_size_spin.setValue(1)

        self.verticalLayout_11.addWidget(self.min_font_size_spin)

        self.max_font_size_lbl = QLabel(self.frame_4)
        self.max_font_size_lbl.setObjectName(u"max_font_size_lbl")

        self.verticalLayout_11.addWidget(self.max_font_size_lbl)

        self.max_font_size_spin = QSpinBox(self.frame_4)
        self.max_font_size_spin.setObjectName(u"max_font_size_spin")
        self.max_font_size_spin.setMaximum(4000)
        self.max_font_size_spin.setSingleStep(10)

        self.verticalLayout_11.addWidget(self.max_font_size_spin)

        self.font_step_lbl = QLabel(self.frame_4)
        self.font_step_lbl.setObjectName(u"font_step_lbl")

        self.verticalLayout_11.addWidget(self.font_step_lbl)

        self.font_step_spin = QSpinBox(self.frame_4)
        self.font_step_spin.setObjectName(u"font_step_spin")
        self.font_step_spin.setMinimum(1)
        self.font_step_spin.setMaximum(200)
        self.font_step_spin.setValue(1)

        self.verticalLayout_11.addWidget(self.font_step_spin)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.color_mode_lbl = QLabel(self.frame_4)
        self.color_mode_lbl.setObjectName(u"color_mode_lbl")

        self.verticalLayout_12.addWidget(self.color_mode_lbl)

        self.color_mode_combo = QComboBox(self.frame_4)
        self.color_mode_combo.setObjectName(u"color_mode_combo")

        self.verticalLayout_12.addWidget(self.color_mode_combo)

        self.color_map_lbl = QLabel(self.frame_4)
        self.color_map_lbl.setObjectName(u"color_map_lbl")

        self.verticalLayout_12.addWidget(self.color_map_lbl)

        self.color_map_combo = QComboBox(self.frame_4)
        self.color_map_combo.setObjectName(u"color_map_combo")

        self.verticalLayout_12.addWidget(self.color_map_combo)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_12.addWidget(self.label_17)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bg_color_edit = QLineEdit(self.frame_4)
        self.bg_color_edit.setObjectName(u"bg_color_edit")

        self.horizontalLayout.addWidget(self.bg_color_edit)

        self.bg_color_pick_btn = QPushButton(self.frame_4)
        self.bg_color_pick_btn.setObjectName(u"bg_color_pick_btn")

        self.horizontalLayout.addWidget(self.bg_color_pick_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.use_mask_chkbox = QCheckBox(self.frame_4)
        self.use_mask_chkbox.setObjectName(u"use_mask_chkbox")
        self.use_mask_chkbox.setEnabled(False)

        self.verticalLayout_12.addWidget(self.use_mask_chkbox)

        self.use_mask_colors_chk = QCheckBox(self.frame_4)
        self.use_mask_colors_chk.setObjectName(u"use_mask_colors_chk")
        self.use_mask_colors_chk.setEnabled(False)

        self.verticalLayout_12.addWidget(self.use_mask_colors_chk)

        self.color_to_mask_combo = QComboBox(self.frame_4)
        self.color_to_mask_combo.setObjectName(u"color_to_mask_combo")
        self.color_to_mask_combo.setEnabled(False)

        self.verticalLayout_12.addWidget(self.color_to_mask_combo)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_12.addWidget(self.label_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mask_color_edit = QLineEdit(self.frame_4)
        self.mask_color_edit.setObjectName(u"mask_color_edit")

        self.horizontalLayout_2.addWidget(self.mask_color_edit)

        self.mask_color_pick_btn = QPushButton(self.frame_4)
        self.mask_color_pick_btn.setObjectName(u"mask_color_pick_btn")

        self.horizontalLayout_2.addWidget(self.mask_color_pick_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.mask_contour_thick_lbl = QLabel(self.frame_4)
        self.mask_contour_thick_lbl.setObjectName(u"mask_contour_thick_lbl")

        self.verticalLayout_12.addWidget(self.mask_contour_thick_lbl)

        self.mask_thick_spin = QSpinBox(self.frame_4)
        self.mask_thick_spin.setObjectName(u"mask_thick_spin")

        self.verticalLayout_12.addWidget(self.mask_thick_spin)


        self.verticalLayout_9.addLayout(self.verticalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.copyright_lbl = QLabel(self.frame_4)
        self.copyright_lbl.setObjectName(u"copyright_lbl")
        self.copyright_lbl.setEnabled(False)
        self.copyright_lbl.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.copyright_lbl)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_9.addWidget(self.frame_settings_2)


        self.gridLayout_2.addWidget(self.frame_global, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 992, 33))
        self.menuFunny = QMenu(self.menubar)
        self.menuFunny.setObjectName(u"menuFunny")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFunny.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFunny.addAction(self.actionGet_statistics_as_txt)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionHelp_me)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Telegram Wordcloud PyQt6", None))
        self.actionGet_statistics_as_txt.setText(QCoreApplication.translate("MainWindow", u"Get statistics as .txt", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp_me.setText(QCoreApplication.translate("MainWindow", u"Help me", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Image", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.generate_vid_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Video", None))
        self.preview_lbl.setText(QCoreApplication.translate("MainWindow", u"*Please generate a Wordcloud to see preview*", None))
        self.lbl_json_file.setText(QCoreApplication.translate("MainWindow", u"Select a .json file with chat:", None))
        self.path_json_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_stop_file.setText(QCoreApplication.translate("MainWindow", u"[OPTIONAL] Select a .txt file with stop keywords:", None))
        self.path_stop_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lbl_png_file.setToolTip(QCoreApplication.translate("MainWindow", u"Select multiple frames to have a possibility to form a video (woah)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_png_file.setText(QCoreApplication.translate("MainWindow", u"[OPTIONAL] Select mask file(s) or video:", None))
        self.path_mask_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_width.setText(QCoreApplication.translate("MainWindow", u"Desired image Width [px]:", None))
        self.lbl_height.setText(QCoreApplication.translate("MainWindow", u"Desired image Height [px]:", None))
        self.lbl_max_word.setText(QCoreApplication.translate("MainWindow", u"Max. amount of words:", None))
        self.lbl_min_word_len.setText(QCoreApplication.translate("MainWindow", u"Min. word length:", None))
        self.lbl_sort_word.setText(QCoreApplication.translate("MainWindow", u"Sort words:", None))
        self.lbl_scaling.setText(QCoreApplication.translate("MainWindow", u"Scaling factor:", None))
        self.path_font_lbl.setText(QCoreApplication.translate("MainWindow", u"[OPTIONAL] Font path:", None))
        self.path_font_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.min_font_size_lbl.setText(QCoreApplication.translate("MainWindow", u"Min. font size:", None))
        self.max_font_size_lbl.setText(QCoreApplication.translate("MainWindow", u"Max. font size (0 - Image height):", None))
        self.font_step_lbl.setText(QCoreApplication.translate("MainWindow", u"Font step:", None))
        self.color_mode_lbl.setText(QCoreApplication.translate("MainWindow", u"Color mode:", None))
        self.color_map_lbl.setText(QCoreApplication.translate("MainWindow", u"Color map:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Background color:", None))
        self.bg_color_edit.setText(QCoreApplication.translate("MainWindow", u"#000000FF", None))
        self.bg_color_pick_btn.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.use_mask_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use a mask when generating image", None))
#if QT_CONFIG(tooltip)
        self.use_mask_colors_chk.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ignore &quot;Color Map&quot; parameter and try to use colors from mask image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_mask_colors_chk.setText(QCoreApplication.translate("MainWindow", u"Use colors from mask", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Mask contour color:", None))
        self.mask_color_edit.setText(QCoreApplication.translate("MainWindow", u"#000000FF", None))
        self.mask_color_pick_btn.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.mask_contour_thick_lbl.setText(QCoreApplication.translate("MainWindow", u"Mask contour thickness:", None))
        self.copyright_lbl.setText(QCoreApplication.translate("MainWindow", u"(c) vledd 2024-2025", None))
        self.menuFunny.setTitle(QCoreApplication.translate("MainWindow", u"More", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About+Help", None))
    # retranslateUi

