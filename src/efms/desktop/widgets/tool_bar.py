from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class ToolBar(QToolBar):

    def __init__(self):

        super().__init__("Main Toolbar")

        self.undo_action = QAction("Undo", self)

        self.redo_action = QAction("Redo", self)

        self.refresh_action = QAction("Refresh", self)

        self.addAction(self.undo_action)

        self.addAction(self.redo_action)

        self.addSeparator()

        self.addAction(self.refresh_action)