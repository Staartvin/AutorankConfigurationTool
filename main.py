from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys

import data.datamanager.datamanager
import data.pathdata
import data.logger.logwindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.data_manager = data.datamanager.datamanager.DataManager()
        self.log_window = data.logger.logwindow.LogWindow()
        data.logger.logwindow.LogWindow.instance = self.log_window

        # Load the UI Page
        uic.loadUi('mainwindow.ui', self)

        self.setWindowTitle("Autorank Configuration Tool")

        self.load_autorank_folder.triggered.connect(self.click_load_autorank_folder)
        self.open_logger_button.triggered.connect(self.open_logger_window)
        self.clear_logger_button.triggered.connect(self.clear_logger_window)

    def closeEvent(self, event) -> None:
        # Close log window when main window closes
        if self.log_window is not None:
            self.log_window.close()
        event.accept()

    def click_load_autorank_folder(self):
        # Open dialog to load Autorank folder
        file_dialog = QFileDialog(self)

        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.Directory)
        file_dialog.setWindowTitle("Select your Autorank folder")

        is_valid_folder = False

        while not is_valid_folder:
            if not file_dialog.exec_():
                # User didn't select a folder, so we just stop here.
                return

            # Check if the selected folder is a valid Autorank folder
            is_valid_folder = self.data_manager.is_valid_autorank_folder(file_dialog.selectedFiles()[0])

            # If it is not valid, make sure to tell the user
            if not is_valid_folder:
                error_dialog = QMessageBox(self)

                error_dialog.setText("The folder you selected was not a valid Autorank folder. It should contain at "
                                     "least a Paths.yml and Settings.yml file.")
                error_dialog.exec_()

        self.data_manager.set_autorank_folder_path(file_dialog.selectedFiles()[0])

        # Load Paths file
        self.data_manager.load_paths_file()

        # Show message in bar.
        self.statusBar().showMessage(f"Loaded Autorank folder '{self.data_manager.autorank_folder}'", 10 * 1000)

    def open_logger_window(self):
        if not self.log_window.isVisible():
            self.statusBar().showMessage("Opening logger window", 5000)
            self.log_window.show()
        else:
            # The window is already open, so just raise it to draw the attention to the user.
            self.log_window.raise_()

    def clear_logger_window(self):
        self.log_window.clear_logger()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
