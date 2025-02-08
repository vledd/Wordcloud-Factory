import json
import sys

import numpy
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageColor
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
from matplotlib import colormaps
import multiprocessing as mp
import threading as th

import telegram_parse_helpers as parsehelp
from constants import ParserSortWords

from gui_main import Ui_MainWindow

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

import time


def frame_worker(filename, config, progress_queue):
    print(f"Worker {mp.current_process().pid} is processing {filename}")

    mask_data = numpy.array(Image.open(filename))
    image_colors = ImageColorGenerator(mask_data)
    mask_numpy = mask_data.copy()
    mask_numpy = process_mask_colors(config["masking_strategy"], mask_numpy)

    wc = WordCloud(stopwords=config["stopwords"],
                   background_color=config["bg_color"],
                   max_words=config["max_words"],
                   colormap=config["colormap"],
                   scale=config["scale"],
                   mode=config["mode"],
                   mask=mask_numpy,
                   min_font_size=config["min_font_size"],
                   max_font_size=config["max_font_size"],
                   font_step=config["font_step"],
                   contour_color=config["contour_color"],
                   contour_width=config["contour_width"],
                   )

    wc.generate(" ".join(config["words_list"]))

    # Only recolor when needed
    if config["need_recolor"]:
        wc.recolor(color_func=image_colors)

    img = wc.to_image()
    img.save(f"../export/{filename[filename.rfind('/') + 1 ::]}")

    progress_queue.put(1)  # Notify progress


def main_worker(file_lists, config, progress_queue):
    print("Started main worker!")
    # print(file_lists)
    # print(config)
    with mp.Pool(processes=20) as pool:
        pool.starmap(frame_worker, [(job, config, progress_queue) for sublist in file_lists for job in sublist])

    progress_queue.put(2)  # Signal process thread to close (all done)


def process_mask_colors(choice: str, mask: numpy.array):
    if choice == "Black + White are masked":
        # By default, Wordcloud library is already masking out (not generating words) on #FFFFFF
        # Thus we just find all black colors and make it white (for mask)
        mask_blk_color = np.all(mask == [0, 0, 0], axis=-1)
        mask[mask_blk_color] = [255, 255, 255]
    elif choice == "White is masked":
        # Basically do nothing - White is masked by default in Wordcloud library
        # FIXME VERY IMPORTANT add some threshold possibility
        pass
    elif choice == "Black is masked":
        mask_wht_color = np.all(mask == [255, 255, 255], axis=-1)
        mask_blk_color = np.all(mask == [0, 0, 0], axis=-1)
        # Let's do an evil hack -- in order to not hack into lib -- we change mask color to 0xFF - 1
        # Library will ignore it, coloring will be the same
        mask[mask_wht_color] = [254, 254, 254]
        # Make blacks as whites to mask out
        mask[mask_blk_color] = [255, 255, 255]
    elif choice == "None are masked":
        # Use evil hack to draw absolutely everything
        # Very useful when experimenting with different backgrounds!
        mask_wht_color = np.all(mask == [255, 255, 255], axis=-1)
        mask[mask_wht_color] = [254, 254, 254]
    return mask


