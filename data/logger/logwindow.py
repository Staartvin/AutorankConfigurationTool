import datetime
import typing

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QFont


class LogWindow(QtWidgets.QMainWindow):
    logged_messages_model: typing.Optional["LogMessageModel"] = None
    instance: "LogWindow" = None

    def __init__(self, *args, **kwargs):
        super(LogWindow, self).__init__(*args, **kwargs)
        LogWindow.logged_messages_model = LogMessageModel()

        # Load the UI Page
        uic.loadUi('logging_window.ui', self)

        self.loggingView.setModel(LogWindow.logged_messages_model)

    @staticmethod
    def log_message(message: str):
        if message is not None:
            LogWindow.logged_messages_model.log_messages.append((datetime.datetime.now(), message))
            # Tell Qt we've added data
            LogWindow.logged_messages_model.layoutChanged.emit()
            LogWindow.instance.loggingView.resizeColumnsToContents()

    @staticmethod
    def clear_logger():
        # Clear the log and tell Qt we've changed the list
        LogWindow.logged_messages_model.log_messages.clear()
        LogWindow.logged_messages_model.layoutChanged.emit()


class LogMessageModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, log_messages=None, **kwargs):
        super(LogMessageModel, self).__init__(*args, **kwargs)
        self.log_messages = log_messages or []

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            date_time, message = self.log_messages[index.row()]

            if index.column() == 0:
                return date_time.strftime("%Y/%m/%d %H:%M:%S")
            else:
                return message

        if role == Qt.FontRole:
            if index.column() == 1:
                font = QFont()
                font.setBold(True)
                return font

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.log_messages)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 2

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Time"
            else:
                return "Message"
        if role == Qt.FontRole:
            if section == 1:
                font = QFont()
                font.setBold(True)
                return font
