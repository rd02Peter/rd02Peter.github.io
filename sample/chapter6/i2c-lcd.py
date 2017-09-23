#!/usr/bin/env python
# coding: utf-8
# ======== 在I2C連接的字元LCD SB1602BW上顯示文字 ========
import smbus
import time
import sys
import unicodedata
from jcconv import *

## 設定値
I2C_ADDR = 0x3E   # 裝置位址
COLUMN = 16       # LCD的位數
CONTRAST = 8      # LCD的對比度（0~15）

## 函式：LCD的初始化
def lcd_init(bus,contrast):
    fcnt = 0x70 | (contrast & 0x0F)
    bus.write_i2c_block_data(I2C_ADDR, 0x00, [0x38,0x39,0x14,fcnt
    ,0x5f,0x6a])
    time.sleep(0.3)
    bus.write_i2c_block_data(I2C_ADDR, 0x00, [0x0c,0x01])
    time.sleep(0.3)
    bus.write_byte_data(I2C_ADDR, 0x00, 0x06)
    time.sleep(0.3)

## 函式：製作要送往LCD的資料
def lcd_make_data(text):
    maxlen = COLUMN * 2
    data = [0x20] * maxlen
    ## 全形 → 半形轉換（平假名文字轉為半形片假名）
    unistr = unicode(text,'utf-8')
    uninor = unicodedata.normalize('NFKC',unistr)
    unihan = kata2half( hira2kata(uninor) )
    ## 無法轉換成功的文字個別進行轉換（常用到的）
    unihan = unihan.replace(u'ー',u'ｰ')
    ## 轉換為SJIS並每位元組逐一放入data
    sjis = unihan.encode('shift_jis','replace')
    for i in range(len(sjis)):
        if i >= maxlen: break
        data[i] = ord(sjis[i])
    return data

## 函式：傳送文字到LCD
def lcd_send_data(bus,data):
    maxlen = COLUMN * 2
    ## 第一行
    bus.write_byte_data(I2C_ADDR, 0x00, 0x80)
    bus.write_i2c_block_data(I2C_ADDR, 0x40, data[0:COLUMN])
    ## 第二行
    bus.write_byte_data(I2C_ADDR, 0x00, 0xc0)
    bus.write_i2c_block_data(I2C_ADDR, 0x40, data[COLUMN:maxlen])

## 主函式
if len(sys.argv) > 1:
    bus = smbus.SMBus(1)
    lcd_init(bus,CONTRAST)              # 初始化LCD
    data = lcd_make_data(sys.argv[1])   # 製作要傳送的資料
    lcd_send_data(bus,data)            # 將資料傳送到LCD
else:
    print "Usage: "+sys.argv[0]+" \"message\""
