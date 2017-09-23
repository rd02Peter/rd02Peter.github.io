#!/bin/sh
#
# 當按下接在 GPIO18,23,24,25 的按鈕，會將個按鈕對應
# 到的訊息推文。推文狀態以開發板上的LED通知。
#


## 各個按鈕分配到的GPIO連接埠與推文訊息的設定
PORT1=18
MESSAGE1="今天是營業日"

PORT2=23
MESSAGE2="麵包出爐囉！"

PORT3=24
MESSAGE3="現在剛好賣完了"

PORT4=25
MESSAGE4="今日已結束營業"

## 推文的函式
tweet() {
  ## 讓開發板上的LED閃爍
  sudo su -c "echo heartbeat > /sys/class/leds/led0/trigger"

  ## 執行推文
  tweettext="$1 `date +%H:%M`"
  echo -n "正在推文「"$tweettext"」..."
  ttytter -ssl -status="$tweettext" >/dev/null
  echo "完成！"

  ## 讓開發板上的LED亮燈5秒（等待五秒）
  sudo su -c "echo none > /sys/class/leds/led0/trigger"
  sudo su -c "echo 1 > /sys/class/leds/led0/brightness"
  sleep 5

  ## 將開發板上的LED設回mmc0模式
  sudo su -c "echo mmc0 > /sys/class/leds/led0/trigger"
  echo "請按下推文按鈕 1～4"
}

## 將各個GPIO連接埠設定為in模式、下拉
for port in $PORT1 $PORT2 $PORT3 $PORT4 ; do
  gpio -g mode $port in
  gpio -g mode $port down
done

## 主要迴圈
echo "請按下推文按鈕 1～4"
while true ; do

  ## 當按鈕 1 被按下
  if [ `gpio -g read $PORT1` -eq 1 ] ; then
    tweet "$MESSAGE1"
  fi

  ## 當按鈕 2 被按下
  if [ `gpio -g read $PORT2` -eq 1 ] ; then
    tweet "$MESSAGE2"
  fi

  ## 當按鈕 3 被按下
  if [ `gpio -g read $PORT3` -eq 1 ] ; then
    tweet "$MESSAGE3"
  fi

  ## 當按鈕 4 被按下
  if [ `gpio -g read $PORT4` -eq 1 ] ; then
    tweet "$MESSAGE4"
  fi

  ## 等待 0.1 秒後反覆執行
  sleep 0.1
done
