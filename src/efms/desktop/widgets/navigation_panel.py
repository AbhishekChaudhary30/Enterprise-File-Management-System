from PySide6.QtWidgets import QListWidget


class NavigationPanel(QListWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumWidth(240)

        self.addItems(

            [

                "Dashboard",

                "Workspace",

                "Search",

                "Organizer",

                "Duplicates",

                "Backup",

                "Reports",
                
                "Trash"

                "Settings",

            ]

        )