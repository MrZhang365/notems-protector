'''
嘿，这是个note.ms网络剪贴板保护装置，它的原理就是不断地控制浏览器给服务器发送请求来实现目标网络剪贴板的内容始终不变。


开发团队：小张软件ZhangSoft ( 官方网站：https://www.zhangsoft.cf/ GitHub：https://github.com/ZhangSoftTeam )
鸣谢用户：MaggieLOL ( 个人博客：https://www.thz.cool GitHub：https://github.com/MaggieLOL )
'''

from selenium import webdriver
from time import sleep as zzz

targetName = 'target'    #改成目标剪贴板的名称

driver = webdriver.Edge('请在此处放置Edge浏览器的驱动的路径')    #可以改成其他浏览器
driver.get('https://note.ms/'+targetName)
c=driver.find_element('xpath',"/html/body/div[1]/div[1]/div/div/textarea")

print('note.ms保护装置即将在5秒后启动！目标剪贴板名称：'+targetName)
zzz(5)
print('已启动！')

while True:
    zzz(0.5)
    c.send_keys('a')
    zzz(0.5)
    c.send_keys('\b')