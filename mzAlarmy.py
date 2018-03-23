import sys, random, _thread

import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QKeyEvent

from alarm_manager import AlarmManager
from main import Ui_MainWindow

from clock import Clock
from background_changer import BackgroundChanger


class MzAlarmy(QtWidgets.QMainWindow):
    """Main application class"""

    def __init__(self):
        """Initializing main class"""
        super(MzAlarmy, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Removing any numbers from lcd's for enhanced user experience at starting of application
        self.ui.hrsLabel.display('')
        self.ui.minsLabel.display('')
        self.ui.secsLabel.display('')

        self.clock = Clock(self.ui.hrsLabel, self.ui.minsLabel, self.ui.secsLabel)
        self.clock.start()
        self.background_changer = BackgroundChanger(self, 'offline', 'backgrounds/*.jpg')
        self.background_changer.sleep(5) # Making sleep to fix bugs during assigning background
        self.background_changer.start()

        # Setting events
        self.set_events()

        self.alarm_manager = AlarmManager('alarms.txt')
        self.alarm_manager.load_alarms()

        # Setting alarms
        #self.initialize_alarms()

        # Setting alarm mp3
        #self.p = vlc.MediaPlayer("ring.mp3")



    def set_events(self):
        # Menu events
        self.ui.actionSet_Alarms.triggered.connect(self.open_set_alarms)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.alarm_manager.stop_alarm()

    def open_set_alarms(self):
        from set_alarms import SetAlarms

        dialog = SetAlarms()
        self.alarm_manager.load_alarms()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = MzAlarmy()
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
