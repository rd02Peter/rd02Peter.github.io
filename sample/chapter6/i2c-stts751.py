# coding: utf-8
# ======== 從以I2C連接的溫度感測器STTS751取得量測值 ========
import smbus

## 設定値
I2C_ADDR = 0x39    # 裝置位址

## 初期設定
bus = smbus.SMBus(1)
bus.write_byte_data(I2C_ADDR, 0x03, 0x0c)   # 設定解析度=12bit

## 測定
raw1 = bus.read_byte_data(I2C_ADDR, 0x00)    # 取得高位bit
raw2 = bus.read_byte_data(I2C_ADDR, 0x02)    # 取得低位bit

## 計算
t = (raw1 & 0x7F) << 4 | (raw2 & 0xF0) >> 4
if raw1 & 0x80: t = - ((t ^ 0x07FF) + 1)
temp = 1.0 / 2**4 * t

## 顯示結果
print "Temp = %.4f" % temp
