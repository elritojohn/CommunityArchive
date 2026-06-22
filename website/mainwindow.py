from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QTextEdit,
    QGroupBox,
    QComboBox,
    QStatusBar
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Community Archive Migration Assistant")
        self.resize(1400, 900)

        self.build_ui()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        ###########################################################
        # Top toolbar
        ###########################################################

        toolbar = QHBoxLayout()

        self.browseButton = QPushButton("Browse Source Folder")
        self.scanButton = QPushButton("Scan Folder")
        self.importButton = QPushButton("Import Selected")

        toolbar.addWidget(self.browseButton)
        toolbar.addWidget(self.scanButton)
        toolbar.addStretch()
        toolbar.addWidget(self.importButton)

        layout.addLayout(toolbar)

        ###########################################################
        # Main three-column layout
        ###########################################################

        columns = QHBoxLayout()

        ###########################################################
        # Left side
        ###########################################################

        leftGroup = QGroupBox("Collections")

        leftLayout = QVBoxLayout()

        self.collectionTree = QTreeWidget()
        self.collectionTree.setHeaderLabel("Archive Collections")

        QTreeWidgetItem(self.collectionTree, ["Family"])
        QTreeWidgetItem(self.collectionTree, ["Theatre"])
        QTreeWidgetItem(self.collectionTree, ["Photographs"])
        QTreeWidgetItem(self.collectionTree, ["Business"])
        QTreeWidgetItem(self.collectionTree, ["Oral Histories"])

        leftLayout.addWidget(self.collectionTree)

        leftGroup.setLayout(leftLayout)

        ###########################################################
        # Center
        ###########################################################

        centerGroup = QGroupBox("Files")

        centerLayout = QVBoxLayout()

        self.fileList = QListWidget()

        centerLayout.addWidget(self.fileList)

        centerGroup.setLayout(centerLayout)

        ###########################################################
        # Right
        ###########################################################

        rightGroup = QGroupBox("Metadata")

        rightLayout = QVBoxLayout()

        rightLayout.addWidget(QLabel("Subcollection"))

        self.subcollection = QComboBox()
        self.subcollection.addItems([
            "General",
            "Production",
            "Personal",
            "Correspondence",
            "Photographs"
        ])

        rightLayout.addWidget(self.subcollection)

        rightLayout.addWidget(QLabel("Topics"))

        self.topicEditor = QTextEdit()

        rightLayout.addWidget(self.topicEditor)

        rightLayout.addWidget(QLabel("Description"))

        self.descriptionEditor = QTextEdit()

        rightLayout.addWidget(self.descriptionEditor)

        rightGroup.setLayout(rightLayout)

        ###########################################################

        columns.addWidget(leftGroup, 2)
        columns.addWidget(centerGroup, 4)
        columns.addWidget(rightGroup, 3)

        layout.addLayout(columns)

        ###########################################################

        status = QStatusBar()

        status.showMessage("Community Archive Ready")

        self.setStatusBar(status)
