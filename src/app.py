import json
import numpy
from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageColor
from wordcloud import WordCloud, STOPWORDS
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
        self.ui.save_btn.clicked.connect(self.save_wordcloud)
        self.ui.bg_color_pick_btn.clicked.connect(self.pick_bg_color)

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
        self.mask_path = qtw.QFileDialog.getOpenFileName(self,
                                                        "Select File",
                                                        filter="Mask files (*.png *.jpg)")[0]
        if len(self.mask_path) == 0:
            self.ui.path_mask_edit.setText("No valid file provided!")
            self.ui.statusbar.showMessage("Failed to load mask...")
            self.mask_path = None  # This is needed in order to not break logic
        else:
            self.ui.path_mask_edit.setText(str(self.mask_path))
            self.ui.statusbar.showMessage("Mask load OK")

    def generate_wordcloud(self):
        # Load JSON file
        json_file = open(self.json_path, 'r', encoding="utf-8")
        json_read = json_file.read()
        json_data = json.loads(json_read)
        json_file.close()

        # Load Stopwords if path is provided
        if self.stopwords_path is not None:
            stopword_file = open(self.stopwords_path, 'r', encoding="utf-8")
            stopword_read = stopword_file.read().splitlines()
            stopword_file.close()
        else:
            # Otherwise skip
            stopword_read = None

        sort_type: ParserSortWords
        if self.ui.sort_combo.currentText() == "Most Popular":
            sort_type = ParserSortWords.DESCENDING
        else:
            sort_type = ParserSortWords.ASCENDING

        # Parse data
        words_list: list[str] = (
            list(word[0] for word in parsehelp.parse_json_chat(json_data,
                                                               min_word_size=int(self.ui.min_word_len_spin.text()),
                                                               sorting=sort_type))
        )

        wc = WordCloud(width=int(self.ui.img_width_spin.text()),
                       height=int(self.ui.img_height_spin.text()),
                       stopwords=stopword_read,
                       background_color=self.hex_color_to_tuple(self.ui.bg_color_edit.text()),
                       max_words=int(self.ui.max_word_spin.text()),
                       colormap=self.ui.color_map_combo.currentText(),
                       scale=float(self.ui.scaling_spin.text()),
                       mode=self.ui.color_mode_combo.currentText(),)
        wc.generate(" ".join(words_list))
        self.wordcloud_image = wc.to_image()  # For future saving purposes
        self.wordcloud_image_qt = ImageQt(self.wordcloud_image)

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
widget.setWindowTitle("Telegram Wordcloud PyQt6 v0.4")

widget.show()

app.exec()
