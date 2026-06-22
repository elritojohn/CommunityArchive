#!/usr/bin/env python3

import sys

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Community Archive")
    app.setOrganizationName("WROMP")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
