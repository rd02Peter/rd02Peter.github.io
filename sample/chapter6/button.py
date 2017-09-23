# coding: utf-8
# ======== 取得按鈕的狀態 ========
import RPi.GPIO as GPIO
import time

## 設定值
BUTTON = 25

## 初始化 IN模式、設定為下拉
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## 重複20次
for i in range(20):
    btn = GPIO.input(BUTTON)    # 取得按鈕的狀態
    print "GPIO%d = %d" % (BUTTON, btn)    # 顯示
    time.sleep(0.5)    # 等待0.5秒

## 結束
GPIO.cleanup()
