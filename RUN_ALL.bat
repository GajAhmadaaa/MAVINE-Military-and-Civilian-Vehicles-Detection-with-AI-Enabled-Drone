@echo off

echo [M A V I N E]
echo [Military and Civilian Vehicles Detection with AI-Enabled Drone]
echo Starting MAVINE...

python detect.py --weights best.pt --data data.yaml --device 0 --source rtmp://localhost/live

flask run

echo.
echo Operation completed..
pause