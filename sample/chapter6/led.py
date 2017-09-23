# coding: utf-8
# ======== 讓LED閃爍 ========
import RPi.GPIO as GPIO
import time

## 設定值
LED = 24

## 初始化 設定為out模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

## 反覆10次
for i in range(10):
    GPIO.output(LED, 1)	# 讓LED亮燈
    time.sleep(0.5)		# 等待0.5秒
    GPIO.output(LED, 0)	# 讓LED熄燈
    time.sleep(0.5)		# 等待0.5秒

## 結束
GPIO.cleanup()
