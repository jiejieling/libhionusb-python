class Constant(object):
    """
    常量类，映射DLL中define
    """

    # 录音类型
    RECORD_LOCAL = 0
    RECORD_TALK = 1
    RECORD_LY = 2

    # 设备标识
    WM_DEVICE = 7

    # 设备事件
    # USB设备插入/拔出
    WM_DEVICECHANGE = 0x0219
    # 设备插入
    WM_DEVICEADD = 0x8000
    # 设备拔出
    WM_DEVICEREMOVE = 0x8004

    # windows 用户自定义事件
    WM_USER = 0x0400
    # 设备连接
    WM_DEVICECONNECT = WM_USER + 701
    # 设备断开
    WM_DEVICEDISCONNECT = WM_USER + 702
    # 摘机
    WM_OFFHOOK = WM_USER + 703
    # 挂机
    WM_ONHOOK = WM_USER + 704
    # 来电显示
    WM_CALLERID = WM_USER + 705
    # 响铃
    WM_RING = WM_USER + 706
    # 拨号
    WM_KEY = WM_USER + 707
    # 停止留言
    WM_STOPLY = WM_USER + 708
    # 静音
    WM_MUTE = WM_USER + 709
