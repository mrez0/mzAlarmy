from helpers import get_seconds_to_alarm

from alarm import Alarm
from audio_player import AudioPlayer


class AlarmManager():
    def __init__(self, alarms_file):
        self.alarms_file = alarms_file
        self.alarms_list = []
        self.player = AudioPlayer('ring.mp3')

    def add_alarm(self):
        pass

    def remove_alarm(self):
        pass

    def load_alarms(self):
        """Preventing old alarms from triggering and starting new alarm list from file"""
        if self.alarms_list:
            for alarm in self.alarms_list:
                alarm.unset()

        self.alarms_list = []

        f = open(self.alarms_file, 'r')
        alarms_str = f.read()
        f.close()

        if not alarms_str:
            return

        alarms_list = alarms_str.split(',')

        for alarm_time in alarms_list:
            seconds_to_alarm = get_seconds_to_alarm(alarm_time)
            alarm = Alarm(seconds_to_alarm, self.player)
            alarm.set()
            self.alarms_list.append(alarm)

    def stop_alarm(self):
        self.player.stop()

