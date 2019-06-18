# 特别感谢
特别感谢society765在本项目中给与的启发，本项目在其[工作基础](https://github.com/society765/yys-auto-yuhun)上修改完成。

同时感谢sup817ch的图像识别思路，本项目game_ctl模块基于其[工作基础](https://github.com/sup817ch/AutoOnmyoji)。

# 使用说明

环境：python 3.7, 32 bit；yys PC端；win 10系统。

1、该脚本可以用于阴阳师御魂、业原火、御灵等单刷或双人组队，适用于PC端；

2、窗口现在可以完全后台，可以被遮挡，但是不能最小化，不能最小化，不能最小化；

3、玩家需要提前准备好战斗阵容，阵容需要锁定；

4、在战斗过程中，该脚本会自动拒绝所有悬赏封印的邀请；

5、本人只测试过魂十，其他请自测；

6、如果60s程序没有任何操作，视为体力用光，为了保护加成，自动关闭YYS；

7、该脚本仅使用了画面找色，鼠标后台点击的函数，完全模拟人类玩家行为，没有使用任何内存读写函数。在敏感位置添加了均匀分布的随机时间漂移，和随机坐标漂移；

# 目前进展
目前已经完成了单刷、单人司机和单人打手的工作，其他工作待完成。

# 注意事项
1、点怪目前不可用，因为大蛇模型太大，挡住了点怪图标；

2、当使用 Windows 7 系统时，需要调整系统的画面设置：把主题调为最丑最挫的那个。在 Windows 10 系统中，不需要调整系统画面设置。

3、当使用高分辨率屏幕时，在阴阳师客户端程序兼容性选项里，不要勾选"替代高DPI缩放行为"，这个选项应该是默认不勾选的。

# 使用方法

第一步，准备yys

1、如果单刷，则进入御魂/业原火/御灵，备好式神，锁定阵容即可；

2、如果单人司机，则进入组队页面，锁定阵容；

3、如果单人打手，则进入组队页面，锁定阵容。

第二步，开打

1、双击运行run.bat，会弹出设置界面，点击确认后再根据个人情况选择参数；

2、如果不想安装环境，可以访问下载最新已[编译](https://github.com/AcademicDog/onmyoji_bot/releases)版本。

# 下一步计划
1、更新双开部分；

2、完善点怪操作。

# 更新说明
20190619--抛弃dll插件，用win32api，同时用图像识别替代简单找色

# 协议 (License)

该源代码使用了 [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) 开源协议。

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.