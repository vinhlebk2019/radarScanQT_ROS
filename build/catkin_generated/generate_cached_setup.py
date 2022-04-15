# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
<<<<<<< HEAD
    for workspace in '/home/le/aev/aev_ws/devel;/home/le/catkin_ws/devel;/opt/ros/melodic'.split(';'):
=======
    for workspace in '/home/le/catkin_ws/devel;/opt/ros/melodic'.split(';'):
>>>>>>> 9ceb1f80b4ec1fc1f1dee2e47f5094883812ff84
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

<<<<<<< HEAD
code = generate_environment_script('/home/le/aev/radarScanQT_ROS/devel/env.sh')

output_filename = '/home/le/aev/radarScanQT_ROS/build/catkin_generated/setup_cached.sh'
=======
code = generate_environment_script('/home/le/catkin_ws/devel/env.sh')

output_filename = '/home/le/catkin_ws/build/catkin_generated/setup_cached.sh'
>>>>>>> 9ceb1f80b4ec1fc1f1dee2e47f5094883812ff84
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
