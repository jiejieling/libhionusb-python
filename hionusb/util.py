import ctypes
import time

import win32con
import win32gui
import ctypes.wintypes


class WinMsgHandler(object):
    """
    Windows MSG 处理类
    """
    # 定义回调函数类型
    DeviceChangeCallback = ctypes.WINFUNCTYPE(
        ctypes.wintypes.BOOL,  # 返回值类型
        ctypes.wintypes.HWND,  # 参数类型: HWND
        ctypes.wintypes.UINT,  # 参数类型: UINT
        ctypes.wintypes.WPARAM,  # 参数类型: WPARAM
        ctypes.wintypes.LPARAM  # 参数类型: LPARAM
    )

    def __init__(self, handler):
        self.handler = handler
        self._hwnd = None
        self._dev_notify_handle = None
        self._stop = False

    def get_win(self):
        """
        获取窗口句柄
        """
        return self._hwnd

    def gen_callback(self):
        def callback(hwnd, msg, wparam, lparam):
            if self.handler(hwnd, msg, wparam, lparam):
                return 0
            else:
                return 1

        return callback

    def init(self, windows_title="Window Title"):
        # 注册设备更改回调函数
        callback_func = self.DeviceChangeCallback(self.gen_callback())
        user32 = ctypes.windll.user32
        user32.RegisterDeviceNotificationW.restype = ctypes.wintypes.HANDLE

        # 创建一个窗口类
        wndclass = win32gui.WNDCLASS()
        wndclass.hInstance = win32gui.GetModuleHandle(None)
        wndclass.lpszClassName = "WindowClass"
        wndclass.lpfnWndProc = callback_func  # 处理窗口消息的回调函数

        # 注册
        win32gui.RegisterClass(wndclass)

        # 创建
        self._hwnd = win32gui.CreateWindowEx(
            win32con.WS_EX_CLIENTEDGE,
            wndclass.lpszClassName,
            "Window Title",
            win32con.WS_OVERLAPPEDWINDOW,
            100,
            100,
            300,
            200,
            None,
            None,
            wndclass.hInstance,
            None
        )

        if not self._hwnd:
            return False, f'Create Windows error: {ctypes.windll.kernel32.GetLastError()}'

        class GUID(ctypes.Structure):
            _fields_ = [
                ("Data1", ctypes.wintypes.DWORD),
                ("Data2", ctypes.wintypes.WORD),
                ("Data3", ctypes.wintypes.WORD),
                ("Data4", ctypes.wintypes.BYTE * 8)
            ]

        # 定义设备接口类别结构体
        class DEV_BROADCAST_DEVICEINTERFACE(ctypes.Structure):
            _fields_ = [
                ("dbcc_size", ctypes.wintypes.DWORD),
                ("dbcc_devicetype", ctypes.wintypes.DWORD),
                ("dbcc_reserved", ctypes.wintypes.DWORD),
                ("dbcc_classguid", GUID),
                ("dbcc_name", ctypes.c_wchar * 1)
            ]

        # 注册全部USB设备监听器
        dev_interface_guid = (
            0xA5DCBF10,
            0x6530,
            0x11D2,
            (ctypes.wintypes.BYTE * 8)(0x90, 0x1F, 0x00, 0xC0, 0x4F, 0xB9, 0x51, 0xED)  # GUID_DEVINTERFACE_USB_DEVICE
        )
        dev_interface = DEV_BROADCAST_DEVICEINTERFACE()
        dev_interface.dbcc_size = ctypes.sizeof(dev_interface)
        dev_interface.dbcc_devicetype = win32con.DBT_DEVTYP_DEVICEINTERFACE
        dev_interface.dbcc_classguid = dev_interface_guid

        self._dev_notify_handle = user32.RegisterDeviceNotificationW(
            ctypes.wintypes.HANDLE(self._hwnd),  # 接收设备更改消息的窗口句柄
            ctypes.byref(dev_interface),  # 设备接口类别
            ctypes.wintypes.DWORD(0x00000000),  # 控制标志
        )

    def start(self):
        # 进入消息循环
        user32 = ctypes.windll.user32
        msg = ctypes.wintypes.MSG()
        while True:
            if self._stop:
                break

            if user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, win32con.PM_REMOVE) != 0:
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageW(ctypes.byref(msg))
            else:
                time.sleep(1)

        # 注销设备更改回调函数
        user32.UnregisterDeviceNotification(self._dev_notify_handle)

    def stop(self):
        """
        关闭消息监听
        """
        self._stop = True
