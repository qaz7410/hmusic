from selenium import webdriver
import time
from pykeyboard import PyKeyboard
# import speech
import tkinter.messagebox

# tkinter.Tk().geometry('0x0+999999+0')
# def music():

k = PyKeyboard()    #调用PyKeyboard

# speech.say('请输入你想听的音乐')
name=input('请输入你要听的音乐\n')

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=')
bro.find_element_by_xpath('/html/body/div[3]/div/div[1]/input').send_keys(name)
time.sleep(1)
k.tap_key(k.enter_key)  #模拟键盘按Enter
time.sleep(0.5)
bro.find_element_by_class_name('song_name').click()
time.sleep(0.5)



