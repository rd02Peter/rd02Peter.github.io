# coding: utf-8
# ======== WebIOPi巨集：I2C的READ/WRITE ========
import webiopi
import smbus
bus = smbus.SMBus(1)

## 向I2C連接埠傳送資料（1位元組）
@webiopi.macro
def i2c_write(addr, reg, data):
    bus.write_byte_data(int(addr) ,int(reg), int(data))
    return "1"

## 向I2C連接埠傳送資料（連續資料）
@webiopi.macro
def i2c_bwrite(addr, reg, *datas):
    idatas = [int(n) for n in datas]
    bus.write_i2c_block_data(int(addr), int(reg), idatas)
    return "1"

## 從I2C連接埠讀取資料
@webiopi.macro
def i2c_read(addr, reg):
    data = bus.read_byte_data(int(addr), int(reg))
    return "%d" % data
