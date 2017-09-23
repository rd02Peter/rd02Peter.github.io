# coding: utf-8
# ======== 讓接在GPIO連接埠的喇叭發出聲音 ========
import RPi.GPIO as GPIO
import time

## 設定值
BUZZER = 27
TONE_HIGH = 1000   # 高音 1000Hz
TONE_LOW  = 500   # 低音 500Hz

## 初始化 設定為OUT模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

## 以頻率1000Hz來設定PWM
p = GPIO.PWM(BUZZER, TONE_HIGH)

## PWM開始 (初始值為50%)
p.start(50)

## 反覆5次
for i in range(5):
    ## 發出高音
    p.ChangeFrequency(TONE_HIGH)    # 變更頻率
    time.sleep(0.5)

    ## 發出低音
    p.ChangeFrequency(TONE_LOW)    # 變更頻率
    time.sleep(0.5)

## PWM停止
p.stop()

## 結束
GPIO.cleanup()
