import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wye/Projects/robotics-onboarding-notes/day-1/ros2_ws/install/day1_topics'
