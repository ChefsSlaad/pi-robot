#! /bin/bash

PI_CAM_DIR="/home/pi/projects/RPi_Cam_Web_Interface"
PI_WEB_DIR="/home/pi/projects/pi-robot/pi-robot_web_interface"

action="$1"

if pgrep "web.py" > /dev/null  
then
    STATUS="active"
else
    STATUS="stopped"
fi

# if action not supplied at the command prompt display usage message and exit
[ $# -eq 0 ] && { echo "Usage: $0 start|stop|status"; exit 0; }
	
# start web.py and exit script
if [ $1 = "start" ];then  
    if [ $STATUS = "active" ];then
        echo "web_interface allready active"
        exit 0
    else
        echo "starting web interface"
        $PI_CAM_DIR/start.sh 
        $PI_WEB_DIR/web.py & > /dev/null 
        exit 0
    fi
#stop web.py and exit script
elif [ $1 =  "stop" ];then
    if [ $STATUS = "stopped" ];then
        echo "web interface not active" 
        exit 0
    else 
        echo "stopping we interface"
        pkill web.py
        $PI_CAM_DIR/stop.sh 
        exit 0
    fi
#status web.py and exit script
elif [ $1 = "status" ] ; then
    echo "web interface $STATUS"
    exit 0 
fi

exit 1
