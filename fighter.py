import threading
import win32com.client

import game_ctl
import utilities
import logsystem


class Fighter:

    def __init__(self, emyc=0):
        # 初始参数
        self.emyc = emyc

        # 启动日志
        self.log = logsystem.WriteLog()

        # 绑定窗口
        self.yys = game_ctl.GameControl(u'阴阳师-网易游戏')
        self.log.writeinfo('registration successful')

        # 激活窗口
        self.yys.activate_window()
        self.log.writeinfo('Activation successful')
        utilities.mysleep(500)

    def check_battle(self):
        # 检测是否进入战斗
        self.yys.wait_game_img('img\\ZI-DONG.png')
        self.log.writeinfo('Already in battle')

    def check_end(self):
        # 检测是否打完
        self.yys.wait_game_img('img\\JIE-SU.png')
        self.log.writeinfo("Battle finished")

    def click_monster(self):
        # 点击怪物
        pass
