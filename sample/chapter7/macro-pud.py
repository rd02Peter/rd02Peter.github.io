# coding: utf-8
# ======== WebIOPi巨集：設定上拉、下拉 ========
import webiopi
GPIO = webiopi.GPIO

## 將GPIO連接埠設定為IN模式、並進行上拉/下拉的設定
@webiopi.macro
def set_gpio_pulldown(io, mode):
    pud = GPIO.PUD_OFF
    if mode.lower() == 'down':
        pud = GPIO.PUD_DOWN
    elif mode.lower() == 'up':
        pud = GPIO.PUD_UP
    GPIO.setFunction(int(io), GPIO.IN, pud)
