import sys

from efms.database.initializer import initialize_database
from efms.desktop.app import create_application
from efms.desktop.views.main_window import MainWindow


def main():

    initialize_database()

    app = create_application()

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()