from hionusb import api, util, constant
import ctypes


def handler(hwnd, msg, wparam, lparam):
    if msg == constant.Constant.WM_DEVICECHANGE:
        # 设备插入/拔出
        # ret = api.bind_windows(hwnd)
        pass

    elif msg == constant.Constant.WM_DEVICECONNECT:
        print(f"Device[{wparam}] connect")

    elif msg == constant.Constant.WM_DEVICEDISCONNECT:
        print(f"Device[{lparam}] disconnect")

    return True


win_msg_handler = util.WinMsgHandler(handler)
win_msg_handler.init()
win_msg_handler.start()
