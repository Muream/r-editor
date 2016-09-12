from PySide import QtGui
from PySide import QtCore
import r_editor

import sys


def show():
    """Open up the UI."""

    app = QtGui.QApplication(sys.argv)

    ui = ReditorUI()
    ui.show()
    app.exec_()
    sys.exit()


class ReditorUI(QtGui.QMainWindow):
    """Base UI class."""

    def __init__(self, *args, **kwargs):
        super(ReditorUI, self).__init__(*args, **kwargs)

        self.subreddit = ""
        self.sorting = ""
        self.time = ""
        self.maxPosts = 0

        self.createCentralWidget()
        self.create_reddit_layout()
        self.create_clips_layout()
        self.create_redit_layout()
        self.setWindowTitle('r-editor')

    def createCentralWidget(self):
        """
        """
        self.setCentralWidget(QtGui.QWidget())
        self.centralWidget().setLayout(QtGui.QVBoxLayout())

    def create_reddit_layout(self):
        """
        """
        self.redditLayout = QtGui.QHBoxLayout()

        self.subredditTxtBox = QtGui.QLineEdit()
        self.sortingCB = QtGui.QComboBox()
        self.timeCB = QtGui.QComboBox()

        self.subredditTxtBox.setPlaceholderText("Subreddit...")

        self.sortingCB.addItem("Top")
        self.sortingCB.addItem("Hot")
        self.sortingCB.addItem("New")
        self.sortingCB.addItem("Rising")
        self.sortingCB.currentIndexChanged.connect(self.lock_times)

        self.timeCB.addItem("Hour")
        self.timeCB.addItem("Day")
        self.timeCB.addItem("Week")
        self.timeCB.addItem("Month")
        self.timeCB.addItem("Year")
        self.timeCB.addItem("All Time")

        self.redditLayout.addWidget(self.subredditTxtBox)
        self.redditLayout.addWidget(self.sortingCB)
        self.redditLayout.addWidget(self.timeCB)

        self.centralWidget().layout().addLayout(self.redditLayout)

    def create_clips_layout(self):
        self.clipsLayout = QtGui.QHBoxLayout()
        # Todo use QtGui.QSpinBox
        self.clipsSB = QtGui.QSpinBox()
        self.clipsLayout.addWidget(self.clipsSB)

        self.centralWidget().layout().addLayout(self.clipsLayout)

    def create_redit_layout(self):
        self.launchLayout = QtGui.QHBoxLayout()
        self.launchButton = QtGui.QPushButton("r-edit!")

        self.launchButton.released.connect(self.do_edit_clips)

        self.launchLayout.addWidget(self.launchButton)

        self.centralWidget().layout().addLayout(self.launchLayout)

    def do_edit_clips(self):
        r_editor.main(self.subredditTxtBox.text())

    def lock_times(self):
        if self.sortingCB.currentText() == "Top":
            self.timeCB.setEnabled(True)
        else:
            self.timeCB.setEnabled(False)

if __name__ == '__main__':
    show()
