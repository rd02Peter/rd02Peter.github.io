#!/bin/sh
PORT=25                     # 紅外線人體感測器的GPIO連接埠號
SAVEDIR="$HOME/Pictures"   # 照片檔案的儲存目錄

## GPIO連接埠的設定
gpio -g mode $PORT in

## 主要迴圈
mkdir -p $SAVEDIR
buzzer beep2
echo "啟動監視系統"
while true ; do

  ## 等待感測器的動作
  if [ `gpio -g read $PORT` -eq 1  ] ; then
    echo "*** ALERT *** 發生入侵異常狀況"

    ## 拍攝
    filename=`date +"%Y%m%d-%H%M%S"`.jpg
    raspistill -o $SAVEDIR/$filename -t 2000 -w 1024 -h 768
    echo "照片儲存完成"

    ## 發出警報聲響驚嚇小偷
    buzzer alert &

    ## 發出警報後等待10秒
    sleep 10
    buzzer beep1
    echo "繼續進行監視"
  fi

  ## 等待 0.5 秒後重複動作
  sleep 0.5

done
