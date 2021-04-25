from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from lxml import etree
import time,easygui

def music(bro,name):
    bro.get('https://music.163.com/')
    time.sleep(0.1)
    bro.find_element_by_id('srch').send_keys(name)
    bro.find_element_by_id('srch').send_keys(Keys.ENTER)
    time.sleep(0.5)
    bro.switch_to.frame('contentFrame')
    time.sleep(0.5)
    bro.find_element_by_class_name('ply').click()  #点击播放歌曲
    time.sleep(0.5)
    bro.find_element_by_class_name('s-fc7').click()   #跳转到歌词页面进而爬取歌词
    # bro.find_element_by_class_name('u-btn2').click()    #点击播放歌曲，跟14行二选一，建议使用14行防止跳转歌词页面失败也播放不了歌曲

def get_music_data():
    htmls = bro.page_source
    html = etree.HTML(htmls)
    h = html.xpath('//*[@id="lyric-content"]')
    h1 = html.xpath('//*[@id="flag_more"]')
    title = html.xpath('/html/head/title/text()')
    title = "".join(title)

    for i in h:
        # print("\n".join(i.xpath('./text()')))
        with open (title+'.txt','a',encoding='utf-8') as f:
            f.write("\n".join(i.xpath('./text()')))

    for i in h1:
        # print("\n".join(i.xpath('./text()')))
        with open (title+'.txt','a',encoding='utf-8') as f:
            f.write("\n".join(i.xpath('./text()')))

    print('歌词以下载完成并保存在：' + title + '.txt')

if __name__ == '__main__':
    name = easygui.enterbox('请输入歌曲名称','欢迎使用本软件')
    print('您选择的歌曲是:'+name)
    if name != None:
        op = easygui.buttonbox(
            msg='请做出如下选择',
            title='欢迎使用本软件',
            choices=['只听音乐','边听音乐边下载歌词','退出']
        )

        if op == None or op == '退出':
            print('欢迎使用本软件')

        elif op == '只听音乐':
            bro = webdriver.Chrome(executable_path='./chromedriver.exe')
            music(bro,name)

        elif op == '边听音乐边下载歌词':
            bro = webdriver.Chrome(executable_path=r'D:\py文件\chromedriver.exe')
            music(bro,name)
            get_music_data()
















