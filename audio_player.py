from pygame import mixer # Load the required library

class AudioPlayer():
    def __init__(self, audio_file):
        mixer.init()
        mixer.music.load(audio_file)

    def play(self):
        mixer.music.play()

    def stop(self):
        mixer.music.stop()

    def pause(self):
        mixer.music.pause()

    def resume(self):
        mixer.music.unpause()