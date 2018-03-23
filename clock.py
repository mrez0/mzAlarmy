from datetime import datetime

from PyQt5 import QtCore


class Clock(QtCore.QThread):
    def __init__(self, lcd_hr, lcd_min, lcd_sec):
        super(Clock, self).__init__()

        self.lcd_hr = lcd_hr
        self.lcd_min = lcd_min
        self.lcd_sec = lcd_sec

        # self.start()

    def update_time(self):
        hours, minutes, seconds = self.get_current_time()

        self.lcd_hr.display(hours)
        self.lcd_min.display(minutes)
        self.lcd_sec.display(seconds)

    def get_current_time(self):
        now = datetime.now()
        return [now.hour, now.minute, now.second]

    def run(self):
        # Setting timer to run every 1 second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # run every 1 minute

        self.exec_()