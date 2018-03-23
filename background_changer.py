import glob, random
from shutil import copy

import requests
from PIL import Image
from PyQt5 import QtCore


class BackgroundChanger(QtCore.QThread):
    def __init__(self, main_window, source, location):
        super(BackgroundChanger, self).__init__()
        self.main_window = main_window
        self.source = source
        self.location = location
        self.images = []
        self.background = 'background.jpg'

        # Setting flag when getting image online so decline any call to update background if in progress
        self.changing_to_online_image = False

        # Starting new thread
        # self.start()

    def get_images(self):
        if self.source == 'offline':
            self.images = self.get_offline_images()
        else:
            self.images = self.get_online_images()

        if not self.images:
            self.images = []

    def get_online_images(self):
        try:
            url = 'https://pixabay.com/api/?key=8444926-9dec022f8c6a86340c514f12f&q=nature+landscape&image_type=photo&pretty=true'
            response = requests.get(url)
            response_json = response.json()
            return response_json['hits']
        except:
            return  # Any error? return None

    def get_offline_images(self):
        return glob.glob(self.location)

    def change_background(self):
        if not len(self.images):
            return

        if self.source == 'online':
            self.change_online_background()
        else:
            self.change_offline_background()

    def change_online_background(self):
        if self.changing_to_online_image:
            return

        self.changing_to_online_image = True

        index = random.randint(0, len(self.images) - 1)

        image_url = self.images[index]['largeImageURL']

        # Saving image from url to file
        try:
            with open('background.jpg', 'wb') as handle:
                response = requests.get(image_url, stream=True)

                for block in response.iter_content(1024):
                    if not block:
                        self.setting_new_background = False
                        return

                    handle.write(block)

        except:
            self.setting_new_background = False
            return

        # My image is a 200x374 jpeg that is 102kb large
        foo = Image.open("background.jpg")

        # I downsize the image with an ANTIALIAS filter (gives the highest quality)
        foo = foo.resize((160, 300), Image.ANTIALIAS)
        foo.save("background.jpg", optimize=True, quality=95)
        # The saved downsized image size is 22.9kb

        copy('background.jpg', 'background2.jpg')

        if self.background == 'background.jpg':
            self.background = 'background1.jpg'
        else:
            self.background = 'background.jpg'


        style = '#MainWindow{border-image: url("%s") no-repeat center center fixed;}' % self.background

        self.main_window.setStyleSheet(style)

        self.changing_to_online_image = False

    def change_offline_background(self):
        index = random.randint(0, len(self.images) - 1)
        image_file = self.images[index].replace('\\', '/')
        style = '#MainWindow{border-image: url("%s") no-repeat center center fixed;}' % image_file


        self.main_window.setStyleSheet(style)

    def run(self):
        self.get_images()

        # Setting timer to change background every 5 seconds
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_background)
        self.timer.start(15000)
        self.change_background()
        self.exec_()
