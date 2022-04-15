#!/usr/bin/env sh
# generated from catkin/cmake/template/local_setup.sh.in

# since this file is sourced either use the provided _CATKIN_SETUP_DIR
# or fall back to the destination set at configure time
<<<<<<< HEAD
: ${_CATKIN_SETUP_DIR:=/home/le/aev/radarScanQT_ROS/devel}
=======
: ${_CATKIN_SETUP_DIR:=/home/le/catkin_ws/devel}
>>>>>>> 9ceb1f80b4ec1fc1f1dee2e47f5094883812ff84
CATKIN_SETUP_UTIL_ARGS="--extend --local"
. "$_CATKIN_SETUP_DIR/setup.sh"
unset CATKIN_SETUP_UTIL_ARGS
