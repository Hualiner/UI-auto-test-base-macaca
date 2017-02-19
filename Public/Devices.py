import os


class Devices:
    """获取连接的设备的信息"""
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        self.GET_IOS = "instruments -s devices"

    def get_devices(self):
        value = os.popen(self.GET_ANDROID)

        devices = []

        for v in value.readlines():
            android = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                android['platformName'] = 'Android'
                android['udid'] = s_value[:s_value.find('device')].strip()
                android['package'] = 'com.platform.jhj'
                # android['activity'] = 'xxxxxx'

                devices.append(android)

        # value = os.popen(self.GET_IOS)
        #
        # for v in value.readlines():
        #     iOS = {}
        #
        #     s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")
        #
        #     if v.rfind('Simulator') != -1:
        #         continue
        #     if v.rfind("(") == -1:
        #         continue
        #
        #     iOS['platformName'] = 'iOS'
        #     iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
        #     iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
        #     iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
        #     iOS['bundleId'] = 'xxxx'
        #
        #     device.append(iOS)

        return devices
