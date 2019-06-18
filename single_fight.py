import time
import fighter
import game_ctl
import utilities


class SingleFight(fighter.Fighter):
    '''单人御魂战斗，参数done, emyc'''

    def __init__(self, done, emyc):
        # 初始化
        fighter.Fighter.__init__(self, emyc)

    def start(self):
        '''单人战斗主循环'''
        mood1 = utilities.Mood()
        mood2 = utilities.Mood()
        mood3 = utilities.Mood()
        while True:
            # 在御魂主选单，点击“挑战”按钮, 需要使用“阵容锁定”！
            self.yys.wait_game_img('img\\TIAO-ZHAN.png')
            mood1.moodsleep()
            self.yys.mouse_click_bg((790, 418), (790 + 113, 418 + 51))
            self.log.writeinfo('Already clicked TIAO-ZHAN')

            # 检测是否进入战斗
            self.check_battle()

            # 在战斗中，自动点怪
            self.click_monster()

            # 检测是否打完
            self.check_end()
            mood2.moodsleep()

            # 在战斗结算页面
            start_time = time.time()
            while time.time() - start_time <= 10:
                self.yys.mouse_click_bg(utilities.secondposition())
                if(self.yys.wait_game_img('img\\TIAO-ZHAN.png', mood3.get1mood()/1000, False)):
                    break
            self.log.writeinfo("Back to YUHUN level selection")
