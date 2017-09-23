#!/bin/bash
RTMP_URL=rtmp://x.xxxxxxxx.fme.ustream.tv/ustreamVideo/xxxxxxxx
STREAM_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WIDTH=1024   #影片的大小（寬）
HEIGHT=768   #影片的大小（高）
FPS=25       #畫面更新率
PREVIEW=10,40,320,240   #預覽（位置 x, y, 大小 w, h）

raspivid -t 0 \
  -e -p $PREVIEW -op 255 \
  -w $WIDTH -h $HEIGHT -fps $FPS \
  -o - | \
avconv -re \
  -f h264 -i - -an \
  -f flv $RTMP_URL/$STREAM_KEY
