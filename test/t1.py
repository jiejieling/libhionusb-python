from hionusb import api, util
from hionusb.constant import Constant
import ctypes


class DeviceStatus(object):
    """
    设备状态类
    """

    def __init__(self):
        # 设备是否插入
        self.DEVICE_ARRIVAL = False

        # 设备是否绑定事件
        self.DEVICE_BIND = False


def gen_handler():
    ds = DeviceStatus()

    def handler(hwnd, msg, wparam, lparam):
        if msg == Constant.WM_DEVICECHANGE:
            if wparam == Constant.WM_DEVICE:
                ret = api.bind_windows(hwnd)
            # if wparam == Constant.WM_DEVICEADD:
            #     # 设备插入
            #     ds.DEVICE_ARRIVAL = True
            # elif wparam == Constant.WM_DEVICEREMOVE:
            #     # 设备拔出
            #     ds.DEVICE_ARRIVAL = False
            # elif wparam == Constant.WM_DEVICE:
            #     # 话机插入/拔出
            #     if ds.DEVICE_ARRIVAL:
            #         # 话机插入
            #         ret = api.bind_windows(hwnd)
            #         ds.DEVICE_BIND = True
            #     else:
            #         # 话机拔出
            #         # ret = api.unbind_windows()
            #         # ds.DEVICE_BIND = False
            #         pass

        elif msg == Constant.WM_DEVICECONNECT:
            print(f"Device[{wparam}] connect")
            no = b'013716210357'
            f = br'C:\Users\seven\Desktop\temp\1.wav'
            ret = api.offhook_ctrl(0)
            ret = api.start_dial(0, no)
            ret = api.set_talk_record(0, True)
            ret = api.start_record_file(0, f)
            ret = api.set_talk_record(0, False)
            ret = api.hangup_ctrl(0)
            ret = api.stop_record_file(0)
            ret = api.query_phone_status(0)

        elif msg == Constant.WM_DEVICEDISCONNECT:
            print(f"Device[{lparam}] disconnect")

        elif msg == Constant.WM_CALLERID:
            # 呼入事件
            call_in_num = ctypes.c_char_p(lparam).value.decode()
            print(f"Device[{lparam}] get call in from {call_in_num} ")

        return True

    return handler

ret = api.init_dll()
win_msg_handler = util.WinMsgHandler(gen_handler())
win_msg_handler.init()
ret = api.bind_windows(win_msg_handler.get_win())
win_msg_handler.start()
