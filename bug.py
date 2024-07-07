'''
嘿，这是个note.ms网络剪贴板保护装置，它的原理就是不断地控制浏览器给服务器发送请求来实现目标网络剪贴板的内容始终不变。


开发团队：小张软件ZhangSoft ( 官方网站：https://www.zhangsoft.cf/ GitHub：https://github.com/ZhangSoftTeam )
修改；灯确吉L（offical site: dqjl.eu.org , dqj.lol contact me at light689@163.com or bilibili 灯确吉L Github: https://github.com/lightworld689）
鸣谢用户：MaggieLOL ( 个人博客：https://www.thz.cool GitHub：https://github.com/MaggieLOL )
'''
from selenium import webdriver
from time import sleep as zzz
import txt.py

targetName = 'target' # 保护目标
force_editing = False # 不要知道这是什么……

url = f'https://note.ms/{targetName}'
if force_editing:
    url += '?force-editing=true'

driver = webdriver.Edge('请在此处放置Edge浏览器的驱动的路径')
driver.get(url)

c = driver.find_element('xpath', "/html/body/div[1]/div[1]/div/div/textarea")

print(txt.overlay_text)

print(f'note.ms保护装置即将在5秒后启动！目标剪贴板名称：{targetName} 0号编辑：{force_editing}')
zzz(5)
print('已启动！')

while True:
    zzz(0.5)
    c.send_keys('a')
    zzz(0.5)
    c.send_keys('\b')
