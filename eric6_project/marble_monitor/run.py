import sys
from PyQt5 import QtWidgets

from ui import Dialog

app = QtWidgets.QApplication(sys.argv)
win = Dialog.Dialog()
win.show()
sys.exit(app.exec())
