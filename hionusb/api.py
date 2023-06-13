import os
import sys
import platform
import ctypes

CWD = os.path.dirname(__file__)
DLL = os.path.join(CWD, r'lib\UsbDll.dll')

if sys.platform != 'win32' or platform.architecture()[0] != '32bit':
    # pyhionusb only used for windows + python 32bit
    raise ImportError("pyhionusb is only used for windows platform and python 32bit arch.")

if not os.path.exists(DLL):
    raise ImportError("Not found usbdll.dll, please try to reinstall this module")

try:
    lib = ctypes.WinDLL(DLL, use_errno=True)
except OSError:
    raise ImportError("Invalid usbdll.dll, please try to reinstall this module")


def dll_prototype(method_name, restype, *argtypes):
    """
    Create a named foreign function belonging to dll

    :param method_name: Name of the foreign function
    :param restype: resulting type
    :param argtypes: arguments that represent argument types
    :returns: foreign function of dll library
    """
    # use_errno=True ensures that errno is exposed by ctypes.get_errno()
    func = ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=True)(
        (method_name, lib))

    def exec_func(*args):
        ret = func(*args)
        if ret < 0:
            return False, ctypes.get_errno()
        else:
            return True, ret

    return exec_func


# 初始化，仅调用一次, init_dll()
init_dll = dll_prototype("InitDll", ctypes.c_int)

# 摘机, offhook_ctrl(idx)
offhook_ctrl = dll_prototype("OffHookCtrl", ctypes.c_int, ctypes.c_int)

# 挂机, hangup_ctrl(idx)
hangup_ctrl = dll_prototype("HangUpCtrl", ctypes.c_int, ctypes.c_int)

# 拨号, start_dial(idx, "number")
start_dial = dll_prototype("StartDial", ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# 设置振铃 bell(idx, mode), mode: 0--关闭; 1--打开
bell = dll_prototype("Bell", ctypes.c_int, ctypes.c_byte)

# 绑定窗口， bind_windows(hwnd)
bind_windows = dll_prototype("BindWindow", ctypes.c_int, ctypes.c_void_p)

# 解绑窗口, unbind_windows()
unbind_windows = dll_prototype("UnBindWindow", ctypes.c_int)

# 查询话机状态，query_phone_status(idx), 0 挂机，1摘机
query_phone_status = dll_prototype("QueryPhoneStatus", ctypes.c_int, ctypes.c_int)

# 打开本地录音, set_local_record(idx, rec), rec: false关闭，true打开
set_local_record = dll_prototype("setLocalRecord", ctypes.c_int, ctypes.c_int, ctypes.c_bool)

# 打开通话录音set_talk_record(idx, rec), rec: false关闭，true打开
set_talk_record = dll_prototype("setTalkRecord", ctypes.c_int, ctypes.c_int, ctypes.c_bool)

# 打开通话录音set_leave_record(idx, rec), rec: false关闭，true打开
set_leave_record = dll_prototype("setLeaveRecord", ctypes.c_int, ctypes.c_int, ctypes.c_bool)

# 获取序列号, get_serial_no(idx, number), number 存放序列号
get_serial_no = dll_prototype("GetSerialNo", ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# 设置序列号, set_serial_no(idx, number), number 存放序列号
set_serial_no = dll_prototype("SetSerialNo", ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# 闪断, flash(idx, v), 0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms之间
flash = dll_prototype("Flash", ctypes.c_int, ctypes.c_int, ctypes.c_uint)

# 设置拨号音开关, set_dial_tone(idx, mode) mode: 0--关闭; 1--打开
set_dial_tone = dll_prototype("SetDialTone", ctypes.c_int, ctypes.c_int, ctypes.c_byte)

# 设置自动接听开关, set_auto_answer(idx, mode) mode: 0--关闭; 1--打开
set_auto_answer = dll_prototype("SetAutoAnswer", ctypes.c_int, ctypes.c_int, ctypes.c_byte)

# 设置闪断时间, set_flash_time(idx, v), 0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms之间
set_flash_time = dll_prototype("SetFlashTime", ctypes.c_int, ctypes.c_int, ctypes.c_uint)

# 设置出局码, set_out_code(idx, code),
set_out_code = dll_prototype("SetOutcode", ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# 开始录音, start_record_file(idx, file)
start_record_file = dll_prototype("StartRecordFile", ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

# 停止录音, stop_record_file(idx)
stop_record_file = dll_prototype("StopRecordFile", ctypes.c_int, ctypes.c_int)

# 转播, zhuan_bo(idx, v), ivalue--转拨操作的时间长度,取值为0--100ms,1--180ms,2--300ms,3--600ms,4--1000ms之间
zhuan_bo = dll_prototype("ZhuanBo", ctypes.c_int, ctypes.c_int, ctypes.c_uint)

# 设置呼叫保留, hold(idx, flag), 1:开启保留，0：关闭
hold = dll_prototype("Hold", ctypes.c_int, ctypes.c_int, ctypes.c_bool)

# 设置开启闭音, mute(idx, flag), 1:开启保留，0：关闭
mute = dll_prototype("Mute", ctypes.c_int, ctypes.c_int, ctypes.c_bool)