if __name__ == "__main__":
    # Window with the main software functionality
    class MainScreenWindow(qtw.QMainWindow):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Multiprocessing-related variables
            self.manager = None
            self.cfg_dict = None
            self.progress_queue = None
            self.worker_process = None
            self.jobs_list_split = None
            self.observing_thread = None

            # Main path + misc.
            self.json_path = None
            self.stopwords_path = None
            self.mask_path = None
            self.wordcloud_image = None
            self.wordcloud_image_qt = None

            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            self.ui.statusbar.showMessage("Awaiting .json file...")

            # Add items to combos
            self.ui.sort_combo.addItems(("Most Popular", "Least Popular"))
            self.ui.color_mode_combo.addItems(("RGB", "RGBA"))
            self.ui.color_map_combo.addItems(list(colormaps))
            self.ui.color_to_mask_combo.addItems(("Black + White are masked",
                                                  "Black is masked",
                                                  "White is masked",
                                                  "None are masked"))

            # Connect signals
            self.ui.path_json_btn.clicked.connect(self.get_json_path)
            self.ui.path_stop_btn.clicked.connect(self.get_stopwords_path)
            self.ui.path_mask_btn.clicked.connect(self.get_mask_path)
            self.ui.generate_btn.clicked.connect(self.generate_wordcloud)
            self.ui.generate_vid_btn.clicked.connect(self.generate_video)
            self.ui.use_mask_chkbox.clicked.connect(self.use_mask_clicked)
            self.ui.save_btn.clicked.connect(self.save_wordcloud)
            self.ui.bg_color_pick_btn.clicked.connect(self.pick_bg_color)
            self.ui.mask_color_pick_btn.clicked.connect(self.pick_mask_color)

        def use_mask_clicked(self):
            if self.ui.use_mask_chkbox.isChecked():
                self.ui.use_mask_colors_chk.setEnabled(True)
                self.ui.color_to_mask_combo.setEnabled(True)
                # Disable size controls, they are overridden by mask dimensions
                self.ui.img_width_spin.setEnabled(False)
                self.ui.img_height_spin.setEnabled(False)
            else:
                self.ui.use_mask_colors_chk.setEnabled(False)
                self.ui.color_to_mask_combo.setEnabled(False)
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
                self.ui.generate_vid_btn.setEnabled(False)
                self.ui.statusbar.showMessage("Awaiting .json file...")
            else:
                self.ui.path_json_edit.setText(str(self.json_path))
                self.ui.preview_lbl.setEnabled(True)
                self.ui.generate_btn.setEnabled(True)
                self.ui.save_btn.setEnabled(True)
                # Needed to correctly enable "Generate Video" button
                if self.ui.use_mask_chkbox.isEnabled():
                    self.ui.generate_vid_btn.setEnabled(True)
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
            self.mask_path = qtw.QFileDialog.getOpenFileNames(self,
                                                            "Select File",
                                                             filter="Mask files (*.jpg);;"
                                                                    "Video files (*.mp4)")[0]
            if len(self.mask_path) == 0:
                self.ui.path_mask_edit.setText("No valid file provided!")
                self.ui.statusbar.showMessage("Failed to load mask...")
                self.mask_path = None  # This is needed in order to not break logic
                self.ui.use_mask_chkbox.setEnabled(False)
                self.ui.use_mask_chkbox.setChecked(False)
                self.ui.generate_vid_btn.setEnabled(False)
            else:
                self.ui.path_mask_edit.setText(str(self.mask_path))
                self.ui.statusbar.showMessage("Mask load OK")
                self.ui.use_mask_chkbox.setEnabled(True)
                # This is needed to enable Generate Video button only if .json words are correctly parsed
                # I can understand it if generate and save buttons are active.
                if self.ui.generate_btn.isEnabled():
                    self.ui.generate_vid_btn.setEnabled(True)

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
                    mask_data = numpy.array(Image.open(self.mask_path[0]))
                    image_colors = ImageColorGenerator(mask_data)
                    mask_numpy = mask_data.copy()

                    # Mask out colors stated in combo box
                    mask_numpy = process_mask_colors(self.ui.color_to_mask_combo.currentText(), mask_numpy)
                    # For debug purposes
                    # Image.fromarray(mask_numpy, mode='RGB').show()

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

            if len(words_list) == 0:
                self.ui.statusbar.showMessage("All words filtered! Nothing to show...")
                qtw.QApplication.beep()
                return

            wc = WordCloud(width=int(self.ui.img_width_spin.text()),
                           height=int(self.ui.img_height_spin.text()),
                           stopwords=stopword_read,
                           background_color=self.hex_color_to_tuple(self.ui.bg_color_edit.text()),
                           max_words=int(self.ui.max_word_spin.text()),
                           colormap=self.ui.color_map_combo.currentText(),
                           scale=float(self.ui.scaling_spin.text().replace(',', '.')),
                           mode=self.ui.color_mode_combo.currentText(),
                           mask=mask_numpy,
                           min_font_size=int(self.ui.min_font_size_spin.text()),
                           max_font_size=max_font_size,
                           font_step=int(self.ui.font_step_spin.text()),
                           contour_color=self.hex_color_to_tuple(self.ui.mask_color_edit.text()),
                           contour_width=int(self.ui.mask_thick_spin.text()),
                           )

            wc.generate(" ".join(words_list))

            # Only recolor when needed
            if self.ui.use_mask_colors_chk.isChecked():
                wc.recolor(color_func=image_colors)

            self.wordcloud_image = wc.to_image()  # For future saving purposes
            self.wordcloud_image_qt = ImageQt(self.wordcloud_image)
            # Spandau Ballet "Journeys To Glory" -->
            # an album everyone who reads this should undoubtedly listen to RIGHT NOW (c) vled & ruslan4ik & qwysam
            self.ui.preview_lbl.setPixmap(qtg.QPixmap.fromImage(self.wordcloud_image_qt))

        @staticmethod
        def split_list_to_jobs(jobs_list: list[str], jobs_num: int):
            for i in range(0, jobs_num):
                yield jobs_list[i::jobs_num]

        def progress_listener(self, progress_queue):
            print("Started listener")
            while True:
                ret: int = progress_queue.get()
                if ret == 2:
                    break
                # print("++Progress")
                self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
            sys.exit(0)  # Properly close the thread


        # FIXME yeah duplications should be removed but need to discuss how to correctly
        # wrap everything in "if`s" and for loops. Let it be a separate func for now (4ever lol)
        def generate_video(self):
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

            if len(words_list) == 0:
                self.ui.statusbar.showMessage("All words filtered! Nothing to show...")
                qtw.QApplication.beep()
                return

            self.jobs_list_split = list(self.split_list_to_jobs(self.mask_path, 20))

            # Manager
            self.manager = mp.Manager()

            self.cfg_dict = self.manager.dict({
                "stopwords": stopword_read,
                "bg_color": self.hex_color_to_tuple(self.ui.bg_color_edit.text()),
                "max_words": int(self.ui.max_word_spin.text()),
                "colormap": self.ui.color_map_combo.currentText(),
                "scale": float(self.ui.scaling_spin.text().replace(',', '.')),
                "mode": self.ui.color_mode_combo.currentText(),
                "min_font_size": int(self.ui.min_font_size_spin.text()),
                "max_font_size": max_font_size,
                "font_step": int(self.ui.font_step_spin.text()),
                "contour_color": self.hex_color_to_tuple(self.ui.mask_color_edit.text()),
                "contour_width": int(self.ui.mask_thick_spin.text()),
                "masking_strategy": self.ui.color_to_mask_combo.currentText(),
                "need_recolor": self.ui.use_mask_colors_chk.isChecked(),
                # TBH this is probably not a very good idea, let's still leave it here for now TODO
                "words_list": words_list,
            })

            # Queue for progress updates
            self.progress_queue = self.manager.Queue()

            self.ui.progressBar.setMaximum(len(self.mask_path))

            # Thread for maintaining the progress bar
            self.observing_thread = th.Thread(target=self.progress_listener,
                                              args=(self.progress_queue,))
            self.observing_thread.start()

            # Start main worker process (brigadier)
            self.worker_process = mp.Process(target=main_worker,
                                             args=(self.jobs_list_split,
                                                   self.cfg_dict,
                                                   self.progress_queue))
            self.worker_process.start()

        def pick_bg_color(self):
            # TODO ShowAlphaChannel could vary regarding on which mode is selected in combo. For now always on
            color = qtw.QColorDialog.getColor(options=qtw.QColorDialog.ColorDialogOption.ShowAlphaChannel)
            # Very dirty hack to move Alpha channel at the end of the string
            hexcolor = color.name(qtg.QColor.NameFormat.HexRgb) + color.name(qtg.QColor.NameFormat.HexArgb)[1:3]
            self.ui.bg_color_edit.setText(hexcolor.upper())

        def pick_mask_color(self):
            # TODO ShowAlphaChannel could vary regarding on which mode is selected in combo. For now always on
            color = qtw.QColorDialog.getColor(options=qtw.QColorDialog.ColorDialogOption.ShowAlphaChannel)
            # Very dirty hack to move Alpha channel at the end of the string
            hexcolor = color.name(qtg.QColor.NameFormat.HexRgb) + color.name(qtg.QColor.NameFormat.HexArgb)[1:3]
            self.ui.mask_color_edit.setText(hexcolor.upper())

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


    app = qtw.QApplication([])
    app.setStyle("Fusion")
    widget = MainScreenWindow()
    widget.setWindowTitle("Telegram Wordcloud PySide6 v0.6.0-rc3")

    widget.show()

    app.exec()
