# coding: utf-8
# ======== WebIOPi 巨集：用攝影機模組拍攝 ========
import webiopi
import os

## 儲存檔案的目錄
SAVEDIR = '/home/pi/webiopi/test'

## 執行 raspistill 指令
@webiopi.macro
def camera(fileno):
    ## 決定檔案名稱
    safe_no = int(fileno)
    path = SAVEDIR + '/camera_' + str(safe_no) + '.jpg'
    ## 拍照，以使用者 pi 執行指令
    command = 'raspistill -o '+ path +' -t 1000 -w 640 -h 480'
    os.system('su pi -c \"'+ command + '\"')
    ## 將磁碟快取寫入
    os.system('sync')
