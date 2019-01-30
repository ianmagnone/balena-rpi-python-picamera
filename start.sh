modprobe v4l2_common && python timelapse.py &
cd /data
python -m SimpleHTTPServer 80
