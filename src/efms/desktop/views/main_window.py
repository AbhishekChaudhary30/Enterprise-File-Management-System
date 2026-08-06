from logging import root

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QMainWindow,
)

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QMessageBox,
)

from efms.desktop.controllers.application_controller import (
    ApplicationController,
)

from efms.desktop.widgets.menu_bar import MenuBar
from efms.desktop.widgets.navigation_panel import NavigationPanel
from efms.desktop.widgets.status_bar import StatusBar
from efms.desktop.widgets.tool_bar import ToolBar
from efms.desktop.widgets.workspace import Workspace


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.controller = ApplicationController()

        self.setWindowTitle(

            "Enterprise File Management System"

        )

        self.resize(

            1400,

            850,

        )

        self.menu = MenuBar()

        self.toolbar = ToolBar()

        self.status = StatusBar()

        self.navigation = NavigationPanel()

        self.workspace = Workspace()

        self.setMenuBar(

            self.menu

        )

        self.addToolBar(

            Qt.TopToolBarArea,

            self.toolbar,

        )

        self.setStatusBar(

            self.status

        )

        central = QWidget()

        layout = QHBoxLayout()

        layout.addWidget(

            self.navigation

        )

        layout.addWidget(

            self.workspace,

            1,

        )

        central.setLayout(layout)

        self.setCentralWidget(

            central

        )

        self.workspace.browse_button.clicked.connect(

            self.scan_selected_folder

        )
        
        self.workspace.search_button.clicked.connect(
            self.search_files
        )
        
        self.navigation.currentRowChanged.connect(
            self.change_page
        )
        
        self.workspace.organize_button.clicked.connect(
            self.organize_files
        )
        
        self.workspace.duplicate_button.clicked.connect(
            self.find_duplicates
        )
        
        self.workspace.backup_button.clicked.connect(
            self.create_backup
        )
        
        self.workspace.report_button.clicked.connect(
            self.generate_report
        )
        
        self.workspace.copy_button.clicked.connect(
            self.copy_file
        )

        self.workspace.move_button.clicked.connect(
            self.move_file
        )

        self.workspace.rename_button.clicked.connect(
            self.rename_file
        )

        self.workspace.delete_button.clicked.connect(
            self.delete_file
        )
        
        self.toolbar.undo_action.triggered.connect(
            self.undo_operation
        )

        self.toolbar.redo_action.triggered.connect(
            self.redo_operation
        )

        self.toolbar.refresh_action.triggered.connect(
            self.refresh_workspace
        )
        
        self.workspace.trash_restore_button.clicked.connect(
            self.restore_file
        )

        self.workspace.trash_delete_button.clicked.connect(
            self.permanent_delete
        )

    def scan_selected_folder(self):

        directory = self.workspace.current_directory

        if directory is None:

            return

        result = self.controller.scan_directory(

            directory

        )

        self.workspace.load_files(

            result

        )
        
        self.refresh_dashboard()

        self.status.showMessage(

            f"{result['total_files']} files loaded.",

            5000,

        )
        
        self.refresh_dashboard()
        
    def search_files(self):

        root = self.workspace.current_directory

        if root is None:

            self.status.showMessage(
                "Select folder first.",
                3000,
            )

            return

        keyword = self.workspace.search_input.text().strip()

        if not keyword:

            self.status.showMessage(
                "Enter search value.",
                3000,
            )

            return

        search_type = self.workspace.search_type.currentText()

        result = self.controller.search(

            root,

            keyword,

            search_type,

        )

        self.workspace.load_search_results(

            result,

        )

        self.status.showMessage(

            f"{len(result)} file(s) found.",

            5000,

        )
        
        self.refresh_dashboard()
        
    def organize_files(self):

        root = self.workspace.current_directory

        if root is None:

            self.status.showMessage(
                "Select folder first.",
                3000,
            )

            return

        self.controller.organize(root)

        self.workspace.organizer_status.setText(
            "Organization Completed"
        )

        self.status.showMessage(
            "Files organized successfully.",
            5000,
        )

        result = self.controller.scan_directory(root)

        self.workspace.load_files(result)
        
        self.refresh_dashboard()
        
    def find_duplicates(self):

        root = self.workspace.current_directory

        if root is None:

            self.status.showMessage(
                "Select folder first.",
                3000,
            )

            return

        duplicates = self.controller.find_duplicates(
            root
        )

        self.workspace.load_duplicate_results(
            duplicates
        )

        self.status.showMessage(
            f"{len(duplicates)} duplicate group(s) found.",
            5000,
        )
        
        self.refresh_dashboard()
        
    def create_backup(self):

        root = self.workspace.current_directory

        if root is None:

            self.status.showMessage(
                "Select folder first.",
                3000,
            )

            return

        backup_path = self.controller.create_backup(
            root
        )

        self.workspace.backup_status.setText(

            f"Backup Created:\n{backup_path}"

        )

        self.status.showMessage(

            "Backup created successfully.",

            5000,

        )
        
        self.refresh_dashboard()
        
    def generate_report(self):

        root = self.workspace.current_directory

        if root is None:

            self.status.showMessage(
                "Select folder first.",
                3000,
            )

            return

        report_path = self.controller.generate_report(
            root
        )

        self.workspace.report_status.setText(
            f"Report Generated:\n{report_path}"
        )

        self.status.showMessage(
            "Report generated successfully.",
            5000,
        )
        
        self.refresh_dashboard()
        
    def refresh_workspace(self):

        root = self.workspace.current_directory

        if root is None:

            return

        result = self.controller.scan_directory(root)

        self.workspace.load_files(result)
        
        self.refresh_dashboard()
        
    def refresh_dashboard(self):

        root = self.workspace.current_directory

        if root is None:
            return

        files = self.controller.scan_directory(root)["files"]

        folders = self.controller.folder_manager.scan_folders(root)

        duplicates = self.controller.duplicate_service.find_duplicates(root)

        backups = self.controller.backup_service.list_backups()

        reports = list(Path("reports").glob("*"))

        self.workspace.update_dashboard(

            files=len(files),

            folders=len(folders),

            duplicates=len(duplicates),

            backups=len(backups),

            reports=len(reports),

        )
        
        history = self.controller.recent_history()

        self.workspace.update_history(
            history
        )
        
    def copy_file(self):

        source = self.workspace.selected_file()

        if source is None:

            QMessageBox.warning(

                self,

                "Copy",

                "Select a file first.",

            )

            return

        destination = QFileDialog.getExistingDirectory(

            self,

            "Select Destination",

        )

        if not destination:

            return

        destination = Path(destination) / source.name

        self.controller.copy_file(

            source,

            destination,

        )

        self.status.showMessage(

            "Copy completed.",

            5000,

        )
        
        self.scan_selected_folder()


    def move_file(self):

        source = self.workspace.selected_file()

        if source is None:

            QMessageBox.warning(

                self,

                "Move",

                "Select a file first.",

            )

            return

        destination = QFileDialog.getExistingDirectory(

            self,

            "Select Destination",

        )

        if not destination:

            return

        destination = Path(destination) / source.name

        self.controller.move_file(

            source,

            destination,

        )

        self.refresh_workspace()

        self.status.showMessage(

            "Move completed.",

            5000,

        )
        
        self.scan_selected_folder()
        
    def rename_file(self):

        target = self.workspace.selected_file()

        if target is None:

            QMessageBox.warning(

                self,

                "Rename",

                "Select a file first.",

            )

            return

        new_name, ok = QInputDialog.getText(

            self,

            "Rename",

            "New file name:",

            text=target.name,

        )

        if not ok:

            return

        if not new_name.strip():

            return

        self.controller.rename_file(

            target,

            new_name.strip(),

        )

        self.refresh_workspace()

        self.status.showMessage(

            "File renamed successfully.",

            5000,

        )
        
        self.scan_selected_folder()
        
    def delete_file(self):

        target = self.workspace.selected_file()

        if target is None:

            QMessageBox.warning(
                self,
                "Delete",
                "Select a file first.",
            )

            return

        reply = QMessageBox.question(

            self,

            "Delete",

            f"Delete\n\n{target.name} ?",

            QMessageBox.Yes | QMessageBox.No,

        )

        if reply != QMessageBox.Yes:

            return

        self.controller.delete_file(target)

        self.refresh_workspace()

        self.status.showMessage(

            "File deleted successfully.",

            5000,

        )
        
        self.scan_selected_folder()
        
    def undo_operation(self):

        if self.controller.undo():

            self.refresh_workspace()

            self.status.showMessage(

                "Undo completed.",

                3000,

            )


    def redo_operation(self):

        if self.controller.redo():

            self.refresh_workspace()

            self.status.showMessage(

                "Redo completed.",

                3000,

            )
            
    def change_page(self, index):

        self.workspace.show_page(index)

        if index == 7:
            
            self.refresh_trash()

        self.refresh_dashboard()
        
    def refresh_trash(self):

        trash_files = list(
            Path("data/trash").glob("*")
        )

        self.workspace.load_trash(
            trash_files
        )
        
        
    def restore_file(self):

        trash_file = self.workspace.selected_trash_file()
        
        print("=" * 60)
        print(
            "ROW :",
            self.workspace.trash_table.currentRow(),
        )

        print(
            "ITEM :",
            self.workspace.trash_table.currentItem(),
        )
        
        print("=" * 60)
        print("SELECTED :", trash_file)
        print("=" * 60)

        if trash_file is None:
            return

        destination = QFileDialog.getExistingDirectory(
            self,
            "Restore To",
        )

        if not destination:
            return

        self.controller.restore_file(
            trash_file,
            Path(destination) / trash_file.name,
        )

        self.refresh_trash()

        self.refresh_dashboard()

        self.status.showMessage(
            "File restored.",
            3000,
        )
        
    def permanent_delete(self):

        trash_file = self.workspace.selected_trash_file()

        if trash_file is None:
            return

        reply = QMessageBox.question(
            self,
            "Delete",
            f"Permanently delete\n\n{trash_file.name} ?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        self.controller.permanent_delete(
            trash_file
        )

        self.refresh_trash()

        self.refresh_dashboard()

        self.status.showMessage(
            "File permanently deleted.",
            3000,
        )
    