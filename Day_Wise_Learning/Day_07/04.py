class SmartDevice:
    def __init__(self, _firmware_version="v10"):
        self.name = "Camera"
        self._firmware_version = _firmware_version
        self.__system_key = "SECRET_KEY_123"

    def get_device_status(self):
        print(f"Version: {self._firmware_version}, Device name: {self.name}")


class SmartCamera(SmartDevice):
    def __init__(self, _firmware_version="v10", video_resolution="1080p"):
        super().__init__(_firmware_version)
        self.video_resolution = video_resolution

    def exploit_test(self):
        print(f"Name: {self.name}")
        print(f"Version: {self._firmware_version}")
        # print(self.__system_key)  # This will raise an AttributeError


Living_Room_Camera = SmartCamera()
Living_Room_Camera.get_device_status()
Living_Room_Camera.exploit_test()

print(Living_Room_Camera._SmartDevice__system_key)