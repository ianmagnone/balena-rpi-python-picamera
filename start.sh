modprobe v4l2_common && python timelapse.py &
cd /usr/src/app/
python -m SimpleHTTPServer 80
