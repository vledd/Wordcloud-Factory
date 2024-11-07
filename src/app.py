import json
import numpy
from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageColor
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
from matplotlib import colormaps

import telegram_parse_helpers as parsehelp
from constants import ParserSortWords

from gui_main import Ui_MainWindow

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw

import time

# Window with the main software functionality
class MainScreenWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.json_path = None
        self.stopwords_path = None
        self.mask_path = None
        self.wordcloud_image = None
        self.wordcloud_image_qt = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.statusbar.showMessage("Awaiting .json file...")

        self.ui.sort_combo.addItems(("Most Popular", "Least Popular"))
        self.ui.color_mode_combo.addItems(("RGB", "RGBA"))
        self.ui.color_map_combo.addItems(list(colormaps))

        self.ui.path_json_btn.clicked.connect(self.get_json_path)
        self.ui.path_stop_btn.clicked.connect(self.get_stopwords_path)
        self.ui.path_mask_btn.clicked.connect(self.get_mask_path)
        self.ui.generate_btn.clicked.connect(self.generate_wordcloud)
        self.ui.use_mask_chkbox.clicked.connect(self.use_mask_clicked)
        self.ui.save_btn.clicked.connect(self.save_wordcloud)
        self.ui.bg_color_pick_btn.clicked.connect(self.pick_bg_color)

    def use_mask_clicked(self):
        if self.ui.use_mask_chkbox.isChecked():
            self.ui.use_mask_colors_chk.setEnabled(True)
            # Disable size controls, they are overridden by mask dimensions
            self.ui.img_width_spin.setEnabled(False)
            self.ui.img_height_spin.setEnabled(False)
        else:
            self.ui.use_mask_colors_chk.setEnabled(False)
            self.ui.img_width_spin.setEnabled(True)
            self.ui.img_height_spin.setEnabled(True)


    def get_json_path(self):
        """
        Open file dialog to get a path for .JSON file with Telegram messages.
        :return: None
        """
        self.json_path = qtw.QFileDialog.getOpenFileName(self, "Select File", filter="JSON File (*.json)")[0]
        if len(self.json_path) == 0:
            # TODO it would be nice to additionally add some validation functionality.
            # At least so it would check for ["message"] fields in JSON.
            self.ui.path_json_edit.setText("No valid file provided!")
            self.ui.preview_lbl.setEnabled(False)
            self.ui.generate_btn.setEnabled(False)
            self.ui.save_btn.setEnabled(False)
            self.ui.statusbar.showMessage("Awaiting .json file...")
        else:
            self.ui.path_json_edit.setText(str(self.json_path))
            self.ui.preview_lbl.setEnabled(True)
            self.ui.generate_btn.setEnabled(True)
            self.ui.save_btn.setEnabled(True)
            self.ui.statusbar.showMessage("Ready!")

    def get_stopwords_path(self):
        """
        Open file dialog to get a path for .txt file with stopwords.
        :return: None
        """
        self.stopwords_path = qtw.QFileDialog.getOpenFileName(self, "Select File", filter="Stop words (*.txt)")[0]
        if len(self.stopwords_path) == 0:
            self.ui.path_stop_edit.setText("No valid file provided!")
            self.ui.statusbar.showMessage("Failed to load stopwords...")
            self.stopwords_path = None  # This is needed in order to not break logic
        else:
            self.ui.path_stop_edit.setText(str(self.stopwords_path))
            self.ui.statusbar.showMessage("Stopwords load OK")

    def get_mask_path(self):
        """
        Open file dialog to get a path for image mask.
        :return: None
        """
        # FIXME I also want PNG but it requires more study bc it immediately crashes rn
        self.mask_path = qtw.QFileDialog.getOpenFileName(self,
                                                        "Select File",
                                                        filter="Mask files (*.jpg)")[0]
        if len(self.mask_path) == 0:
            self.ui.path_mask_edit.setText("No valid file provided!")
            self.ui.statusbar.showMessage("Failed to load mask...")
            self.mask_path = None  # This is needed in order to not break logic
            self.ui.use_mask_chkbox.setEnabled(False)
            self.ui.use_mask_chkbox.setChecked(False)
        else:
            self.ui.path_mask_edit.setText(str(self.mask_path))
            self.ui.statusbar.showMessage("Mask load OK")
            self.ui.use_mask_chkbox.setEnabled(True)

    def generate_wordcloud(self):
        # -----------------------------------------------------
        # Load JSON file
        json_file = open(self.json_path, 'r', encoding="utf-8")
        json_read = json_file.read()
        json_data = json.loads(json_read)
        json_file.close()

        # -----------------------------------------------------
        # Load Stopwords if path is provided
        if self.stopwords_path is not None:
            stopword_file = open(self.stopwords_path, 'r', encoding="utf-8")
            stopword_read = stopword_file.read().splitlines()
            stopword_file.close()
        else:
            # Otherwise skip
            stopword_read = None
        # -----------------------------------------------------

        # -----------------------------------------------------
        sort_type: ParserSortWords
        if self.ui.sort_combo.currentText() == "Most Popular":
            sort_type = ParserSortWords.DESCENDING
        else:
            sort_type = ParserSortWords.ASCENDING
        # -----------------------------------------------------

        # TODO Revise a bit later
        mask_numpy = None
        if self.ui.use_mask_chkbox.isChecked():
            if self.mask_path is not None:
                # TODO Taken from Wordcloud Lib exampled. Needs a deeper study
                mask_data = numpy.array(Image.open(self.mask_path))
                image_colors = ImageColorGenerator(mask_data)
                mask_numpy = mask_data.copy()
                mask_numpy[mask_numpy.sum(axis=2) == 0] = 255  # Wuzz dat??

        # Make NONE if 0 is selected since Wordcloud lib accepts only such logic
        if int(self.ui.max_font_size_spin.text()) == 0:
            max_font_size = None
        else:
            max_font_size = int(self.ui.max_font_size_spin.text())

        # Parse data
        words_list: list[str] = (
            list(word[0] for word in parsehelp.parse_json_chat(json_data,
                                                               min_word_size=int(self.ui.min_word_len_spin.text()),
                                                               sorting=sort_type))
        )

        # FIXME if no words provided in list (for example min_word_len is too big, thing crashes)
        wc = WordCloud(width=int(self.ui.img_width_spin.text()),
                       height=int(self.ui.img_height_spin.text()),
                       stopwords=stopword_read,
                       background_color=self.hex_color_to_tuple(self.ui.bg_color_edit.text()),
                       max_words=int(self.ui.max_word_spin.text()),
                       colormap=self.ui.color_map_combo.currentText(),
                       scale=float(self.ui.scaling_spin.text()),
                       mode=self.ui.color_mode_combo.currentText(),
                       mask=mask_numpy,
                       min_font_size=int(self.ui.min_font_size_spin.text()),
                       max_font_size=max_font_size,)

        wc.generate(" ".join(words_list))

        # Only recolor when needed
        if self.ui.use_mask_colors_chk.isChecked():
            wc.recolor(color_func=image_colors)

        self.wordcloud_image = wc.to_image()  # For future saving purposes
        self.wordcloud_image_qt = ImageQt(self.wordcloud_image)
        # Spandau Ballet "Journeys To Glory" album everyone listen who reads this (c) vled & ruslan4ik
        self.ui.preview_lbl.setPixmap(qtg.QPixmap.fromImage(self.wordcloud_image_qt))

    def pick_bg_color(self):
        # TODO ShowAlphaChannel could vary regarding on which mode is selected in combo. For now always on
        color = qtw.QColorDialog.getColor(options=qtw.QColorDialog.ColorDialogOption.ShowAlphaChannel)
        # Very dirty hack to move Alpha channel at the end of the string
        hexcolor = color.name(qtg.QColor.NameFormat.HexRgb) + color.name(qtg.QColor.NameFormat.HexArgb)[1:3]
        self.ui.bg_color_edit.setText(hexcolor.upper())

    def save_wordcloud(self):
        if self.wordcloud_image is not None:
            save_path = qtw.QFileDialog.getSaveFileName(self,
                                                        "Select directory where to save wordcloud",
                                                        filter="Wordcloud (*.png)",
                                                        directory="wordcloud.png")
            if save_path[0] != '':
                self.wordcloud_image.save(save_path[0])
        else:
            self.ui.statusbar.showMessage("Nothing to save!")
            qtw.QApplication.beep()

    @staticmethod
    def hex_color_to_tuple(hex_color: str) -> tuple:
        """
        This function converts a HEX string to a tuple. RGB or RGBA.
        Tbh I dunno why wrap one-liner function but I love this wrapper.
        :param hex_color: HEX string with color
        :return: Tuple with colors
        """

        return ImageColor.getrgb(hex_color)


# if __name__ == "main.py":
app = qtw.QApplication([])
app.setStyle("Fusion")
widget = MainScreenWindow()
widget.setWindowTitle("Telegram Wordcloud PyQt6 v0.5.1")

widget.show()

app.exec()
