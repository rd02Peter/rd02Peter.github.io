#!/bin/sh
ID=test       # 使用者名稱
PW=1234       # 密碼
PORT=8080     # 連接埠
SIZE=320x240  # 影像的大小（寬 x 高）
FPS=10        # 畫面更新率

export LD_LIBRARY_PATH=/usr/local/lib
mjpg_streamer \
  -i "input_uvc.so -f $FPS -r $SIZE -d /dev/video0 -y" \
  -o "output_http.so -w /usr/local/www -p $PORT -c $ID:$PW"
