# DAY 1

## Goal

- Understand the core ROS2 communication model: Topic-based publish/subscribe
- Learn how to debug using the CLI
- Set up Mac IDE for ROS2 development on Ubuntu VM

## Done

- Troubleshot why the UTM shared folder is not accessible
  - not compatible with Mac's ARM64 architecture
- Changed to use SSHFS
  - successfully mounted the shared folder
- Tried CLI commands (echo, hz, info, etc.)
- Created a workspace and package from scratch

## Learned

- setup SSHFS
- create a new workspace and package

# DAY 0

## Goal

- Able to run `ros2` commands without errors
- Able to run a ROS 2 demo (turtlesim / minimal pub-sub)

## Done

- on my M2 Macbook, installed
  - UTM
  - Ubuntu: 22.04.5 LTS (more compatible with ROS 2 Humble, while 24.04 is for Jazzy)
  - both Ubuntu Server and Desktop
  - ROS
  - colcon
- ran the two demos: turtlesim / minimal pub-sub

## Learned

- What are the differences between: Perception / Planning / Control
- understand what layer cmd_vel is in
- ROS 2 vs bare metal
- know what is Nav2
- real-time vs. fast (Deterministic Latency)
