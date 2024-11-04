import json
import numpy
from PIL import Image
from PIL.ImageQt import ImageQt
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt

import telegram_parse_helpers as parsehelp

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
        self.wordcloud_image = None
        self.wordcloud_image_qt = None


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.statusbar.showMessage("Awaiting .json file...")

        self.ui.sort_combo.addItems(("Most Popular", "Least Popular"))
        self.ui.color_mode_combo.addItems(("RGB", "RGBA"))

        self.ui.path_json_btn.clicked.connect(self.get_json_path)
        self.ui.generate_btn.clicked.connect(self.generate_wordcloud)

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

    def generate_wordcloud(self):
        # Load JSON file
        json_file = open(self.json_path, 'r', encoding="utf-8")
        json_read = json_file.read()
        json_data = json.loads(json_read)
        json_file.close()

        # Parse data
        words_list: list[str] = list(word[0] for word in parsehelp.parse_json_chat(json_data))
        wc = WordCloud()
        wc.generate(" ".join(words_list))
        self.wordcloud_image = wc.to_image()
        self.wordcloud_image_qt = ImageQt(self.wordcloud_image)

        self.ui.preview_lbl.setPixmap(qtg.QPixmap.fromImage(self.wordcloud_image_qt))


# if __name__ == "main.py":
app = qtw.QApplication([])
app.setStyle("Fusion")
widget = MainScreenWindow()
widget.setWindowTitle("Telegram Wordcloud PyQt6")

widget.show()

app.exec()
