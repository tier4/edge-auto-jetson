#/bin/bash

# start camera trigger 
echo -e "\e[36m--- [PREPARATION] camera trigger start ---\e[0m"
source install/setup.bash
RMW_IMPLEMENTATION=
ros2 launch sensor_trigger sensor_trigger.launch.xml frame_rate:=30.0 gpio:=51 & trigger_video0=$!
ros2 launch sensor_trigger sensor_trigger.launch.xml frame_rate:=30.0 gpio:=52 & trigger_video1=$!
sleep 5

# tier4 C1 camera(/dev/video0) streaming test
echo -e "\e[36m--- [TEST 1] tier4 C1 camera(/dev/video0) streaming test ---\e[0m"
timeout 30s v4l2-ctl --stream-mmap --stream-count=300 -d /dev/video0
test1_result=$?
if [ $test1_result = 0 ]; then 
    echo -e "\e[32m[SUCCESS] /dev/video0 streaming success.\e[0m"
elif [ $test1_result = 124 ]; then
    echo -e "\e[31m[FAILED] /dev/video0 streaming failed. [exit code ${test1_result} ... timeout]\e[0m"
else
    echo -e "\e[31m[FAILED] /dev/video0 streaming failed. [exit code ${test1_result} ... unknown]\e[0m"
fi

# tier4 C1 camera(/dev/video1) streaming test
echo -e "\e[36m--- [TEST 2] tier4 C1 camera(/dev/video1) streaming test ---\e[0m"
timeout 30s v4l2-ctl --stream-mmap --stream-count=300 -d /dev/video1
test2_result=$?
if [ $test2_result = 0 ]; then 
    echo -e "\e[32m[SUCCESS] /dev/video1 streaming success.\e[0m"
elif [ $test2_result = 124 ]; then
    echo -e "\e[31m[FAILED] /dev/video1 streaming failed. [exit code ${test2_result} ... timeout]\e[0m"
else
    echo -e "\e[31m[FAILED] /dev/video1 streaming failed. [exit code ${test2_result} ... unknown]\e[0m"
fi

# 
kill -n 9 $trigger_video0
kill -n 9 $trigger_video1

# show result
if [ $test1_result = 0 ] && [ $test1_result = 0 ]; then
    echo -e "\e[32m[RESULT] Success.\e[0m"
else
    echo -e "\e[31m[RESULT] failed.\e[0m"
fi