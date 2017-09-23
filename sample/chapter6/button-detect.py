# coding: utf-8
# ======== 偵測按鈕被壓下 ========
import RPi.GPIO as GPIO
import time

## 設定值
BUTTON = 25

## 初始化 IN模式、設定為下拉
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


## 函式：當按鈕被壓下時進行的處理
def button_pushed(channel):
    print "Pushed!!"

## 事件的定義
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=button_pushed, bouncetime=200)

## 主迴圈
try:
    while True:    # 不斷反覆
        print "Please push the button."
        time.sleep(1)
except KeyboardInterrupt:    # 當Ctrl + C被按下
    print "STOP"

## 結束
GPIO.remove_event_detect(BUTTON)    # 刪除定義的事件
GPIO.cleanup()
