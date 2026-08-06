import sys

from PySide6.QtWidgets import QApplication

from efms.database.initializer import initialize_database
from efms.desktop.views.main_window import MainWindow


def main():

    initialize_database()      # <-- IMPORTANT

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()