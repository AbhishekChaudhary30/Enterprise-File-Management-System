from pathlib import Path
from PySide6.QtWidgets import QListWidget

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog,
    QStackedWidget,
    QComboBox,
)


class Workspace(QWidget):

    def __init__(self):

        super().__init__()

        self.stack = QStackedWidget()

        self.current_directory = None

        self.stack.addWidget(self.create_dashboard_page())
        self.stack.addWidget(self.create_workspace_page())
        self.stack.addWidget(self.create_search_page())
        self.stack.addWidget(self.create_organizer_page())
        self.stack.addWidget(self.create_duplicate_page())
        self.stack.addWidget(self.create_backup_page())
        self.stack.addWidget(self.create_reports_page())
        self.stack.addWidget(self.create_trash_page())

        layout = QVBoxLayout()

        layout.addWidget(self.stack)

        self.setLayout(layout)

    def create_dashboard_page(self):

        page = QWidget()

        self.dashboard_title = QLabel(
            "Enterprise File Management System"
        )

        self.dashboard_title.setStyleSheet(
            "font-size:24px;font-weight:bold;"
        )

        self.total_files_label = QLabel(
            "Total Files : 0"
        )

        self.total_folders_label = QLabel(
            "Total Folders : 0"
        )

        self.total_duplicates_label = QLabel(
            "Duplicate Groups : 0"
        )

        self.total_backups_label = QLabel(
            "Backups : 0"
        )

        self.total_reports_label = QLabel(
            "Reports : 0"
        )

        layout = QVBoxLayout()

        layout.addWidget(self.dashboard_title)

        layout.addSpacing(20)

        layout.addWidget(self.total_files_label)

        layout.addWidget(self.total_folders_label)

        layout.addWidget(self.total_duplicates_label)

        layout.addWidget(self.total_backups_label)

        layout.addWidget(self.total_reports_label)
        
        layout.addSpacing(25)

        layout.addWidget(
            QLabel("Recent Operations")
        )

        self.history_list = QListWidget()

        layout.addWidget(
            self.history_list
        )

        layout.addStretch()

        page.setLayout(layout)

        return page
    
    def create_workspace_page(self):

        page = QWidget()

        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)

        self.browse_button = QPushButton("Browse Folder")

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(
            [
                "File Name",
                "Location",
            ]
        )

        self.copy_button = QPushButton("Copy")
        self.move_button = QPushButton("Move")
        self.rename_button = QPushButton("Rename")
        self.delete_button = QPushButton("Delete")

        top_layout = QHBoxLayout()

        top_layout.addWidget(
            QLabel("Selected Folder")
        )

        top_layout.addWidget(
            self.path_edit,
            1,
        )

        top_layout.addWidget(
            self.browse_button
        )

        button_layout = QHBoxLayout()

        button_layout.addWidget(
            self.copy_button
        )

        button_layout.addWidget(
            self.move_button
        )

        button_layout.addWidget(
            self.rename_button
        )

        button_layout.addWidget(
            self.delete_button
        )

        layout = QVBoxLayout()

        layout.addLayout(
            top_layout
        )

        layout.addWidget(
            QLabel("Files")
        )

        layout.addLayout(
            button_layout
        )

        layout.addWidget(
            self.table,
            1,
        )

        page.setLayout(
            layout
        )

        self.browse_button.clicked.connect(
            self.select_folder
        )

        return page
    
    def create_search_page(self):

        page = QWidget()

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Enter filename..."
        )

        self.search_type = QComboBox()

        self.search_type.addItems(
            [
                "Name",
                "Extension",
                "Keyword",
            ]
        )

        self.search_button = QPushButton(
            "Search"
        )

        self.search_table = QTableWidget()

        self.search_table.setColumnCount(2)

        self.search_table.setHorizontalHeaderLabels(
            [
                "File Name",
                "Location",
            ]
        )

        top = QHBoxLayout()

        top.addWidget(self.search_input)

        top.addWidget(self.search_type)

        top.addWidget(self.search_button)

        layout = QVBoxLayout()

        layout.addLayout(top)

        layout.addWidget(self.search_table)

        page.setLayout(layout)

        return page
    
    def create_organizer_page(self):

        page = QWidget()

        self.organize_button = QPushButton(
            "Organize Files By Extension"
        )

        self.organizer_status = QLabel(
            "Ready"
        )

        layout = QVBoxLayout()

        layout.addWidget(self.organize_button)

        layout.addWidget(self.organizer_status)

        layout.addStretch()

        page.setLayout(layout)

        return page
    
    def create_duplicate_page(self):

        page = QWidget()

        self.duplicate_button = QPushButton(
            "Find Duplicate Files"
        )

        self.duplicate_table = QTableWidget()

        self.duplicate_table.setColumnCount(2)

        self.duplicate_table.setHorizontalHeaderLabels(
            [
                "Hash",
                "Files",
            ]
        )

        layout = QVBoxLayout()

        layout.addWidget(self.duplicate_button)

        layout.addWidget(self.duplicate_table)

        page.setLayout(layout)

        return page
    
    def create_backup_page(self):

        page = QWidget()

        self.backup_button = QPushButton(
            "Create Backup"
        )

        self.backup_status = QLabel(
            "Ready"
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self.backup_button
        )

        layout.addWidget(
            self.backup_status
        )

        layout.addStretch()

        page.setLayout(layout)

        return page
    
    def create_reports_page(self):

        page = QWidget()

        self.report_button = QPushButton(
            "Generate Report"
        )

        self.report_status = QLabel(
            "Ready"
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self.report_button
        )

        layout.addWidget(
            self.report_status
        )

        layout.addStretch()

        page.setLayout(layout)

        return page
    
    def create_trash_page(self):

        page = QWidget()

        self.trash_restore_button = QPushButton(
            "Restore"
        )

        self.trash_delete_button = QPushButton(
            "Delete Permanently"
        )

        self.trash_table = QTableWidget()
        
        from PySide6.QtWidgets import QAbstractItemView
        
        self.trash_table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.trash_table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.trash_table.setColumnCount(2)

        self.trash_table.setHorizontalHeaderLabels(
            [
                "File",
                "Location",
            ]
        )

        button_layout = QHBoxLayout()

        button_layout.addWidget(
            self.trash_restore_button
        )

        button_layout.addWidget(
            self.trash_delete_button
        )

        layout = QVBoxLayout()

        layout.addLayout(button_layout)

        layout.addWidget(
            self.trash_table
        )

        page.setLayout(layout)

        return page

    def create_placeholder(self, title: str):

        page = QWidget()

        layout = QVBoxLayout()

        label = QLabel(f"{title} Module\n\nComing Soon")

        label.setStyleSheet(

            "font-size:18px;"

        )

        layout.addWidget(label)

        page.setLayout(layout)

        return page

    def show_page(self, index: int):

        self.stack.setCurrentIndex(index)

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Folder",

        )

        if not folder:

            return

        self.current_directory = Path(folder)

        self.path_edit.setText(folder)

    def load_files(self, result: dict):

        files = result["files"]

        self.table.setRowCount(len(files))

        for row, file in enumerate(files):

            path = Path(file)
            
            name_item = QTableWidgetItem(path.name)
            
            name_item.setData(Qt.UserRole, str(path))

            self.table.setItem(

                row,

                0,

                name_item,

            )

            self.table.setItem(

                row,

                1,

                QTableWidgetItem(str(path.parent)),

            )

        self.table.resizeColumnsToContents()
        
    def load_search_results(
        self,
        files,
    ):

        self.search_table.setRowCount(
            len(files)
        )

        for row, file in enumerate(files):

            path = Path(file)

            self.search_table.setItem(
                row,
                0,
                QTableWidgetItem(path.name),
            )

            self.search_table.setItem(
                row,
                1,
                QTableWidgetItem(str(path.parent)),
            )

        self.search_table.resizeColumnsToContents()
        
    def load_duplicate_results(
        self,
        duplicates: dict,
    ):

        self.duplicate_table.setRowCount(
            len(duplicates)
        )

        for row, (file_hash, files) in enumerate(
            duplicates.items()
        ):

            self.duplicate_table.setItem(
                row,
                0,
                QTableWidgetItem(file_hash)
            )

            self.duplicate_table.setItem(
                row,
                1,
                QTableWidgetItem(
                    "\n".join(
                        str(file)
                        for file in files
                    )
                )
            )

        self.duplicate_table.resizeColumnsToContents()
        
        
        
    def update_dashboard(
            self,
            files: int,
            folders: int,
            duplicates: int,
            backups: int,
            reports: int,
        ):

            self.total_files_label.setText(
                f"Total Files : {files}"
            )

            self.total_folders_label.setText(
                f"Total Folders : {folders}"
            )

            self.total_duplicates_label.setText(
                f"Duplicate Groups : {duplicates}"
            )

            self.total_backups_label.setText(
                f"Backups : {backups}"
            )

            self.total_reports_label.setText(
                f"Reports : {reports}"
            )
            
    def update_history(
            self,
            history,
        ):

            self.history_list.clear()

            for item in history:

                self.history_list.addItem(

                    f"{item.operation} | "

                    f"{Path(item.target).name} | "

                    f"{item.status}"

                )   
        
    def selected_file(self) -> Path | None:

        row = self.table.currentRow()

        if row < 0:

            return None

        item = self.table.item(
            row,
            0,
        )

        if item is None:

            return None

        full_path = item.data(
            Qt.UserRole,
        )

        if full_path is None:

            return None

        return Path(full_path)
    
    def load_trash(self, files):

        self.trash_table.setRowCount(len(files))

        for row, file in enumerate(files):

            path = Path(file)

            name_item = QTableWidgetItem(path.name)

            name_item.setData(
                Qt.UserRole,
                str(path),
            )

            self.trash_table.setItem(
                row,
                0,
                name_item,
            )

            self.trash_table.setItem(
                row,
                1,
                QTableWidgetItem(str(path.parent)),
            )

        self.trash_table.resizeColumnsToContents()
        
        if len(files) > 0:
            self.trash_table.selectRow(0)
        
    def selected_trash_file(self) -> Path | None:

        row = self.trash_table.currentRow()

        if row < 0:
            return None

        item = self.trash_table.item(row, 0)

        if item is None:
            return None

        full_path = item.data(Qt.UserRole)

        if full_path is None:
            return None

        return Path(full_path)