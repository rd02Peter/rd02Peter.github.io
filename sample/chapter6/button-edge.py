# coding: utf-8
# ======== 等待按鈕被壓下 ========
import RPi.GPIO as GPIO
import time

## 設定值
BUTTON = 25
TIMEOUT = 10000    # 逾時設定 (ms)

## 初始化 IN模式、設定為下拉
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## 等到按鈕被壓下
channel = GPIO.wait_for_edge(BUTTON, GPIO.RISING, timeout=TIMEOUT)
if channel:
    print "Pushed!!"    # 按鈕被壓下時
else:
    print "Timeout"    # 逾時

## 結束
GPIO.cleanup()
