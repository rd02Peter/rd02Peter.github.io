# coding: utf-8
# ======== 以PWM來發出doremi音階 ========
import RPi.GPIO as GPIO
import time

## 設定値
BUZZER = 27
TONES = { 'DO':262, 'RE':294, 'MI':330, 'FA':349, 'SO':392,
'RA':440, 'SI':494, 'DO2':523 }
MELODY = [ 'DO','RE','MI','FA','SO','RA','SI','DO2' ]

## 初始化 設定為OUT模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

## 以頻率1Hz（暫用）來設定PWM
p = GPIO.PWM(BUZZER, 1)

## 依序發出音階的聲音
p.start(50)                  # PWM開始
for onkai in MELODY:          # 依序前進一個音階
    freq = TONES[onkai]
    p.ChangeFrequency(freq)       # 變更頻率
    time.sleep(0.5)
p.stop()                       # PWM停止

## 休止符
time.sleep(0.5)

## 倒序發出音階的聲音
p.start(50)                  # PWM開始
for onkai in reversed(MELODY):   # 倒序前進一個音階
    freq = TONES[onkai]
    p.ChangeFrequency(freq)       # 變更頻率
    time.sleep(0.5)
p.stop()                     # PWM停止

## 結束
GPIO.cleanup()
