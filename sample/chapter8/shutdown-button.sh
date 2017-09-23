#!/bin/sh
PORT=22      # 使用的GPIO連接埠
PUSHTIME=5  # 到執行關機前的秒數

## 設定GPIO為in模式
gpio -g mode $PORT in
gpio -g mode $PORT down

## 控制ACT LED的 subroutine
set_led_mode () {
  echo $1 > /sys/class/leds/led0/trigger
}
set_led_value () {
  echo $1 > /sys/class/leds/led0/brightness
}

## 等待直到壓住了5秒
cnt=0
while [ $cnt -lt $PUSHTIME ] ; do
  if [ `gpio -g read $PORT` -eq "1" ] ; then
    cnt=`expr $cnt + 1`
    [ $cnt -eq 1 ] && set_led_mode heartbeat
  else
    [ $cnt -gt 0 ] && set_led_mode mmc0
    cnt=0
  fi
  sleep 1
done

## 用 ACT LED 來通知關機
set_led_mode none
set_led_value 1
sleep 2
set_led_value 0
set_led_mode mmc0

## 執行關機
shutdown -h now
