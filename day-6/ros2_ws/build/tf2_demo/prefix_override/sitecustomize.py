import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wye/Projects/robotics-onboarding-notes/day-6/ros2_ws/install/tf2_demo'
