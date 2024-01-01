from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class AudioController:
    def __init__(self):
        # Initialize the audio controller with the default audio device
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

    def change_volume(self, new_volume):
        # Set the master volume level to new_volume
        self.volume.SetMasterVolumeLevelScalar(new_volume / 100.0, None)

        # return new volume 
        int(self.volume.GetMasterVolumeLevelScalar() * 100)

    def get_volume(self):
        return int(self.volume.GetMasterVolumeLevelScalar() * 100)
    

