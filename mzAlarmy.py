import sys, random, _thread

from PyQt5 import QtWidgets, QtCore
from main import Ui_MainWindow

import requests
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

        # Setting events
        self.set_events()

        # Setting alarms
        self.initialize_alarms()

        # Setting alarm mp3
        self.p = vlc.MediaPlayer("ring.mp3")

    def set_events(self):

        # Setting constant timer (ie. setinterval in javascript) to update time on screen
        self.constant_timer = QtCore.QTimer()
        self.constant_timer.timeout.connect(self.update_time)
        self.constant_timer.start(1000)  # run every 1 second

        # Menu events
        self.ui.actionSet_Alarms.triggered.connect(self.open_set_alarms)

        # Change background image every 10 minutes
        self.setting_new_background = False # Flag for preventing repetitive calls to change background specially at short time interval
        self.change_background = QtCore.QTimer()
        self.change_background.timeout.connect(self.new_background)
        self.change_background.start(60000)  # run every 1 minute
        self.new_background()

    def closeEvent(self, event):
        self.p.stop()
        del self.p
        event.accept()

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
        self.p.play()

    def new_background(self):
        """Changing background in new thread"""

        # If setting new image in progress, return from call
        if self.setting_new_background:
            return

        # Changing background in new thread to prevent halt to program time
        _thread.start_new_thread(self.set_background_image, ())

    def set_background_image(self):
        self.setting_new_background = True

        image = self.get_new_image()

        if not image:
            self.setting_new_background = False
            return

        # Saving image from url to file
        with open('background.jpg', 'wb') as handle:
            response = requests.get(image, stream=True)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

        main_window.setStyleSheet('#MainWindow{border-image: url(background.jpg) no-repeat center center fixed;}')
        self.setting_new_background = False

    def get_new_image(self):
        """Getting images from internet"""

        # Check first if images list exist
        try:
            self.background_images_list
            self.background_images_index
        except:
            try:
                url = 'https://pixabay.com/api/?key=8444926-9dec022f8c6a86340c514f12f&q=nature+landscape&image_type=photo&pretty=true'
                response = requests.get(url)
                response_json = response.json()
                self.background_images_list = response_json['hits']
            except:
                return '' # Any error? return empty string
            self.background_images_index = 0

        if self.background_images_list:
            # Getting random photo
            index = random.randint(0, len(self.background_images_list) - 1)
            return self.background_images_list[index]['largeImageURL']


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MzAlarmy()
    main_window.show()
    sys.exit(app.exec_())
