#!/usr/bin/env python
# coding: utf-8
# ======== 讓連接在GPIO連接埠上的喇叭發出聲音 ========
import RPi.GPIO as GPIO
import time
import sys
import os.path

## 設定值
BUZZER = 27

## 初始化 設定為OUT模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

## 根據給的參數來改變發出的聲音
if len(sys.argv) > 1:
    p = GPIO.PWM(BUZZER, 1)     ## 以1Hz (暫時)設定PWM

    if sys.argv[1] == "alert":     # 警報模式
        p.start(50)
        for i in range(10):
            for freq in range(1000,99,-100):
                p.ChangeFrequency(freq)
                time.sleep(0.03)
        p.stop()
    elif sys.argv[1] == "beep1":   # 短嗶聲
        p.start(50)
        p.ChangeFrequency(1000)
        time.sleep(0.05)
        p.stop()
    elif sys.argv[1] == "beep2":   # 長嗶聲
        p.start(50)
        p.ChangeFrequency(1000)
        time.sleep(0.5)
        p.stop()

## 當沒有給予參數時顯示使用方法
else:
    myname = os.path.basename(sys.argv[0])
    print "Usage: "+ myname +" [alert|beep1|beep2]"

## 結束
GPIO.cleanup()
