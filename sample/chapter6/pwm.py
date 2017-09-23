# coding: utf-8
# ======== 以PWM讓LED緩和地閃爍 ========
import RPi.GPIO as GPIO
import time

## 設定値
LED = 24

## 初始化 設定為out模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

## 設定PWM為頻率1000Hz
p = GPIO.PWM(LED, 1000);  #1000Hz

## PWM開始 (初始值為0%)
p.start(0)

## 反覆3次
for i in range(3):
    ## 淡入
    for rat in range(0,101,10):    # 0~100%以10%為單位增加
        p.ChangeDutyCycle(rat);    # 變更Duty Cycle
        time.sleep(0.5)
    ## 淡出
    for rat in range(100,-1,-10):   # 100~0%以10%為單位減少
        p.ChangeDutyCycle(rat);    # 變更Duty Cycle
        time.sleep(0.5)

## PWM停止
p.stop()

## 結束
GPIO.cleanup()
