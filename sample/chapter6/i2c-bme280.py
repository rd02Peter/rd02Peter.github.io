# coding: utf-8
# ======== 從溫濕度壓力感測器模組BME280取得量測值 ========
import Adafruit_BME280 as BME280

## 設定値
I2C_ADDR = 0x76   # 裝置位址

## 測量
sensor = BME280.BME280(address=I2C_ADDR,
mode=BME280.BME280_OSAMPLE_8)

##  取得資料
data_t = sensor.read_temperature()
data_p = sensor.read_pressure() / 100
data_h = sensor.read_humidity()

## 顯示結果
print 'Temp     = %.2f deg C' % data_t
print 'Humidity = %.2f %%' % data_h
print 'Pressure = %.2f hPa' % data_p
