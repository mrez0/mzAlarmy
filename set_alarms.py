from PyQt5 import QtWidgets, QtCore
from alarms import Ui_SetAlarms


class SetAlarms(QtWidgets.QDialog):
    """Alarm settings dialog"""

    def __init__(self):
        """Initializing main class"""
        super(SetAlarms, self).__init__()

        self.ui = Ui_SetAlarms()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Setting events
        self.set_events()

        # Reading alarms in text file and populate list
        alarms = self.get_alarms()
        self.populate_alarms(alarms)

        self.exec_()

    def set_events(self):
        self.ui.close_button.clicked.connect(self.close_dialog)
        self.ui.add_button.clicked.connect(self.add_alarm)
        self.ui.alarms_list.currentItemChanged.connect(self.enable_remove_button)

    def add_alarm(self):
        time = self.ui.timeEdit.time().toString('hh:mm') # Converting QTimeEdit to str
        QtWidgets.QListWidgetItem(time, self.ui.alarms_list)

    def enable_remove_button(self):
        self.ui.remove_button.setEnabled(True)

    def close_dialog(self):
        """Save alarms from list to file and close"""
        alarms = []
        for index in range(self.ui.alarms_list.count()):
            alarms.append(self.ui.alarms_list.item(index).text())

        alarms_str = ','.join(alarms)
        f = open('alarms.txt', 'w+')
        f.write(alarms_str)
        f.close()
        self.close()

    def get_alarms(self):
        f = open('alarms.txt', 'r')
        alarms_str = f.read()
        alarms_list = alarms_str.split(',')
        f.close()
        return alarms_list

    def populate_alarms(self, alarms):
        for alarm in alarms:
            if alarm:
                QtWidgets.QListWidgetItem(alarm, self.ui.alarms_list)