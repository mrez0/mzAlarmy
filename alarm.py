from PyQt5 import QtCore




class Alarm():
    def __init__(self, alarm_time, player):
        self.alarm_time = alarm_time
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.trigger)
        self.timer.setSingleShot(True)
        self.player = player

    def set(self):
        self.timer.start(self.alarm_time * 1000)

    def unset(self):
        self.timer.stop()
        self.timer.deleteLater()

    def trigger(self):
        self.player.play()