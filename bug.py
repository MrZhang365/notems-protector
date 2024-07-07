'''
嘿，这是个note.ms网络剪贴板保护装置，它的原理就是不断地控制浏览器给服务器发送请求来实现目标网络剪贴板的内容始终不变。


开发团队：小张软件ZhangSoft ( 官方网站：https://www.zhangsoft.cf/ GitHub：https://github.com/ZhangSoftTeam )
修改；灯确吉L（offical site: dqjl.eu.org , lr689.eu.org contact me at light689@163.com or bilibili 灯确吉L Github: https://github.com/lightworld689）
鸣谢用户：MaggieLOL ( 个人博客：https://www.thz.cool GitHub：https://github.com/MaggieLOL )
'''
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep as zzz
import txt

targetName = 'target'
force_editing = True
driver_path = r'C:\msedgedriver.exe'

url = f'https://note.ms/{targetName}'
if force_editing:
    url += '?force-editing=true'

service = Service(driver_path)
driver = webdriver.Edge(service=service)
driver.get(url)

c = driver.find_element('xpath', "/html/body/div[1]/div[1]/div/div/textarea")

print(txt.overlay_text)

print(f'note.ms保护装置即将在5秒后启动！目标剪贴板名称：{targetName}')
zzz(5)
print('已启动！')

while True:
    zzz(0.5)
    c.send_keys(txt.overlay_text)
    zzz(0.5)
    c.clear()

