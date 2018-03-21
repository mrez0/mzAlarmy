import sys

from PyQt5 import QtWidgets, QtCore
from main import Ui_MainWindow

import vlc


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

        # Setting constant timer (ie. setinterval in javascript) to update time on screen
        self.constant_timer = QtCore.QTimer()
        self.constant_timer.timeout.connect(self.update_time)
        self.constant_timer.start(1000)  # run every 1 second

        # Menu events
        self.ui.actionSet_Alarms.triggered.connect(self.open_set_alarms)

        # Setting alarms
        self.initialize_alarms()

        # Setting alarm mp3
        self.p = vlc.MediaPlayer("alarm.mp3")

    def update_time(self):
        """Updating time every second"""
        from datetime import datetime
        now = datetime.now()
        self.ui.hrsLabel.display(now.hour)
        self.ui.minsLabel.display(now.minute)
        self.ui.secsLabel.display(now.second)

    def open_set_alarms(self):
        from set_alarms import SetAlarms

        dialog = SetAlarms()
        self.initialize_alarms()

    def get_alarms(self):
        f = open('alarms.txt', 'r')
        alarms_str = f.read()
        alarms_list = alarms_str.split(',')
        f.close()
        return alarms_list

    def initialize_alarms(self):
        from helpers import get_seconds_to_alarm

        alarms_list = self.get_alarms()
        for alarm_item in alarms_list:
            seconds_to_alarm = get_seconds_to_alarm(alarm_item)
            alarm_timer = QtCore.QTimer()
            alarm_timer.singleShot(int(seconds_to_alarm * 1000), self.alarm)

    def alarm(self):
        print('tick')
        self.p.play()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MzAlarmy()
    main_window.show()
    sys.exit(app.exec_())
