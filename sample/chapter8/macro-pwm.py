# coding: utf-8
# ======== WebIOPi巨集：PWM的設定 ========
import webiopi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
p = {}    # PWM的實例變數

## 設定GPIO連接埠為PWM模式
@webiopi.macro
def pwm_set_function(io):
    io = int(io)
    GPIO.setup(io, GPIO.OUT, initial=GPIO.LOW)
    p[io] = GPIO.PWM(int(io), 1000)  #1000Hz

## PWM開始
@webiopi.macro
def pwm_start(io, freq, duty):
    io = int(io);
    p[io].ChangeFrequency(int(freq))
    p[io].start(int(duty))

## PWM頻率的變更
@webiopi.macro
def pwm_freq(io, freq):
    io = int(io)
    p[io].ChangeFrequency(int(freq))

## PWM Duty Cycle的變更
@webiopi.macro
def pwm_duty(io, duty):
    io = int(io)
    p[io].ChangeDutyCycle(int(duty))

## PWM停止
@webiopi.macro
def pwm_stop(io):
    io = int(io)
    p[io].stop()
